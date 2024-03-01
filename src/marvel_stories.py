import json
from metadata import Metadata
import utils


class MarvelStories:
    """
    Class representing the marvel entity Stories
    """

    relations_list = []

    def __init__(self, marvelAPI):
        self.marvelAPI = marvelAPI
        if "stories" not in Metadata.data:
            self.initial_metadata()

    @staticmethod
    def initial_metadata(state: str = "initial"):
        """
        Sets the way initial metadata should look like
        """
        last_timestamp = 0
        last_timestamp_processed = 0
        if state != "initial":
            last_timestamp = Metadata.data.get("stories").get("last_modified_ts", 0)
            last_timestamp_processed = Metadata.data.get("stories").get(
                "last_processed_ts", 0
            )

        Metadata.data["stories"] = {
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
        util_functions.delete_csv("stories.csv")

    def filter_stories(self, list_results: list) -> list:
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
                    "type": el.get("type", None),
                    "modified": el.get("modified", None),
                    "modified_ts": util_functions.convert_to_unix_ts(
                        el.get("modified", None)
                    ),
                    "thumbnail": json.dumps(el.get("thumbnail", {})),
                    "available_comics": el.get("comics").get("available"),
                    "available_series": el.get("series").get("available"),
                    "available_events": el.get("events").get("available"),
                    "available_characters": el.get("characters").get("available"),
                    "available_creators": el.get("creators").get("available"),
                    "originalissue": json.dumps(el.get("originalissue", None)),
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
            for story in raw_results:
                relation = story.get(relation_type)
                if relation.get("available") != relation.get("returned"):
                    Metadata.data["stories"]["rel_" + relation_type][
                        story.get("id")
                    ] = relation.get("collectionURI")
                else:
                    relations_list = []
                    for relation_item in relation.get("items"):
                        extracted_id = util_functions.extract_id(
                            relation_item.get("resourceURI")
                        )
                        relations_list.append(
                            {
                                "story_id": story.get("id"),
                                relation_type + "_id": extracted_id,
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_stories_" + relation_type
                        )

    def process_results(self, raw_results: list, filtered_results: list):
        """
        Processes the stories' data
        :param:
        raw_results (list): raw stories' data
        filtered_results (list): filtered data to be used
        """
        util_functions.write_data_to_csv(filtered_results, "stories")
        self.process_relations(raw_results)

    def get_stories(self):
        """
        Collects the raw data and the filtered data for stories entity modifying the metadata as well
        """
        stories_metadata = Metadata.data.get("stories")
        last_modified_ts = stories_metadata.get("last_modified_ts")
        if stories_metadata.get("state") == "initial":
            last_modified_ts = 0

        filtered_results = []
        while (
            stories_metadata.get("processed_items") < stories_metadata.get("total")
            or stories_metadata.get("total") == 0
        ):
            stories_data = self.marvelAPI.get_marvel_data(
                endpoint="stories",
                offset=stories_metadata.get("offset", 0),
                modifiedSince=last_modified_ts,
            )

            stories_metadata["total"] = stories_data.get("data").get("total")
            stories_metadata["offset"] = stories_data.get("data").get("offset") + 100
            stories_metadata["processed_items"] += stories_data.get("data").get("count")

            raw_results = stories_data.get("data").get("results")
            # because of a bug in the API, total might be bigger than processed
            if len(raw_results) == 0:
                break

            filtered_results = self.filter_stories(raw_results)
            self.process_results(raw_results, filtered_results)

        if len(filtered_results) > 0:
            # because of the broken API the sort by modified is not working properly, we need to loop
            for element in filtered_results:
                if element["modified_ts"] > stories_metadata["last_modified_ts"]:
                    stories_metadata["last_modified_ts"] = element["modified_ts"]

    def get_relations(self):
        """
        Creates the relation list of story_id and rel_id and updates the metadata (tasks list)
        """
        stories_metadata = Metadata.data.get("stories")
        last_modified_ts = stories_metadata.get("last_modified_ts")
        if stories_metadata.get("state") == "initial":
            last_modified_ts = 0

        for relation_type in self.relations_list:
            if len(stories_metadata.get("rel_" + relation_type)) > 0:
                for story_id in list(stories_metadata.get("rel_" + relation_type)):
                    rel_data_items = self.marvelAPI.get_all_marvel_data(
                        url=stories_metadata.get("rel_" + relation_type).get(story_id),
                        modifiedSince=last_modified_ts,
                    )

                    relations_list = []
                    for relation_item in rel_data_items:
                        relations_list.append(
                            {
                                "story_id": story_id,
                                relation_type + "_id": relation_item.get("id"),
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_stories_" + relation_type
                        )

                    stories_metadata.get("rel_" + relation_type).pop(story_id)

    def ingest(self):
        """
        Main method to be invoked for this class to ingest the data (initial and relations)
        """
        self.get_stories()
        print("Ingesting Stories relations")
        self.get_relations()
        Metadata.data["stories"][
            "last_processed_ts"
        ] = util_functions.get_current_unix_ts()
