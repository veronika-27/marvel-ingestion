import csv
import datetime
import time
import os


def write_data_to_csv(api_data: list, file_name: str):
    """
    Opens a csv file and appends the data (skipping headers) in case of existing csv file or writes
    the data from the api call
    :param:
        api_data (list): list of dictionaries with the data
        file_name (str): the name of the file that will be saved
    """

    file_path = "{file_to_be_saved}.csv".format(file_to_be_saved=file_name)
    marvel_headers = api_data[0].keys()

    if os.path.exists(file_path):
        with open(file_path, "a+", encoding="utf8", newline="") as output_file:
            fc = csv.DictWriter(
                output_file,
                fieldnames=marvel_headers,
                escapechar="\\",
                quoting=csv.QUOTE_NONNUMERIC,
            )
            fc.writerows(api_data)
    else:

        with open(file_path, "w", encoding="utf8", newline="") as output_file:
            fc = csv.DictWriter(
                output_file,
                fieldnames=marvel_headers,
                escapechar="\\",
                quoting=csv.QUOTE_NONNUMERIC,
            )
            fc.writeheader()
            fc.writerows(api_data)


def convert_to_unix_ts(ts_str: str):
    """
    Converts the string representation of a timestamp into unix timestamp
    :param:
    ts_str (str): timestamp with %Y-%m-%dT%H:%M:%S%z format
    :return:
    unix_timestamp (int): unix timestamp
    """

    unix_timestamp = 0
    try:
        datetime_str = datetime.datetime.strptime(ts_str, "%Y-%m-%dT%H:%M:%S%z")
        unix_timestamp = int(datetime_str.timestamp())
    except:
        pass

    if unix_timestamp < 0:
        unix_timestamp = 0

    return unix_timestamp


def get_current_unix_ts():
    """
    Get current unix timestamp
    :return:
    unix_timestamp (int): unix timestamp
    """
    unix_timestamp = int(time.time())
    return unix_timestamp


def extract_id(collectionURI: str):
    """
    Extracts the id from a specific url
    :param:
        collectionURI (str): the URI containing needed id for relations
    :return:
        rel_id (int): the id from related data (in case of error rel_id = 0)
    """
    parts = collectionURI.split("/")
    try:
        rel_id = int(parts[-1])
        return rel_id
    except:
        return 0


def delete_csv(path):
    """
    Deletes the csv-s of specific path

    :param:
        path (str): concrete file path
    """
    os.remove(path)
