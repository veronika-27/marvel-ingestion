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

from marvel_comics import MarvelComics
from marvelapi import MarvelAPI


def test_get_comics():
    when(time).sleep(...).thenReturn(0)

    comics_obj = MarvelComics(
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
                    "id": 92818,
                    "digitalId": 57424,
                    "title": "Mighty Marvel Holiday Special - Ghost Ridin' to Love Infinity Comic (2022) #1",
                    "issueNumber": 1,
                    "variantDescription": "",
                    "description": "It’s Valentine’s Day in Los Angeles, and hearts aren’t the only thing on fire—Robbie Reyes, AKA Ghost Rider, has a special mission to undertake in his Hell Charger…",
                    "modified": "2022-02-11T13:09:53-0500",
                    "isbn": "",
                    "upc": "75960620060300511",
                    "diamondCode": "",
                    "ean": "",
                    "issn": "",
                    "format": "Digital Vertical Comic",
                    "pageCount": 10,
                    "textObjects": [
                        {
                            "type": "issue_solicit_text",
                            "language": "en-us",
                            "text": "It’s Valentine’s Day in Los Angeles, and hearts aren’t the only thing on fire—Robbie Reyes, AKA Ghost Rider, has a special mission to undertake in his Hell Charger…",
                        }
                    ],
                    "resourceURI": "http://gateway.marvel.com/v1/public/comics/92818",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/issue/92818/mighty_marvel_holiday_special_-_ghost_ridin_to_love_infinity_comic_2022_1?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "reader",
                            "url": "http://marvel.com/digitalcomics/view.htm?iid=57424&utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                    ],
                    "series": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/series/34414",
                        "name": "Mighty Marvel Holiday Special - Ghost Ridin' to Love Infinity Comic (2022)",
                    },
                    "variants": [],
                    "collections": [],
                    "collectedIssues": [],
                    "dates": [
                        {"type": "onsaleDate", "date": "2022-02-14T00:00:00-0500"},
                        {"type": "focDate", "date": "2022-01-17T00:00:00-0500"},
                        {"type": "unlimitedDate", "date": "2022-02-14T00:00:00-0500"},
                    ],
                    "prices": [{"type": "printPrice", "price": 0}],
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/d/90/620690425d675",
                        "extension": "jpg",
                    },
                    "images": [
                        {
                            "path": "http://i.annihil.us/u/prod/marvel/i/mg/d/90/620690425d675",
                            "extension": "jpg",
                        }
                    ],
                    "creators": {
                        "available": 4,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/92818/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/13523",
                                "name": "Annalise Bissa",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/14317",
                                "name": "Alba Glez",
                                "role": "penciler",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/14269",
                                "name": "Jason Loo",
                                "role": "writer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8929",
                                "name": "Lebeau Underwood",
                                "role": "inker",
                            },
                        ],
                        "returned": 4,
                    },
                    "characters": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/92818/characters",
                        "items": [],
                        "returned": 0,
                    },
                    "stories": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/92818/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/206735",
                                "name": "cover from Holidays Vertical Comic (2029) #5",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/206736",
                                "name": "story from Holidays Vertical Comic (2029) #5",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 2,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/92818/events",
                        "items": [],
                        "returned": 0,
                    },
                },
                {
                    "id": 46012,
                    "digitalId": 30993,
                    "title": "Daredevil: Dark Nights (2013) #3",
                    "issueNumber": 3,
                    "variantDescription": "",
                    "description": "<ul><li>Lee Weeks concludes his chapter in this special series of extraordinary creators celebrating the Man Without Fear!</li><li>Everything may stand in his way but nothing will stop Daredevil from rescuing a young life!</li><li>Will Matt Murdock survive the senses-shattering finale to ANGELS UNAWARE?!</li></ul>",
                    "modified": "2022-03-06T15:31:29-0500",
                    "isbn": "",
                    "upc": "75960607856100311",
                    "diamondCode": "JUN130629",
                    "ean": "",
                    "issn": "",
                    "format": "Comic",
                    "pageCount": 32,
                    "textObjects": [
                        {
                            "type": "issue_solicit_text",
                            "language": "en-us",
                            "text": "<ul><li>Lee Weeks concludes his chapter in this special series of extraordinary creators celebrating the Man Without Fear!</li><li>Everything may stand in his way but nothing will stop Daredevil from rescuing a young life!</li><li>Will Matt Murdock survive the senses-shattering finale to ANGELS UNAWARE?!</li></ul>",
                        }
                    ],
                    "resourceURI": "http://gateway.marvel.com/v1/public/comics/46012",
                    "urls": [
                        {
                            "type": "detail",
                            "url": "http://marvel.com/comics/issue/46012/daredevil_dark_nights_2013_3?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "purchase",
                            "url": "http://comicstore.marvel.com/Daredevil-Dark-Nights-3/digital-comic/30993?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "reader",
                            "url": "http://marvel.com/digitalcomics/view.htm?iid=30993&utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                        {
                            "type": "inAppLink",
                            "url": "https://applink.marvel.com/issue/30993?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c",
                        },
                    ],
                    "series": {
                        "resourceURI": "http://gateway.marvel.com/v1/public/series/17354",
                        "name": "Daredevil: Dark Nights (2013 - 2014)",
                    },
                    "variants": [],
                    "collections": [],
                    "collectedIssues": [],
                    "dates": [
                        {"type": "onsaleDate", "date": "2013-08-07T00:00:00-0400"},
                        {"type": "focDate", "date": "2013-07-24T00:00:00-0400"},
                        {"type": "unlimitedDate", "date": "2014-02-03T00:00:00-0500"},
                        {
                            "type": "digitalPurchaseDate",
                            "date": "2013-08-07T00:00:00-0400",
                        },
                    ],
                    "prices": [
                        {"type": "printPrice", "price": 2.99},
                        {"type": "digitalPurchasePrice", "price": 1.99},
                    ],
                    "thumbnail": {
                        "path": "http://i.annihil.us/u/prod/marvel/i/mg/8/f0/62227bfd23a8a",
                        "extension": "jpg",
                    },
                    "images": [
                        {
                            "path": "http://i.annihil.us/u/prod/marvel/i/mg/8/f0/62227bfd23a8a",
                            "extension": "jpg",
                        }
                    ],
                    "creators": {
                        "available": 6,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/46012/creators",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/11647",
                                "name": "Tom Brennan",
                                "role": "editor",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/2490",
                                "name": "Sergio Cariello",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/527",
                                "name": "Tom Palmer",
                                "role": "inker",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/10172",
                                "name": "Vc Clayton Cowles",
                                "role": "letterer",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/593",
                                "name": "Lee Loughridge",
                                "role": "colorist",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/creators/8991",
                                "name": "Lee Weeks",
                                "role": "penciler (cover)",
                            },
                        ],
                        "returned": 6,
                    },
                    "characters": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/46012/characters",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009262",
                                "name": "Daredevil",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/characters/1009470",
                                "name": "Foggy Nelson",
                            },
                        ],
                        "returned": 2,
                    },
                    "stories": {
                        "available": 2,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/46012/stories",
                        "items": [
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/103546",
                                "name": "Daredevil: Dark Knights (2013) #3",
                                "type": "cover",
                            },
                            {
                                "resourceURI": "http://gateway.marvel.com/v1/public/stories/103547",
                                "name": "story from Daredevil: Dark Knights (2013) #3",
                                "type": "interiorStory",
                            },
                        ],
                        "returned": 2,
                    },
                    "events": {
                        "available": 0,
                        "collectionURI": "http://gateway.marvel.com/v1/public/comics/46012/events",
                        "items": [],
                        "returned": 0,
                    },
                },
            ],
        }
    }

    expected_results = [
        {
            "id": 92818,
            "digitalId": 57424,
            "title": "Mighty Marvel Holiday Special - Ghost Ridin' to Love Infinity Comic (2022) #1",
            "issueNumber": 1,
            "variantDescription": "",
            "description": "It’s Valentine’s Day in Los Angeles, and hearts aren’t the only thing on fire—Robbie Reyes, AKA Ghost Rider, has a special mission to undertake in his Hell Charger…",
            "modified": "2022-02-11T13:09:53-0500",
            "modified_ts": 1644602993,
            "isbn": "",
            "upc": "75960620060300511",
            "diamondCode": "",
            "ean": "",
            "issn": "",
            "format": "Digital Vertical Comic",
            "pageCount": 10,
            "textObjects": '[{"type": "issue_solicit_text", "language": "en-us", "text": "It\\u2019s Valentine\\u2019s Day in Los Angeles, and hearts aren\\u2019t the only thing on fire\\u2014Robbie Reyes, AKA Ghost Rider, has a special mission to undertake in his Hell Charger\\u2026"}]',
            "series": '{"resourceURI": "http://gateway.marvel.com/v1/public/series/34414", "name": "Mighty Marvel Holiday Special - Ghost Ridin\' to Love Infinity Comic (2022)"}',
            "resourceURI": "http://gateway.marvel.com/v1/public/comics/92818",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/issue/92818/mighty_marvel_holiday_special_-_ghost_ridin_to_love_infinity_comic_2022_1?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "reader", "url": "http://marvel.com/digitalcomics/view.htm?iid=57424&utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "variants": "[]",
            "collections": "[]",
            "collectedIssues": "[]",
            "dates": '[{"type": "onsaleDate", "date": "2022-02-14T00:00:00-0500"}, {"type": "focDate", "date": "2022-01-17T00:00:00-0500"}, {"type": "unlimitedDate", "date": "2022-02-14T00:00:00-0500"}]',
            "prices": '[{"type": "printPrice", "price": 0}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/d/90/620690425d675", "extension": "jpg"}',
            "images": '[{"path": "http://i.annihil.us/u/prod/marvel/i/mg/d/90/620690425d675", "extension": "jpg"}]',
            "available_creators": 4,
            "available_stories": 2,
            "available_events": 0,
            "available_characters": 0,
        },
        {
            "id": 46012,
            "digitalId": 30993,
            "title": "Daredevil: Dark Nights (2013) #3",
            "issueNumber": 3,
            "variantDescription": "",
            "description": "<ul><li>Lee Weeks concludes his chapter in this special series of extraordinary creators celebrating the Man Without Fear!</li><li>Everything may stand in his way but nothing will stop Daredevil from rescuing a young life!</li><li>Will Matt Murdock survive the senses-shattering finale to ANGELS UNAWARE?!</li></ul>",
            "modified": "2022-03-06T15:31:29-0500",
            "modified_ts": 1646598689,
            "isbn": "",
            "upc": "75960607856100311",
            "diamondCode": "JUN130629",
            "ean": "",
            "issn": "",
            "format": "Comic",
            "pageCount": 32,
            "textObjects": '[{"type": "issue_solicit_text", "language": "en-us", "text": "<ul><li>Lee Weeks concludes his chapter in this special series of extraordinary creators celebrating the Man Without Fear!</li><li>Everything may stand in his way but nothing will stop Daredevil from rescuing a young life!</li><li>Will Matt Murdock survive the senses-shattering finale to ANGELS UNAWARE?!</li></ul>"}]',
            "series": '{"resourceURI": "http://gateway.marvel.com/v1/public/series/17354", "name": "Daredevil: Dark Nights (2013 - 2014)"}',
            "resourceURI": "http://gateway.marvel.com/v1/public/comics/46012",
            "urls": '[{"type": "detail", "url": "http://marvel.com/comics/issue/46012/daredevil_dark_nights_2013_3?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "purchase", "url": "http://comicstore.marvel.com/Daredevil-Dark-Nights-3/digital-comic/30993?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "reader", "url": "http://marvel.com/digitalcomics/view.htm?iid=30993&utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}, {"type": "inAppLink", "url": "https://applink.marvel.com/issue/30993?utm_campaign=apiRef&utm_source=398865f0b1667f0c6db07cf0c1d29c6c"}]',
            "variants": "[]",
            "collections": "[]",
            "collectedIssues": "[]",
            "dates": '[{"type": "onsaleDate", "date": "2013-08-07T00:00:00-0400"}, {"type": "focDate", "date": "2013-07-24T00:00:00-0400"}, {"type": "unlimitedDate", "date": "2014-02-03T00:00:00-0500"}, {"type": "digitalPurchaseDate", "date": "2013-08-07T00:00:00-0400"}]',
            "prices": '[{"type": "printPrice", "price": 2.99}, {"type": "digitalPurchasePrice", "price": 1.99}]',
            "thumbnail": '{"path": "http://i.annihil.us/u/prod/marvel/i/mg/8/f0/62227bfd23a8a", "extension": "jpg"}',
            "images": '[{"path": "http://i.annihil.us/u/prod/marvel/i/mg/8/f0/62227bfd23a8a", "extension": "jpg"}]',
            "available_creators": 6,
            "available_stories": 2,
            "available_events": 0,
            "available_characters": 2,
        },
    ]

    mocked_response = mock({"status_code": 200, "json": lambda: raw_response})
    with when(requests).get(...).thenReturn(mocked_response):
        with when(comics_obj).process_results(
            raw_response.get("data").get("results"), expected_results
        ).thenReturn(True):
            try:
                comics_obj.get_comics()
                assert True
            except InvocationError:
                assert False
