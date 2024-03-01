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

from marvel_stories import MarvelStories
from marvelapi import MarvelAPI


def test_get_stories():
    when(time).sleep(...).thenReturn(0)

    stories_obj = MarvelStories(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 118778,
            "count": 2,
            "results": [
                {
                    "id": 221267,
                    "title": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #1",
                    "description": "",
                    "resourceURI": "http://gateway.marvel.com/v1/public/stories/221267",
                    "type": "cover",
                    "modified": "2022-03-04T14:43:23-0500",
                    "thumbnail": "null",
                    "creators": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/221267/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/14333",
                                "name": "Katelyn Gregorowicz",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13539",
                                "name": "Robert Quinn",
                                "role": "penciller (cover)",
                            },
                        ],
                        "returned": 2,
                    },
                    "characters": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/221267/characters",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009407",
                                "name": "Loki",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009664",
                                "name": "Thor",
                            },
                        ],
                        "returned": 2,
                    },
                    "series": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/221267/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/34402",
                                "name": "Alligator Loki Infinity Comic (2022)",
                            }
                        ],
                        "returned": 1,
                    },
                    "comics": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/221267/comics",
                        "items": [],
                        "returned": 1,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/221267/events",
                        "items": [],
                        "returned": 0,
                    },
                    "originalIssue": "null",
                },
                {
                    "id": 209402,
                    "title": "story from Marvel Fairytales Vertical Comic (2021) #3",
                    "description": "",
                    "resourceURI": "http://gateway.marvel.com/v1/public/stories/209402",
                    "type": "story",
                    "modified": "2022-03-04T14:39:06-0500",
                    "thumbnail": "null",
                    "creators": {
                        "available": 5,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/209402/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12694",
                                "name": "Gustavo Duarte",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12996",
                                "name": "Ian Herring",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12376",
                                "name": "Wilson Moss",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12465",
                                "name": "Ryan North",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12974",
                                "name": "Vc Joe Sabino",
                                "role": "letterer",
                            },
                        ],
                        "returned": 5,
                    },
                    "characters": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/209402/characters",
                        "items": [],
                        "returned": 0,
                    },
                    "series": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/209402/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32123",
                                "name": "Marvel Fairy Tales Infinity Comic (2022)",
                            }
                        ],
                        "returned": 1,
                    },
                    "comics": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/209402/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94142",
                                "name": "Marvel Fairy Tales Infinity Comic (2022) #3",
                            }
                        ],
                        "returned": 1,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/stories/209402/events",
                        "items": [],
                        "returned": 0,
                    },
                    "originalIssue": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/comics/94142",
                        "name": "Marvel Fairy Tales Infinity Comic (2022) #3",
                    },
                },
            ],
        }
    }

    expected_results = [
        {
            "id": 221267,
            "title": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #1",
            "description": "",
            "resourceURI": "http://gateway.marvel.com/v1/public/stories/221267",
            "type": "cover",
            "modified": "2022-03-04T14:43:23-0500",
            "modified_ts": 1646423003,
            "thumbnail": '"null"',
            "available_comics": 1,
            "available_series": 1,
            "available_events": 0,
            "available_characters": 2,
            "available_creators": 2,
            "originalissue": "null",
        },
        {
            "id": 209402,
            "title": "story from Marvel Fairytales Vertical Comic (2021) #3",
            "description": "",
            "resourceURI": "http://gateway.marvel.com/v1/public/stories/209402",
            "type": "story",
            "modified": "2022-03-04T14:39:06-0500",
            "modified_ts": 1646422746,
            "thumbnail": '"null"',
            "available_comics": 1,
            "available_series": 1,
            "available_events": 0,
            "available_characters": 0,
            "available_creators": 5,
            "originalissue": "null",
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(stories_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            try:
                stories_obj.get_stories()
                assert True
            except InvocationError:
                assert False
