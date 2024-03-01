import json
from metadata import Metadata
import utils


class MarvelCreators:
    """
    Class representing the marvel entity Creators
    """

    relations_list = ["comics"]

    def __init__(self, marvelAPI):
        self.marvelAPI = marvelAPI
        if "creators" not in Metadata.data:
            self.initial_metadata()

    @staticmethod
    def initial_metadata(state: str = "initial"):
        """
        Sets the way initial metadata should look like
        """
        last_timestamp = 0
        last_timestamp_processed = 0
        if state != "initial":
            last_timestamp = Metadata.data.get("creators").get("last_modified_ts", 0)
            last_timestamp_processed = Metadata.data.get("creators").get(
                "last_processed_ts", 0
            )

        Metadata.data["creators"] = {
            "state": state,
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": last_timestamp,
            "last_processed_ts": last_timestamp_processed,
            "rel_comics": {},
        }

    @staticmethod
    def delete_csv():
        """
        Deletes the csv-s with initial creators data and relational data created previously
        """
        util_functions.delete_csv("creators.csv")
        util_functions.delete_csv("rel_creators_comics.csv")

    def filter_creators(self, list_results: list) -> list:
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
                    "firstName": el.get("firstName", None),
                    "middleName": el.get("middleName", None),
                    "lastName": el.get("lastName", None),
                    "suffix": el.get("suffix", None),
                    "fullName": el.get("fullName", None),
                    "modified": el.get("modified", None),
                    "modified_ts": util_functions.convert_to_unix_ts(
                        el.get("modified", None)
                    ),
                    "resourceURI": el.get("resourceURI", None),
                    "urls": json.dumps(el.get("urls", {})),
                    "thumbnail": json.dumps(el.get("thumbnail", {})),
                    "available_comics": el.get("comics").get("available"),
                    "available_stories": el.get("stories").get("available"),
                    "available_events": el.get("events").get("available"),
                    "available_series": el.get("series").get("available"),
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
            for creator in raw_results:
                relation = creator.get(relation_type)
                if relation.get("available") != relation.get("returned"):
                    Metadata.data["creators"]["rel_" + relation_type][
                        creator.get("id")
                    ] = relation.get("collectionURI")
                else:
                    relations_list = []
                    for relation_item in relation.get("items"):
                        extracted_id = util_functions.extract_id(
                            relation_item.get("resourceURI")
                        )
                        relations_list.append(
                            {
                                "creator_id": creator.get("id"),
                                relation_type + "_id": extracted_id,
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_creators_" + relation_type
                        )

    def process_results(self, raw_results: list, filtered_results: list):
        """
        Processes the creators' data
        :param:
        raw_results (list): raw creators' data
        filtered_results (list): filtered data to be used
        """
        util_functions.write_data_to_csv(filtered_results, "creators")
        self.process_relations(raw_results)

    def get_creators(self):
        """
        Collects the raw data and the filtered data for creators entity modifying the metadata as well
        """
        creators_metadata = Metadata.data.get("creators")
        last_modified_ts = creators_metadata.get("last_modified_ts")
        if creators_metadata.get("state") == "initial":
            last_modified_ts = 0

        filtered_results = []
        while (
            creators_metadata.get("processed_items") < creators_metadata.get("total")
            or creators_metadata.get("total") == 0
        ):
            creators_data = self.marvelAPI.get_marvel_data(
                endpoint="creators",
                offset=creators_metadata.get("offset", 0),
                modifiedSince=last_modified_ts,
            )

            creators_metadata["total"] = creators_data.get("data").get("total")
            creators_metadata["offset"] = creators_data.get("data").get("offset") + 100
            creators_metadata["processed_items"] += creators_data.get("data").get(
                "count"
            )

            raw_results = creators_data.get("data").get("results")
            # because of a bug in the API, total might be bigger than processed
            if len(raw_results) == 0:
                break

            filtered_results = self.filter_creators(raw_results)
            self.process_results(raw_results, filtered_results)

        if len(filtered_results) > 0:
            # because of the broken API the sort by modified is not working properly, we need to loop
            for element in filtered_results:
                if element["modified_ts"] > creators_metadata["last_modified_ts"]:
                    creators_metadata["last_modified_ts"] = element["modified_ts"]

    def get_relations(self):
        """
        Creates the relation list of creator_id and rel_id and updates the metadata (tasks list)
        """
        creators_metadata = Metadata.data.get("creators")
        last_modified_ts = creators_metadata.get("last_modified_ts")
        if creators_metadata.get("state") == "initial":
            last_modified_ts = 0

        for relation_type in self.relations_list:
            if len(creators_metadata.get("rel_" + relation_type)) > 0:
                for creator_id in list(creators_metadata.get("rel_" + relation_type)):
                    rel_data_items = self.marvelAPI.get_all_marvel_data(
                        url=creators_metadata.get("rel_" + relation_type).get(
                            creator_id
                        ),
                        modifiedSince=last_modified_ts,
                    )

                    relations_list = []
                    for relation_item in rel_data_items:
                        relations_list.append(
                            {
                                "creator_id": creator_id,
                                relation_type + "_id": relation_item.get("id"),
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_creators_" + relation_type
                        )

                    creators_metadata.get("rel_" + relation_type).pop(creator_id)

    def ingest(self):
        """
        Main method to be invoked for this class to ingest the data (initial and relations)
        """
        self.get_creators()
        print("Ingesting Creators relations")
        self.get_relations()
        Metadata.data["creators"][
            "last_processed_ts"
        ] = util_functions.get_current_unix_ts()
