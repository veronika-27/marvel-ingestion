import os
import sys
from pathlib import Path

source_path = Path(__file__).resolve()
base_dir = source_path.parent.parent
src_path = str(base_dir) + "/src"
sys.path.append(src_path)

from metadata import Metadata


def test_if_metadata_save_creates_metadata_json_correctly():
    Metadata.data["characters"] = {
        "state": "initial",
        "total": 0,
        "offset": 0,
        "processed_items": 0,
        "last_modified_ts": 1,
        "rel_comics": {},
        "rel_events": {},
    }
    Metadata.data["comics"] = (
        {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "last_processed_ts": 0,
        },
    )
    Metadata.data["creators"] = {
        "state": "initial",
        "total": 0,
        "offset": 0,
        "processed_items": 0,
        "last_modified_ts": 1,
        "last_processed_ts": 0,
        "rel_comics": {},
    }
    Metadata.data["events"] = {
        "state": "initial",
        "total": 0,
        "offset": 0,
        "processed_items": 0,
        "last_modified_ts": 1,
        "last_processed_ts": 0,
    }
    Metadata.data["series"] = (
        {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "last_processed_ts": 0,
        },
    )
    Metadata.data["stories"] = {
        "state": "initial",
        "total": 0,
        "offset": 0,
        "processed_items": 0,
        "last_modified_ts": 1,
        "last_processed_ts": 0,
    }

    Metadata.load()
    Metadata.save()
    assert os.path.exists("metadata.json") == True


def test_if_metadata_load_creates_metadata_updates_json_correctly():
    test_meta = Metadata()
    initial_metadata = Metadata.data
    test_meta.load()
    print(initial_metadata)
    assert initial_metadata == {
        "characters": {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "rel_comics": {},
            "rel_events": {},
        },
        "comics": (
            {
                "state": "initial",
                "total": 0,
                "offset": 0,
                "processed_items": 0,
                "last_modified_ts": 1,
                "last_processed_ts": 0,
            },
        ),
        "creators": {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "last_processed_ts": 0,
            "rel_comics": {},
        },
        "events": {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "last_processed_ts": 0,
        },
        "series": (
            {
                "state": "initial",
                "total": 0,
                "offset": 0,
                "processed_items": 0,
                "last_modified_ts": 1,
                "last_processed_ts": 0,
            },
        ),
        "stories": {
            "state": "initial",
            "total": 0,
            "offset": 0,
            "processed_items": 0,
            "last_modified_ts": 1,
            "last_processed_ts": 0,
        },
    }
