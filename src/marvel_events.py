import json
from metadata import Metadata
import utils


class MarvelEvents:
    """
    Class representing the marvel entity Events
    """

    relations_list = []

    def __init__(self, marvelAPI):
        self.marvelAPI = marvelAPI
        if "events" not in Metadata.data:
            self.initial_metadata()

    @staticmethod
    def initial_metadata(state: str = "initial"):
        """
        Sets the way initial metadata should look like
        """
        last_timestamp = 0
        last_timestamp_processed = 0
        if state != "initial":
            last_timestamp = Metadata.data.get("events").get("last_modified_ts", 0)
            last_timestamp_processed = Metadata.data.get("events").get(
                "last_processed_ts", 0
            )

        Metadata.data["events"] = {
            "state": state,
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": last_timestamp,
            "last_processed_ts": last_timestamp_processed,
        }

    @staticmethod
    def delete_csv() -> object:
        """
        Deletes the csv-s with initial events created previously
        """
        util_functions.delete_csv("events.csv")

    def filter_events(self, list_results: list) -> list:
        """
        Filters the raw data returned
        :param
        list_results (list): list of dictionaries with raw data
        :return:
            filtered_results (list): list of dictionaries with the needed (filtered data)
        """
        filtered_results = []

        for el in list_results:
            filtered_results.append(
                {
                    "id": el.get("id", None),
                    "title": el.get("title", None),
                    "description": el.get("description", None),
                    "resourceURI": el.get("resourceURI", None),
                    "urls": json.dumps(el.get("urls", None)),
                    "modified": el.get("modified", None),
                    "modified_ts": util_functions.convert_to_unix_ts(
                        el.get("modified", None)
                    ),
                    "start": el.get("start", None),
                    "end": el.get("end", None),
                    "thumbnail": json.dumps(el.get("thumbnail", {})),
                    "available_comics": el.get("comics").get("available"),
                    "available_stories": el.get("stories").get("available"),
                    "available_series": el.get("series").get("available"),
                    "available_characters": el.get("characters").get("available"),
                    "available_creators": el.get("creators").get("available"),
                    "next": json.dumps(el.get("next", None)),
                    "previous": json.dumps(el.get("previous", None)),
                }
            )

        return filtered_results

    def process_relations(self, raw_results: list):
        """
        Updates the metadata (tasks list) and if available relations can be exhausted (less than 20) writes them into csv
        :param:
         raw_results (list): list of dictionaries with raw results
        """
        for relation_type in self.relations_list:
            for event in raw_results:
                relation = event.get(relation_type)
                if relation.get("available") != relation.get("returned"):
                    Metadata.data["events"]["rel_" + relation_type][
                        event.get("id")
                    ] = relation.get("collectionURI")
                else:
                    relations_list = []
                    for relation_item in relation.get("items"):
                        extracted_id = util_functions.extract_id(
                            relation_item.get("resourceURI")
                        )
                        relations_list.append(
                            {
                                "event_id": event.get("id"),
                                relation_type + "_id": extracted_id,
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_events_" + relation_type
                        )

    def process_results(self, raw_results: list, filtered_results: list):
        """
        Processes the events' data
        :param:
        raw_results (list): raw events' data
        filtered_results (list): filtered data to be used
        """
        util_functions.write_data_to_csv(filtered_results, "events")
        self.process_relations(raw_results)

    def get_events(self):
        """
        Collects the raw data and the filtered data for events entity modifying the metadata as well
        """
        events_metadata = Metadata.data.get("events")
        last_modified_ts = events_metadata.get("last_modified_ts")
        if events_metadata.get("state") == "initial":
            last_modified_ts = 0

        filtered_results = []
        while (
            events_metadata.get("processed_items") < events_metadata.get("total")
            or events_metadata.get("total") == 0
        ):
            events_data = self.marvelAPI.get_marvel_data(
                endpoint="events",
                offset=events_metadata.get("offset", 0),
                modifiedSince=last_modified_ts,
            )

            events_metadata["total"] = events_data.get("data").get("total")
            events_metadata["offset"] = events_data.get("data").get("offset") + 100
            events_metadata["processed_items"] += events_data.get("data").get("count")

            raw_results = events_data.get("data").get("results")
            # because of a bug in the API, total might be bigger than processed
            if len(raw_results) == 0:
                break

            filtered_results = self.filter_events(raw_results)
            self.process_results(raw_results, filtered_results)

        if len(filtered_results) > 0:
            # because of the broken API the sort by modified is not working properly, we need to loop
            for element in filtered_results:
                if element["modified_ts"] > events_metadata["last_modified_ts"]:
                    events_metadata["last_modified_ts"] = element["modified_ts"]

    def get_relations(self):
        """
        Creates the relation list of event_id and rel_id and updates the metadata (tasks list)
        """
        events_metadata = Metadata.data.get("events")
        last_modified_ts = events_metadata.get("last_modified_ts")
        if events_metadata.get("state") == "initial":
            last_modified_ts = 0

        for relation_type in self.relations_list:
            if len(events_metadata.get("rel_" + relation_type)) > 0:
                for event_id in list(events_metadata.get("rel_" + relation_type)):
                    rel_data_items = self.marvelAPI.get_all_marvel_data(
                        url=events_metadata.get("rel_" + relation_type).get(event_id),
                        modifiedSince=last_modified_ts,
                    )

                    relations_list = []
                    for relation_item in rel_data_items:
                        relations_list.append(
                            {
                                "event_id": event_id,
                                relation_type + "_id": relation_item.get("id"),
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_events_" + relation_type
                        )

                    events_metadata.get("rel_" + relation_type).pop(event_id)

    def ingest(self):
        """
        Main method to be invoked for this class to ingest the data (initial and relations)
        """
        self.get_events()
        print("Ingesting Events relations...")
        self.get_relations()
        Metadata.data["events"][
            "last_processed_ts"
        ] = util_functions.get_current_unix_ts()
