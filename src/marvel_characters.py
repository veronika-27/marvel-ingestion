import json
from metadata import Metadata
import utils


class MarvelCharacters:
    """
    Class representing the marvel entity Characters
    """

    relations_list = ["comics", "events"]

    def __init__(self, marvelAPI):
        self.marvelAPI = marvelAPI
        if "characters" not in Metadata.data:
            self.initial_metadata()

    @staticmethod
    def initial_metadata(state: str = "initial"):
        """
        Sets the way initial metadata should look like
        """
        last_timestamp = 0
        last_timestamp_processed = 0
        if state != "initial":
            last_timestamp = Metadata.data.get("characters").get("last_modified_ts", 0)
            last_timestamp_processed = Metadata.data.get("characters").get(
                "last_processed_ts", 0
            )

        Metadata.data["characters"] = {
            "state": state,
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": last_timestamp,
            "last_processed_ts": last_timestamp_processed,
            "rel_comics": {},
            "rel_events": {},
        }

    @staticmethod
    def delete_csv():
        """
        Deletes the csv-s with initial characters data and relational data created previously
        """
        util_functions.delete_csv("characters.csv")
        util_functions.delete_csv("rel_characters_comics.csv")
        util_functions.delete_csv("rel_characters_events.csv")

    def filter_characters(self, list_results: list) -> list:
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
                    "name": el.get("name", None),
                    "description": el.get("description", None),
                    "modified": el.get("modified", None),
                    "modified_ts": util_functions.convert_to_unix_ts(
                        el.get("modified", None)
                    ),
                    "resourceURI": el.get("resourceURI", None),
                    "urls": json.dumps(el.get("urls", None)),
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
            for character in raw_results:
                relation = character.get(relation_type)
                if relation.get("available") != relation.get("returned"):
                    Metadata.data["characters"]["rel_" + relation_type][
                        character.get("id")
                    ] = relation.get("collectionURI")
                else:
                    relations_list = []
                    for relation_item in relation.get("items"):
                        extracted_id = util_functions.extract_id(
                            relation_item.get("resourceURI")
                        )
                        relations_list.append(
                            {
                                "character_id": character.get("id"),
                                relation_type + "_id": extracted_id,
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_characters_" + relation_type
                        )

    def process_results(self, raw_results: list, filtered_results: list):
        """
        Processes the characters' data
        :param:
        raw_results (list): raw characters' data
        filtered_results (list): filtered data to be used
        """
        util_functions.write_data_to_csv(filtered_results, "characters")
        self.process_relations(raw_results)

    def get_characters(self):
        """
        Collects the raw data and the filtered data for characters entity modifying the metadata as well
        """
        char_metadata = Metadata.data.get("characters")
        last_modified_ts = char_metadata.get("last_modified_ts")
        if char_metadata.get("state") == "initial":
            last_modified_ts = 0

        filtered_results = []
        while (
            char_metadata.get("processed_items") < char_metadata.get("total")
            or char_metadata.get("total") == 0
        ):
            char_data = self.marvelAPI.get_marvel_data(
                endpoint="characters",
                offset=char_metadata.get("offset", 0),
                modifiedSince=last_modified_ts,
            )

            char_metadata["total"] = char_data.get("data").get("total")
            char_metadata["offset"] = char_data.get("data").get("offset") + 100
            char_metadata["processed_items"] += char_data.get("data").get("count")

            raw_results = char_data.get("data").get("results")
            # because of a bug in the API, total might be bigger than processed
            if len(raw_results) == 0:
                break

            filtered_results = self.filter_characters(raw_results)
            self.process_results(raw_results, filtered_results)

        if len(filtered_results) > 0:
            # because of the broken API the sort by modified is not working properly, we need to loop
            for element in filtered_results:
                if element["modified_ts"] > char_metadata["last_modified_ts"]:
                    char_metadata["last_modified_ts"] = element["modified_ts"]

            # last_element = filtered_results[-1]
            # char_metadata["last_modified_ts"] = last_element["modified_ts"]

    def get_relations(self):
        """
        Creates the relation list of character_id and rel_id and updates the metadata (tasks list)
        """
        char_metadata = Metadata.data.get("characters")
        last_modified_ts = char_metadata.get("last_modified_ts")
        if char_metadata.get("state") == "initial":
            last_modified_ts = 0

        for relation_type in self.relations_list:
            if len(char_metadata.get("rel_" + relation_type)) > 0:
                # print("Relation " + relation_type + " : " + str(len(char_metadata.get("rel_" + relation_type))))
                # rel_processed=1
                for character_id in list(char_metadata.get("rel_" + relation_type)):
                    rel_data_items = self.marvelAPI.get_all_marvel_data(
                        url=char_metadata.get("rel_" + relation_type).get(character_id),
                        modifiedSince=last_modified_ts,
                    )

                    relations_list = []
                    for relation_item in rel_data_items:
                        relations_list.append(
                            {
                                "character_id": character_id,
                                relation_type + "_id": relation_item.get("id"),
                            }
                        )
                    if len(relations_list) > 0:
                        util_functions.write_data_to_csv(
                            relations_list, "rel_characters_" + relation_type
                        )

                    char_metadata.get("rel_" + relation_type).pop(character_id)
                    # print("Processed " + rel_processed)
                    # rel_processed += 1

    def ingest(self):
        """
        Main method to be invoked for this class to ingest the data (initial and relations)
        """
        self.get_characters()
        print("Ingesting character relations")
        self.get_relations()
        Metadata.data["characters"][
            "last_processed_ts"
        ] = util_functions.get_current_unix_ts()
