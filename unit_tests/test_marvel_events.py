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

from marvel_events import MarvelEvents
from marvelapi import MarvelAPI


def test_get_events():
    when(time).sleep(...).thenReturn(0)

    events_obj = MarvelEvents(
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
                    "id": 296,
                    "title": "Chaos War",
                    "description": "When the Chaos King embarks on a campaign to wipe out all of existence, Hercules gathers the God Squad to stand in his way! Writers Greg Pak and Fred Van Lente join artist Khoi Pham to pit Herc and his rag tag teamâ€”including Thor, the Silver Surfer and Amadeus Choâ€”against an all-powerful evil as dead heroes and villains rise around them!",
                    "resourceURI": "http://gateway.marvel.com/v1/public/events/296",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/events/296/chaos_war?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        }
                    ],
                    "modified": "2013-06-21T11:10:00-0400",
                    "start": "2010-10-01 00:00:00",
                    "end": "2011-03-06 00:00:00",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/5109a003a9112",
                        "extension": "jpg",
                    },
                    "creators": {
                        "available": 57,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/296/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/12401",
                                "name": "Sotocolor",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/598",
                                "name": "Brad Anderson",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/428",
                                "name": "Antonio Fabela",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11579",
                                "name": "Sunny Gho",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4266",
                                "name": "Ian Hannin",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4992",
                                "name": "Simon Bowland",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/5037",
                                "name": "Ed Dukeshire",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/7351",
                                "name": "Henry Fletcher",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/128",
                                "name": "Doug Braithwaite",
                                "role": "artist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/665",
                                "name": "Reilly Brown",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/236",
                                "name": "Tommy Lee Edwards",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13251",
                                "name": "Salva Espin",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/483",
                                "name": "Tom Grummett",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13473",
                                "name": "Brian Ching",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/10288",
                                "name": "Marko Djurdjevic",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/44",
                                "name": "Chris Claremont",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/6986",
                                "name": "J. M. DeMatteis",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13183",
                                "name": "J.M. DeMatteis",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13548",
                                "name": "Danny Miki - Crimelab",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/926",
                                "name": "Cory Hamscher",
                                "role": "inker",
                            },
                        ],
                        "returned": 20,
                    },
                    "characters": {
                        "available": 54,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/296/characters",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009146",
                                "name": "Abomination (Emil Blonsky)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010370",
                                "name": "Alpha Flight",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010784",
                                "name": "Ares",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009163",
                                "name": "Aurora",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009165",
                                "name": "Avengers",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009168",
                                "name": "Banshee",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009175",
                                "name": "Beast",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009189",
                                "name": "Black Widow",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009220",
                                "name": "Captain America",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009224",
                                "name": "Captain Marvel (Mar-Vell)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010719",
                                "name": "Daimon Hellstrom",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009270",
                                "name": "Deathbird",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011037",
                                "name": "Deathcry",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009282",
                                "name": "Doctor Strange",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1012378",
                                "name": "Executioner (Skurge)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009299",
                                "name": "Fantastic Four",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009328",
                                "name": "Grim Reaper",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009330",
                                "name": "Guardian",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009338",
                                "name": "Hawkeye",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011482",
                                "name": "Hela",
                            },
                        ],
                        "returned": 20,
                    },
                    "stories": {
                        "available": 46,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/296/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/71181",
                                "name": "INCREDIBLE HULKS (2009) #618",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/71182",
                                "name": "Interior #71182",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/76014",
                                "name": "Cover From Incredible Hulks (2009) #619",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/76015",
                                "name": "Interior From Incredible Hulks (2009) #619",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/76109",
                                "name": " Interior #76109",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/76687",
                                "name": "Cover #76687",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/76688",
                                "name": "Interior #76688",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80340",
                                "name": "Interior #80340",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80343",
                                "name": "Chaos War (2010) #2",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80344",
                                "name": "Interior #80344",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80345",
                                "name": "Chaos War (2010) #4",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80346",
                                "name": "Interior #80346",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80351",
                                "name": "Chaos War (2010) #3",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80352",
                                "name": "Interior #80352",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80836",
                                "name": "Cover #80836",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80837",
                                "name": "Interior #80837",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80838",
                                "name": "Cover #80838",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/80839",
                                "name": "Interior #80839",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/81176",
                                "name": "CHAOS WAR TPB",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/81177",
                                "name": "CHAOS WAR TPB",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 20,
                    },
                    "comics": {
                        "available": 21,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/296/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36576",
                                "name": "Chaos War (Trade Paperback)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/34517",
                                "name": "Chaos War (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36280",
                                "name": "Chaos War (2010) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/34535",
                                "name": "Chaos War (2010) #3",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/34523",
                                "name": "Chaos War (2010) #4",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36278",
                                "name": "Chaos War (2010) #5",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37067",
                                "name": "Chaos War: Alpha Flight (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37066",
                                "name": "Chaos War: Ares (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37633",
                                "name": "CHAOS WAR: AVENGERS TPB (Trade Paperback)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37068",
                                "name": "Chaos War: Chaos King (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37064",
                                "name": "Chaos War: Dead Avengers (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37085",
                                "name": "Chaos War: Dead Avengers (2010) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37084",
                                "name": "Chaos War: Dead Avengers (2010) #3",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37065",
                                "name": "Chaos War: God Squad (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37062",
                                "name": "Chaos War: Thor (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37060",
                                "name": "Chaos War: Thor (2010) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37881",
                                "name": "Chaos War: X-Men (2010) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/37882",
                                "name": "Chaos War: X-Men (2010) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/31236",
                                "name": "Incredible Hulks (2010) #618",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/34050",
                                "name": "Incredible Hulks (2010) #619",
                            },
                        ],
                        "returned": 20,
                    },
                    "series": {
                        "available": 11,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/296/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/11854",
                                "name": "Chaos War (2010 - 2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/12966",
                                "name": "Chaos War (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13260",
                                "name": "Chaos War: Alpha Flight (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13259",
                                "name": "Chaos War: Ares (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13527",
                                "name": "CHAOS WAR: AVENGERS TPB (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13261",
                                "name": "Chaos War: Chaos King (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13257",
                                "name": "Chaos War: Dead Avengers (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13258",
                                "name": "Chaos War: God Squad (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13253",
                                "name": "Chaos War: Thor (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13588",
                                "name": "Chaos War: X-Men (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/8842",
                                "name": "Incredible Hulks (2010 - 2011)",
                            },
                        ],
                        "returned": 11,
                    },
                    "next": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/events/303",
                        "name": "Age of X",
                    },
                    "previous": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/events/59",
                        "name": "Shadowland",
                    },
                },
                {
                    "id": 302,
                    "title": "Fear Itself",
                    "description": "The Serpent, God of Fear and brother to the Allfather Odin, rises to challenge Earthâ€™s Mightiest in a seven-issue event written by Matt Fraction with art by Stuart Immonen! As the Worthy, heralds of the Serpent, lay waste to the Marvel Universe, how can Thor, Captain America, Iron Man and the Avengers turn back the tide of fear?",
                    "resourceURI": "http://gateway.marvel.com/v1/public/events/302",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/events/302/fear_itself?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "wiki",
                            "url": "http://marvel.com/universe/Fear_Itself?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                    ],
                    "modified": "2013-06-21T11:17:51-0400",
                    "start": "2011-04-16 00:00:00",
                    "end": "2011-10-18 00:00:00",
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/f/03/51099f8823d43",
                        "extension": "jpg",
                    },
                    "creators": {
                        "available": 179,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/302/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/807",
                                "name": "Comicraft",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4992",
                                "name": "Simon Bowland",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/1107",
                                "name": "Dan Abnett",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/24",
                                "name": "Brian Michael Bendis",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11482",
                                "name": "Jesus Aburtov",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/9628",
                                "name": "Ulises Arreola",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13309",
                                "name": "Elizabeth Dismang Breitweiser",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4201",
                                "name": "Bob Almond",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11491",
                                "name": "Michael Babinski",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4014",
                                "name": "Axel Alonso",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8000",
                                "name": "Alejandro Arbona",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8204",
                                "name": "Charlie Beckerman",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/1040",
                                "name": "Jay Anacleto",
                                "role": "penciller (cover)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/648",
                                "name": "Simone Bianchi",
                                "role": "penciller (cover)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/232",
                                "name": "Chris Bachalo",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/4574",
                                "name": "Ryan Bodenheim",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/10087",
                                "name": "Elia Bonetti",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/9371",
                                "name": "Roland Boschi",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/128",
                                "name": "Doug Braithwaite",
                                "role": "penciller",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13215",
                                "name": "Rain Beredo",
                                "role": "artist",
                            },
                        ],
                        "returned": 20,
                    },
                    "characters": {
                        "available": 157,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/302/characters",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009148",
                                "name": "Absorbing Man",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010370",
                                "name": "Alpha Flight",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011227",
                                "name": "Amadeus Cho",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009153",
                                "name": "Angel (Warren Worthington III)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010802",
                                "name": "Ant-Man (Eric O'Grady)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010801",
                                "name": "Ant-Man (Scott Lang)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009159",
                                "name": "Archangel",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011758",
                                "name": "Attuma",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009163",
                                "name": "Aurora",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009165",
                                "name": "Avengers",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011456",
                                "name": "Balder",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011785",
                                "name": "Battlestar",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009175",
                                "name": "Beast",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009187",
                                "name": "Black Panther",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009189",
                                "name": "Black Widow",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011339",
                                "name": "Blue Marvel",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1011236",
                                "name": "Bride of Nine Spiders (Immortal Weapons)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009167",
                                "name": "Bruce Banner",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009220",
                                "name": "Captain America",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1010338",
                                "name": "Captain Marvel (Carol Danvers)",
                            },
                        ],
                        "returned": 20,
                    },
                    "stories": {
                        "available": 189,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/302/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63589",
                                "name": "Avengers (2010) #13",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63590",
                                "name": "Avengers (2010) #13",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63591",
                                "name": "Avengers (2010) #14",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63592",
                                "name": "Interior #63592",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63593",
                                "name": "Avengers (2010) #15",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63594",
                                "name": "Avengers (2010) #15",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63595",
                                "name": "Avengers (2010) #16",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63596",
                                "name": "Avengers (2010) #16",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63597",
                                "name": "Avengers (2010) #17",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/63598",
                                "name": "Avengers (2010) #17",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64682",
                                "name": "HERC 3 (FI)",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64683",
                                "name": "HERC 3 (FI)",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64684",
                                "name": "Hercules (2010) #4",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64685",
                                "name": "Hercules (2010) #4",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64686",
                                "name": "Cover #64686",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64687",
                                "name": "Interior #64687",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64688",
                                "name": "Cover #64688",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64689",
                                "name": "Interior #64689",
                                "type": "interiorStory",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64734",
                                "name": "IRON MAN 2.0 (2011) #5",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/64735",
                                "name": "Iron Man 2.0 (2011) #5",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 20,
                    },
                    "comics": {
                        "available": 89,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/302/comics",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/38570",
                                "name": "Alpha Flight (2011) #1",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/38569",
                                "name": "Alpha Flight (2011) #2",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/38565",
                                "name": "Alpha Flight (2011) #3",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/38567",
                                "name": "Alpha Flight (2011) #4",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/29199",
                                "name": "Avengers (2010) #13",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/29200",
                                "name": "Avengers (2010) #14",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/29201",
                                "name": "Avengers (2010) #15",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/29202",
                                "name": "Avengers (2010) #16",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/29203",
                                "name": "Avengers (2010) #17",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36483",
                                "name": "Avengers Academy (2010) #13",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36478",
                                "name": "Avengers Academy (2010) #14",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36482",
                                "name": "Avengers Academy (2010) #15",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36481",
                                "name": "Avengers Academy (2010) #16",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36480",
                                "name": "Avengers Academy (2010) #17",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36479",
                                "name": "Avengers Academy (2010) #18",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36484",
                                "name": "Avengers Academy (2010) #19",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36785",
                                "name": "Black Panther: The Man Without Fear (2010) #521",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36787",
                                "name": "Black Panther: The Man Without Fear (2010) #522",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/36786",
                                "name": "Black Panther: The Man Without Fear (2010) #523",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/comics/35769",
                                "name": "Captain America (2004) #619",
                            },
                        ],
                        "returned": 20,
                    },
                    "series": {
                        "available": 32,
                        "collectionURI": "http://gateway.marvel.com/v1/public/events/302/series",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13907",
                                "name": "Alpha Flight (2011 - 2012)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/9085",
                                "name": "Avengers (2010 - 2012)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/9086",
                                "name": "Avengers Academy (2010 - 2012)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/15691",
                                "name": "Black Panther: The Man Without Fear (2010 - 2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/832",
                                "name": "Captain America (2004 - 2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13691",
                                "name": "Fear Itself (2010 - 2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14104",
                                "name": "Fear Itself: Black Widow (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14022",
                                "name": "Fear Itself: Fearsome Four (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14800",
                                "name": "Fear Itself: Monkey King (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13858",
                                "name": "Fear Itself: Sin's Past (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14589",
                                "name": "Fear Itself: Spider-Man (2011 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13854",
                                "name": "Fear Itself: Spider-Man (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14059",
                                "name": "Fear Itself: The Deep (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14563",
                                "name": "Fear Itself: The Deep (2011 - Present)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13881",
                                "name": "Fear Itself: The Home Front (2010)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14151",
                                "name": "Fear Itself: Uncanny X-Force (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14065",
                                "name": "Fear Itself: Wolverine (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/13855",
                                "name": "Fear Itself: Youth in Revolt (2011)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/14018",
                                "name": "Ghost Rider (2011 - 2012)",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/series/9898",
                                "name": "Herc (2010 - 2011)",
                            },
                        ],
                        "returned": 20,
                    },
                    "next": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/events/306",
                        "name": "X-Men: Schism",
                    },
                    "previous": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/events/303",
                        "name": "Age of X",
                    },
                },
            ],
        }
    }
    expected_results = [
        {
            "id": 296,
            "title": "Chaos War",
            "description": "When the Chaos King embarks on a campaign to wipe out all of existence, Hercules gathers the God Squad to stand in his way! Writers Greg Pak and Fred Van Lente join artist Khoi Pham to pit Herc and his rag tag teamâ€”including Thor, the Silver Surfer and Amadeus Choâ€”against an all-powerful evil as dead heroes and villains rise around them!",
            "resourceURI": "http://gateway.marvel.com/v1/public/events/296",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/events/296/chaos_war?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "modified": "2013-06-21T11:10:00-0400",
            "modified_ts": 1371827400,
            "start": "2010-10-01 00:00:00",
            "end": "2011-03-06 00:00:00",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/f/20/5109a003a9112", "extension": "jpg"}',
            "available_comics": 21,
            "available_stories": 46,
            "available_series": 11,
            "available_characters": 54,
            "available_creators": 57,
            "next": '{"resourceURI": "http://gateway.marvel.com/v1/public/events/303", "name": "Age of X"}',
            "previous": '{"resourceURI": "http://gateway.marvel.com/v1/public/events/59", "name": "Shadowland"}',
        },
        {
            "id": 302,
            "title": "Fear Itself",
            "description": "The Serpent, God of Fear and brother to the Allfather Odin, rises to challenge Earthâ€™s Mightiest in a seven-issue event written by Matt Fraction with art by Stuart Immonen! As the Worthy, heralds of the Serpent, lay waste to the Marvel Universe, how can Thor, Captain America, Iron Man and the Avengers turn back the tide of fear?",
            "resourceURI": "http://gateway.marvel.com/v1/public/events/302",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/events/302/fear_itself?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "wiki", "url": "http://marvel.com/universe/Fear_Itself?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "modified": "2013-06-21T11:17:51-0400",
            "modified_ts": 1371827871,
            "start": "2011-04-16 00:00:00",
            "end": "2011-10-18 00:00:00",
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/f/03/51099f8823d43", "extension": "jpg"}',
            "available_comics": 89,
            "available_stories": 189,
            "available_series": 32,
            "available_characters": 157,
            "available_creators": 179,
            "next": '{"resourceURI": "http://gateway.marvel.com/v1/public/events/306", "name": "X-Men: Schism"}',
            "previous": '{"resourceURI": "http://gateway.marvel.com/v1/public/events/303", "name": "Age of X"}',
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(events_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            try:
                events_obj.get_events()
                assert True
            except InvocationError:
                assert False
