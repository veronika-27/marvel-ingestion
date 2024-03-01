import os
import sys
import pytest
from pathlib import Path

source_path = Path(__file__).resolve()
base_dir = source_path.parent.parent
src_path = str(base_dir) + "/src"
sys.path.append(src_path)

from utils import *


@pytest.mark.parametrize(
    "ts_str, expected_result",
    [
        ("2012-07-10T19:11:52-0400", 1341961912),
        ("2015-07-10T19:11:52-0400", 1436569912),
    ],
)
def test_that_converting_string_to_unix_ts_works(ts_str, expected_result):
    assert convert_to_unix_ts(ts_str) == expected_result


@pytest.mark.parametrize(
    "collection_url, expected_result",
    [
        ("http://gateway.marvel.com/v1/public/comics/21366", 21366),
        ("http://gateway.marvel.com/v1/public/comics/24571", 24571),
        ("http://gateway.marvel.com/v1/public/comics", 0),
    ],
)
def test_that_extract_id_correctly_splits_the_url(collection_url, expected_result):
    assert extract_id(collection_url) == expected_result


def test_if_write_data_to_csv_creates_file():
    chars_test_list = [
        {
            "id": 1009250,
            "name": "Countess",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 1,
            "available_stories": 1,
            "available_events": 0,
            "available_series": 1,
        },
        {
            "id": 1009375,
            "name": "Joan the Mouse",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 0,
            "available_stories": 0,
            "available_events": 0,
            "available_series": 0,
        },
        {
            "id": 1009392,
            "name": "La Nuit",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/9/10/4c003d76b5ec6", "extension": "jpg"}',
            "available_comics": 2,
            "available_stories": 2,
            "available_events": 0,
            "available_series": 2,
        },
        {
            "id": 1009456,
            "name": "Morph",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/f/10/4ce5a06d6a8ad", "extension": "jpg"}',
            "available_comics": 21,
            "available_stories": 23,
            "available_events": 1,
            "available_series": 12,
        },
        {
            "id": 1009533,
            "name": "Reavers",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/c0/4c003c63deac8", "extension": "jpg"}',
            "available_comics": 16,
            "available_stories": 15,
            "available_events": 0,
            "available_series": 5,
        },
        {
            "id": 1009601,
            "name": "Sleeper",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 6,
            "available_stories": 6,
            "available_events": 0,
            "available_series": 4,
        },
        {
            "id": 1009653,
            "name": "The Anarchist",
            "description": "",
            "modified": "1969-12-31T19:00:00-0500",
            "modified_ts": "1969-12-31T19:00:00-0500",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/1/60/4c003aacdeca9", "extension": "jpg"}',
            "available_comics": 2,
            "available_stories": 5,
            "available_events": 0,
            "available_series": 2,
        },
    ]
    write_data_to_csv(api_data=chars_test_list, file_name="characters_test")
    assert os.path.exists("characters_test.csv") == True


def test_if_delete_csv_removes_file():
    delete_csv("characters_test.csv")
    assert os.path.exists("characters_test.csv") == False
