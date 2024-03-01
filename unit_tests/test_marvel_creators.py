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

from marvel_creators import MarvelCreators
from marvelapi import MarvelAPI
from metadata import Metadata
import utils


def test_get_creators():
    when(time).sleep(...).thenReturn(0)

    creators_obj = MarvelCreators(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 5666,
            "count": 2,
            "results": [
                {
                    "id": 14075,
                    "firstName": "Vc",
                    "middleName": "Ariana",
                    "lastName": "Maher",
                    "suffix": "",
                    "fullName": "Vc Ariana Maher",
                    "modified": "2022-03-02T09:16:49-0500",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                        "extension": "jpg",
                    },
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/14075",
                    "comics": {
                        "available": 349,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/14075/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/93626",
                                "name": "Aliens: Aftermath (2021) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/95519",
                                "name": "Aliens: Aftermath (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/95520",
                                "name": "Aliens: Aftermath (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/90791",
                                "name": "Amazing Spider-Man: Last Remains Companion (Trade Paperback)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/78359",
                                "name": "Avengers: Marvels Snapshots (2020) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/90483",
                                "name": "Dawn Of X Vol. 16 (Trade Paperback)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94074",
                                "name": "DEMON DAYS: BLOOD FEUD 1 (2022) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/93301",
                                "name": "Demon Days: Cursed Web (2021) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/93300",
                                "name": "Demon Days: Mariko (2021) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94803",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94802",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94805",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94801",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/95151",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94007",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94799",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/95152",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94804",
                                "name": "Demon Days: Mariko (2021) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/94073",
                                "name": "Demon Days: Rising Storm (2021) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/99220",
                                "name": "Demon Days: Rising Storm (2021) #1 (Variant)",
                            },
                        ],
                        "returned": 20,
                    },
                    "series": {
                        "available": 80,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/14075/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31982",
                                "name": "Aliens: Aftermath (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31214",
                                "name": "Amazing Spider-Man: Last Remains Companion (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27946",
                                "name": "Avengers: Marvels Snapshots (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31146",
                                "name": "Dawn Of X Vol. 16 (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32105",
                                "name": "DEMON DAYS: BLOOD FEUD 1 (2022 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31894",
                                "name": "Demon Days: Cursed Web (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31893",
                                "name": "Demon Days: Mariko (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32104",
                                "name": "Demon Days: Rising Storm (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/34154",
                                "name": "Devil's Reign: Superior Four (2022 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29372",
                                "name": "Empyre (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29276",
                                "name": "Empyre: Aftermath Avengers (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/30520",
                                "name": "Empyre: Captain America (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/30847",
                                "name": "Empyre: Captain America & The Avengers (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/30849",
                                "name": "Empyre: Lords Of Empyre (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27547",
                                "name": "Excalibur (2019 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27955",
                                "name": "Excalibur by Tini Howard Vol. 2 (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29727",
                                "name": "Excalibur By Tini Howard Vol. 3 (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32356",
                                "name": "Extreme Carnage (2022)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32341",
                                "name": "Extreme Carnage: Lasher (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32343",
                                "name": "Extreme Carnage: Riot (2021)",
                            },
                        ],
                        "returned": 20,
                    },
                    "stories": {
                        "available": 423,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/14075/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/171605",
                                "name": "story from MARVEL ANTHOLOGY TPB (2029) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/173735",
                                "name": "story from Marvels Snapshots: TBD D (2029) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/173791",
                                "name": "story from EXCALIBUR VOL. 2 TPB (2020) #2",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/178067",
                                "name": "story from Marvel Anthology (2029) #3",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/178069",
                                "name": "story from Marvel Anthology (2029) #4",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/178071",
                                "name": "story from Marvel Anthology (2029) #5",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/178073",
                                "name": "story from Marvel Anthology (2029) #6",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/182453",
                                "name": "story from A4 Epilogue (2020) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/182813",
                                "name": "story from X-Force Annual (2020) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183015",
                                "name": "story from A4 TPB (2019) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183109",
                                "name": "story from Silk (2020) #1",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183113",
                                "name": "story from Silk (2020) #2",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183115",
                                "name": "story from Silk (2020) #3",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183117",
                                "name": "story from Silk (2020) #4",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/183119",
                                "name": "story from Silk (2020) #5",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/186558",
                                "name": "story from Excalibur (2019) #12",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/186560",
                                "name": "story from Excalibur (2019) #13",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/186562",
                                "name": "story from Excalibur (2019) #14",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/186668",
                                "name": "story from EXCALIBUR VOL. 3 TPB (2020) #3",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/186744",
                                "name": "story from SNAPSHOTS TPB (2020) #1",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 20,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/14075/events",
                        "items": [],
                        "returned": 0,
                    },
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/creators/14075/vc_ariana_maher?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        }
                    ],
                },
                {
                    "id": 13180,
                    "firstName": "Federico",
                    "middleName": "",
                    "lastName": "Blee",
                    "suffix": "",
                    "fullName": "Federico Blee",
                    "modified": "2022-03-02T09:16:49-0500",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available",
                        "extension": "jpg",
                    },
                    "resourceURI": "http://gateway.marvel.com/v1/public/creators/13180",
                    "comics": {
                        "available": 274,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/13180/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84343",
                                "name": "2020 Force Works (2020) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84670",
                                "name": "2020 Force Works (2020) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84669",
                                "name": "2020 Force Works (2020) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84344",
                                "name": "2020 Force Works (2020) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84972",
                                "name": "2020 Force Works (2020) #2 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/84345",
                                "name": "2020 Force Works (2020) #3",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/88409",
                                "name": "2020 Force Works (2020) #3 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77061",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77407",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77405",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77406",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #1 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77062",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77409",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #2 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77410",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #2 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77063",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #3",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77411",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #3 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/77412",
                                "name": "Absolute Carnage: Lethal Protectors (2019) #3 (Variant)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/76349",
                                "name": "Aero (2019) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/76350",
                                "name": "Aero (2019) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/76351",
                                "name": "Aero (2019) #3",
                            },
                        ],
                        "returned": 20,
                    },
                    "series": {
                        "available": 78,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/13180/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29693",
                                "name": "2020 Force Works (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27633",
                                "name": "Absolute Carnage: Lethal Protectors (2019)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27392",
                                "name": "Aero (2019 - 2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27397",
                                "name": "Aero Vol. 2: The Mystery Of Madame Huang (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/26332",
                                "name": "Age of X-Man: The Amazing Nightcrawler (2019)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27624",
                                "name": "Agents of Atlas (2019)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27625",
                                "name": "Alpha Flight: True North (2019)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32355",
                                "name": "Amazing Spider-Man: Beyond Vol. 1 (2022)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/25996",
                                "name": "Asgardians of the Galaxy (2018 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31322",
                                "name": "Black Cat (2020 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/31553",
                                "name": "Black Panther (2021 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27618",
                                "name": "Black Panther and the Agents of Wakanda (2019 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29700",
                                "name": "Black Widow (2020 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/22386",
                                "name": "Cable (2017 - 2018)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/33953",
                                "name": "Captain America/Iron Man (2021 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29034",
                                "name": "Champions (2020)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/29119",
                                "name": "Champions Vol. 1: Outlawed (2021)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/27312",
                                "name": "Crazy (2019)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/34025",
                                "name": "Daredevil: Woman Without Fear (2022 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/32069",
                                "name": "Deadpool: Black, White & Blood (2021)",
                            },
                        ],
                        "returned": 20,
                    },
                    "stories": {
                        "available": 298,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/13180/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/123649",
                                "name": "cover from Agents of S.M.a.S.H. (2016) #10",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/133512",
                                "name": "story from Hulk (2017) #11",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/134852",
                                "name": "story from Thanos (2018)",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/140445",
                                "name": "cover from Iceman (2017) #6",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/140821",
                                "name": "cover from Cable (2017) #150",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141212",
                                "name": "cover from Cable (2017) #151",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141289",
                                "name": "story from She-Hulk (2017) #159",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141320",
                                "name": "cover from X-Men: Blue (2017) #15",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141644",
                                "name": "cover from Cable (2017) #152",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141676",
                                "name": "cover from Iceman (2017) #8",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141709",
                                "name": "story from She-Hulk (2017) #160",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/141738",
                                "name": "cover from X-Men: Blue (2017) #18",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/142020",
                                "name": "cover from Cable (2017) #153",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/142565",
                                "name": "story from She-Hulk (2017) #161",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/142808",
                                "name": "cover from X-Men: Gold (2017) #19",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/142972",
                                "name": "cover from Spirits of Vengeance (2017) #4",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/142990",
                                "name": "cover from X-Men: Gold (2017) #20",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/143353",
                                "name": "story from She-Hulk (2017) #162",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/143569",
                                "name": "cover from X-Men: Blue (2017) #21",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/143737",
                                "name": "cover from X-Men: Blue (2017) #22",
                                "type": "cover",
                            },
                        ],
                        "returned": 20,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/creators/13180/events",
                        "items": [],
                        "returned": 0,
                    },
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/creators/13180/federico_blee?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        }
                    ],
                },
            ],
        }
    }

    expected_results = [
        {
            "id": 14075,
            "firstName": "Vc",
            "middleName": "Ariana",
            "lastName": "Maher",
            "suffix": "",
            "fullName": "Vc Ariana Maher",
            "modified": "2022-03-02T09:16:49-0500",
            "modified_ts": 1646230609,
            "resourceURI": "http://gateway.marvel.com/v1/public/creators/14075",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/creators/14075/vc_ariana_maher?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 349,
            "available_stories": 423,
            "available_events": 0,
            "available_series": 80,
        },
        {
            "id": 13180,
            "firstName": "Federico",
            "middleName": "",
            "lastName": "Blee",
            "suffix": "",
            "fullName": "Federico Blee",
            "modified": "2022-03-02T09:16:49-0500",
            "modified_ts": 1646230609,
            "resourceURI": "http://gateway.marvel.com/v1/public/creators/13180",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/creators/13180/federico_blee?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/b/40/image_not_available", "extension": "jpg"}',
            "available_comics": 274,
            "available_stories": 298,
            "available_events": 0,
            "available_series": 78,
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(creators_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            print(creators_obj.filter_creators(raw_response.get("data").get("results")))
            try:
                creators_obj.get_creators()
                assert True
            except InvocationError:
                assert False


def test_if_get_relations_returns_expected_results():
    when(time).sleep(...).thenReturn(0)
    creators_obj = MarvelCreators(
        marvelAPI=MarvelAPI(
            public_key="test",
            private_key="test",
        )
    )
    creators_obj.initial_metadata("initial")
    Metadata.data["creators"]["rel_comics"] = {10: "https://example.com/rel/url"}

    raw_response = {
        "data": {
            "offset": 0,
            "limit": 2,
            "total": 2,
            "count": 2,
            "results": [{"id": 1}, {"id": 2}],
        }
    }
    expected_csv_input = [
        {"creator_id": 10, "comics_id": 1},
        {"creator_id": 10, "comics_id": 2},
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(utils).write_data_to_csv(
            expected_csv_input, "rel_creators_comics"
        ).thenReturn(True):
            try:
                creators_obj.get_relations()
                assert True
            except InvocationError:
                assert False

    if len(Metadata.data["creators"]["rel_comics"]) > 0:
        assert False
