import json
import os


class Metadata:
    """
    A class to represent the metadata for further usage (as tasks list for the program)
    ...

    Methods
    -------
    load (self): method that reads the metadata saved so far
    save (self): method that writes the data from our dictionary in metadata.json with current metadata
    """

    data = {}

    @staticmethod
    def load():
        if not Metadata.data and os.path.exists("metadata.json"):
            with open("metadata.json", "r") as f:
                Metadata.data = json.load(f)

    @staticmethod
    def save():
        if not Metadata.data:
            return
        json_str = json.dumps(Metadata.data)
        with open("metadata.json", "w") as f:
            f.write(json_str)
