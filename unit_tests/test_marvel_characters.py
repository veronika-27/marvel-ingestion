import sys
from pathlib import Path
import time
import requests
from mockito import when, mock
from mockito.invocation import InvocationError

source_path = Path(__file__).resolve()
base_dir = source_path.parent.parent
src_path = str(base_dir) + "/src"
sys.path.append(src_path)

from marvel_characters import MarvelCharacters
from marvelapi import MarvelAPI
from metadata import Metadata
import utils


def test_get_characters():
    when(time).sleep(...).thenReturn(0)

    char_obj = MarvelCharacters(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 2,
            "count": 2,
            "results": [
                {
                    "id": 1011896,
                    "name": "Taurus (Cornelius van Lunt)",
                    "description": "New York businessman Cornelius van Lunt started a lucrative career in legitimate real estate dealing, but he later branched out into various criminal endeavors.",
                    "modified": "2021-08-27T22:16:58-0400",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                        "extension": "jpg",
                    },
                    "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011896",
                    "comics": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011896/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/7334",
                                "name": "Avengers (1963) #81",
                            }
                        ],
                        "returned": 1,
                    },
                    "series": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011896/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/1991",
                                "name": "Avengers (1963 - 1996)",
                            }
                        ],
                        "returned": 1,
                    },
                    "stories": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011896/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/15231",
                                "name": "When Dies a Legend",
                                "type": "interiorStory",
                            }
                        ],
                        "returned": 1,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1011896/events",
                        "items": [],
                        "returned": 0,
                    },
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/characters/1011896/taurus_cornelius_van_lunt?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "wiki",
                            "url": "http://marvel.com/universe/Taurus_(Cornelius_van_Lunt)?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "comiclink",
                            "url": "http://marvel.com/comics/characters/1011896/taurus_cornelius_van_lunt?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                    ],
                },
                {
                    "id": 1013504,
                    "name": "Technarchy",
                    "description": "",
                    "modified": "2021-08-27T22:14:12-0400",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                        "extension": "jpg",
                    },
                    "resourceURI": "http://gateway.marvel.com/v1/public/characters/1013504",
                    "comics": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1013504/comics",
                        "items": [],
                        "returned": 0,
                    },
                    "series": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1013504/series",
                        "items": [],
                        "returned": 0,
                    },
                    "stories": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1013504/stories",
                        "items": [],
                        "returned": 0,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/characters/1013504/events",
                        "items": [],
                        "returned": 0,
                    },
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/characters/1013504/technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "wiki",
                            "url": "http://marvel.com/universe/Technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "comiclink",
                            "url": "http://marvel.com/comics/characters/1013504/technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                    ],
                },
            ],
        }
    }

    expected_results = [
        {
            "id": 1011896,
            "name": "Taurus (Cornelius van Lunt)",
            "description": "New York businessman Cornelius van Lunt started a lucrative career in legitimate real estate dealing, but he later branched out into various criminal endeavors.",
            "modified": "2021-08-27T22:16:58-0400",
            "modified_ts": 1630117018,
            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011896",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/characters/1011896/taurus_cornelius_van_lunt?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "wiki", "url": "http://marvel.com/universe/Taurus_(Cornelius_van_Lunt)?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "comiclink", "url": "http://marvel.com/comics/characters/1011896/taurus_cornelius_van_lunt?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 1,
            "available_stories": 1,
            "available_events": 0,
            "available_series": 1,
        },
        {
            "id": 1013504,
            "name": "Technarchy",
            "description": "",
            "modified": "2021-08-27T22:14:12-0400",
            "modified_ts": 1630116852,
            "resourceURI": "http://gateway.marvel.com/v1/public/characters/1013504",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/characters/1013504/technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "wiki", "url": "http://marvel.com/universe/Technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "comiclink", "url": "http://marvel.com/comics/characters/1013504/technarchy?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 0,
            "available_stories": 0,
            "available_events": 0,
            "available_series": 0,
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(char_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            # print(char_obj.filter_characters(raw_response.get('data').get('results')))
            try:
                char_obj.get_characters()
                assert True
            except InvocationError:
                assert False


def test_if_get_relations_returns_expected_results():
    when(time).sleep(...).thenReturn(0)
    char_obj = MarvelCharacters(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )
    char_obj.initial_metadata("initial")
    Metadata.data["characters"]["rel_comics"] = {12345: "https://example.com/rel/url"}

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 2,
            "count": 2,
            "results": [{"id": 111222}, {"id": 333444}],
        }
    }
    expected_csv_input = [
        {"character_id": 12345, "comics_id": 111222},
        {"character_id": 12345, "comics_id": 333444},
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(utils).write_data_to_csv(
            expected_csv_input, "rel_characters_comics"
        ).thenReturn(True):
            try:
                char_obj.get_relations()
                assert True
            except InvocationError:
                assert False

    if len(Metadata.data["characters"]["rel_comics"]) > 0:
        assert False
