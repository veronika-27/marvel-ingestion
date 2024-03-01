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

from marvel_series import MarvelSeries
from marvelapi import MarvelAPI


def test_get_series():
    when(time).sleep(...).thenReturn(0)

    series_obj = MarvelSeries(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 12785,
            "count": 2,
            "results": [
                {
                    "id": 34402,
                    "title": "Alligator Loki Infinity Comic (2022)",
                    "description": "null",
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/34402",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/series/34402/alligator_loki_infinity_comic_2022?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        }
                    ],
                    "startYear": 2022,
                    "endYear": 2022,
                    "rating": "",
                    "type": "",
                    "modified": "2022-03-04T14:50:57-0500",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                        "extension": "jpg",
                    },
                    "creators": {
                        "available": 4,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/34402/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/14333",
                                "name": "Katelyn Gregorowicz",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13339",
                                "name": "Pete Pantazis",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13539",
                                "name": "Robert Quinn",
                                "role": "penciller (cover)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13917",
                                "name": "Alyssa Wong",
                                "role": "writer",
                            },
                        ],
                        "returned": 4,
                    },
                    "characters": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/34402/characters",
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
                    "stories": {
                        "available": 24,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/34402/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221267",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #1",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221268",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221269",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #2",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221270",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #2",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221271",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #3",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221272",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #3",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221273",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #4",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221274",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #4",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221275",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #5",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221276",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #5",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221277",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #6",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221278",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #6",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221279",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #7",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221280",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #7",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221281",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #8",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221282",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #8",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221283",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #9",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221284",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #9",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221285",
                                "name": "cover from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #10",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/221286",
                                "name": "story from Black Panther: Who Is the Black Panther? Infinity Comic (2022) #10",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 20,
                    },
                    "comics": {
                        "available": 1,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/34402/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/100083",
                                "name": "Alligator Loki Infinity Comic (2022) #1",
                            }
                        ],
                        "returned": 1,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/34402/events",
                        "items": [],
                        "returned": 0,
                    },
                    "next": "null",
                    "previous": "null",
                },
                {
                    "id": 20432,
                    "title": "The Amazing Spider-Man (2015 - 2018)",
                    "description": "null",
                    "resourceURI": "http://gateway.marvel.com/v1/public/series/20432",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/series/20432/the_amazing_spider-man_2015_-_2018?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        }
                    ],
                    "startYear": 2015,
                    "endYear": 2018,
                    "rating": "",
                    "type": "",
                    "modified": "2022-03-03T15:34:09-0500",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/9/e0/575ef296bfd40",
                        "extension": "jpg",
                    },
                    "creators": {
                        "available": 84,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/20432/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8542",
                                "name": "Gerry Alanguilan",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12865",
                                "name": "Raymund Bermudez",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11875",
                                "name": "Nick Bradshaw",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13162",
                                "name": "Erick Arciniega",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12989",
                                "name": "Jordie Bellaire",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13215",
                                "name": "Rain Beredo",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11543",
                                "name": "Dan Brown",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12604",
                                "name": "Jim Campbell",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8658",
                                "name": "James Asmus",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8652",
                                "name": "Jacob Chabot",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13023",
                                "name": "Cale Atkinson",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13024",
                                "name": "Hannah Blumenreich",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12815",
                                "name": "Andrea Broccardo",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/87",
                                "name": "Mark Bagley",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/9799",
                                "name": "David Baldeon",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/1141",
                                "name": "Giuseppe Camuncoli",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/648",
                                "name": "Simone Bianchi",
                                "role": "penciller (cover)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13068",
                                "name": "J. Scott Campbell",
                                "role": "penciller (cover)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11798",
                                "name": "Matteo Buffagni",
                                "role": "artist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/5251",
                                "name": "Vc Joe Caramagna",
                                "role": "letterer",
                            },
                        ],
                        "returned": 20,
                    },
                    "characters": {
                        "available": 20,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/20432/characters",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009220",
                                "name": "Captain America",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009276",
                                "name": "Doctor Octopus",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011435",
                                "name": "Green Goblin (Norman Osborn)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009619",
                                "name": "Gwen Stacy",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009486",
                                "name": "Harry Osborn",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009356",
                                "name": "Human Torch",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009359",
                                "name": "Hydra",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009368",
                                "name": "Iron Man",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009372",
                                "name": "J. Jonah Jameson",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011288",
                                "name": "Jackal",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009407",
                                "name": "Loki",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009708",
                                "name": "Mary Jane Watson",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011220",
                                "name": "Mockingbird",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009325",
                                "name": "Norman Osborn",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011426",
                                "name": "Scarlet Spider (Kaine)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009590",
                                "name": "Silver Sable",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1017603",
                                "name": "Spider-Gwen (Gwen Stacy)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1016181",
                                "name": "Spider-Man (Miles Morales)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009610",
                                "name": "Spider-Man (Peter Parker)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009663",
                                "name": "Venom (Flash Thompson)",
                            },
                        ],
                        "returned": 20,
                    },
                    "stories": {
                        "available": 163,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/20432/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121639",
                                "name": "cover from The Amazing Spider-Man (2015) #1",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121640",
                                "name": "story from The Amazing Spider-Man (2015) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121643",
                                "name": "cover from The Amazing Spider-Man (2015) #2",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121644",
                                "name": "story from The Amazing Spider-Man (2015) #2",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121645",
                                "name": "cover from The Amazing Spider-Man (2015) #3",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121646",
                                "name": "story from The Amazing Spider-Man (2015) #3",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121647",
                                "name": "cover from The Amazing Spider-Man (2015) #4",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121648",
                                "name": "story from The Amazing Spider-Man (2015) #4",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121649",
                                "name": "cover from The Amazing Spider-Man (2015) #5",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121650",
                                "name": "story from The Amazing Spider-Man (2015) #5",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121651",
                                "name": "cover from The Amazing Spider-Man (2015) #6",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121652",
                                "name": "story from The Amazing Spider-Man (2015) #6",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121653",
                                "name": "cover from The Amazing Spider-Man (2015) #7",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121654",
                                "name": "story from The Amazing Spider-Man (2015) #7",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121655",
                                "name": "cover from The Amazing Spider-Man (2015) #8",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121656",
                                "name": "story from The Amazing Spider-Man (2015) #8",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121657",
                                "name": "cover from The Amazing Spider-Man (2015) #9",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121658",
                                "name": "story from The Amazing Spider-Man (2015) #9",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121659",
                                "name": "cover from The Amazing Spider-Man (2015) #10",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/121660",
                                "name": "story from The Amazing Spider-Man (2015) #10",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 20,
                    },
                    "comics": {
                        "available": 74,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/20432/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/56490",
                                "name": "The Amazing Spider-Man (2015) #1.1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/56494",
                                "name": "The Amazing Spider-Man (2015) #1.4",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/58644",
                                "name": "The Amazing Spider-Man (2017) #1.4 (Francavilla Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/56495",
                                "name": "The Amazing Spider-Man (2017) #1.5",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/56496",
                                "name": "The Amazing Spider-Man (2015) #1.6",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/59852",
                                "name": "The Amazing Spider-Man (2017) #1.6 (Bianchi Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55304",
                                "name": "The Amazing Spider-Man (2017) #6",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55305",
                                "name": "The Amazing Spider-Man (2015) #7",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55308",
                                "name": "The Amazing Spider-Man (2015) #10",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55309",
                                "name": "The Amazing Spider-Man (2015) #11",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55310",
                                "name": "The Amazing Spider-Man (2015) #12",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55311",
                                "name": "The Amazing Spider-Man (2017) #13",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55312",
                                "name": "The Amazing Spider-Man (2017) #14",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55313",
                                "name": "The Amazing Spider-Man (2015) #15",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/59525",
                                "name": "The Amazing Spider-Man (2017) #15 (Panosian Mighty Men Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/61155",
                                "name": "The Amazing Spider-Man (2017) #15 (Js Campbell Exclusive Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/61156",
                                "name": "The Amazing Spider-Man (2015) #15 (Js Campbell Exclusive Black and White Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/62026",
                                "name": "The Amazing Spider-Man (2015) #15 (Alex Ross 2nd Printing Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/55314",
                                "name": "The Amazing Spider-Man (2017) #16",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/60197",
                                "name": "The Amazing Spider-Man (2017) #16 (Samnee Marvel Tsum Tsum Takeover Variant)",
                            },
                        ],
                        "returned": 20,
                    },
                    "events": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/series/20432/events",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/events/332",
                                "name": "Dead No More: The Clone Conspiracy",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/events/336",
                                "name": "Secret Empire",
                            },
                        ],
                        "returned": 2,
                    },
                    "next": "null",
                    "previous": "null",
                },
            ],
        }
    }

    expected_results = [
        {
            "id": 34402,
            "title": "Alligator Loki Infinity Comic (2022)",
            "description": "null",
            "resourceURI": "http://gateway.marvel.com/v1/public/series/34402",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/series/34402/alligator_loki_infinity_comic_2022?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "startYear": 2022,
            "endYear": 2022,
            "rating": "",
            "modified": "2022-03-04T14:50:57-0500",
            "modified_ts": 1646423457,
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 1,
            "available_stories": 24,
            "available_events": 0,
            "available_characters": 2,
            "available_creators": 4,
            "next": '"null"',
            "previous": '"null"',
        },
        {
            "id": 20432,
            "title": "The Amazing Spider-Man (2015 - 2018)",
            "description": "null",
            "resourceURI": "http://gateway.marvel.com/v1/public/series/20432",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/series/20432/the_amazing_spider-man_2015_-_2018?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "startYear": 2015,
            "endYear": 2018,
            "rating": "",
            "modified": "2022-03-03T15:34:09-0500",
            "modified_ts": 1646339649,
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/9/e0/575ef296bfd40", "extension": "jpg"}',
            "available_comics": 74,
            "available_stories": 163,
            "available_events": 2,
            "available_characters": 20,
            "available_creators": 84,
            "next": '"null"',
            "previous": '"null"',
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(series_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            print(series_obj.filter_series(raw_response.get("data").get("results")))
            try:
                series_obj.get_series()
                assert True
            except InvocationError:
                assert False
