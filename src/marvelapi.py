import datetime
import hashlib
import requests
from datetime import datetime
import time


class ApiUnreachableError(RuntimeError):
    pass


class ApiServiceError(RuntimeError):
    pass


class MarvelAPI:
    """
    A class to represent a Marvel API
    ...

    Attributes
    ----------
    public_key (str): the public key  needed to establish an API connection
    private_key (str): the private key provided by Marvel API to establish the API connection

    Methods
    -------
    generate_hash (self): generates the data needed to establish the API connection in the expected format
    get_marvel_data (self, url, endpoint, limit, offset, modifiedSince): returns dictionary with the generic data
    of specific endpoint according the provided limits and offset"""

    def __init__(self, public_key, private_key):
        """
        Constructs the necessary properties for the MarvelData object creation.
            :params:
            public_key (str): the public key  needed to establish an API connection
            private_key (str): the private key provided by Marvel API to establish the API connection
        """
        self.root_url = "https://gateway.marvel.com:443/v1/public/"
        self.public_key = public_key
        self.private_key = private_key

    def generate_hash(self) -> dict:
        """
        Generates the expected format of the parameters needed for server-side applications authentication needed for
        successful API connection.

        :return: dictionary that contains all the parameters needed (in MD5 hash) for the API connection"""

        params = {}
        ts = str(int(time.time()))
        auth_hash = hashlib.md5()
        auth_hash.update(ts.encode("utf-8"))
        auth_hash.update(self.private_key.encode("utf-8"))
        auth_hash.update(self.public_key.encode("utf-8"))

        params["hash"] = auth_hash.hexdigest()
        params["apikey"] = self.public_key
        params["ts"] = ts

        return params

    def get_marvel_data(
        self,
        endpoint: str,
        url: str = "",
        limit: int = 100,
        offset: int = 0,
        modifiedSince: int = 0,
    ) -> dict:
        """
        Returns dictionary with maximum general data permitted for specific Marvel endpoint/ url or according provided
        limit and offset
        :param:
            endpoint (str): specifies the API endpoint (with specific entity data) to be used in case of missing url
            url (str): specifies the API url to be used
            limit (int): Specifies the maximum data to be extracted, default:100
            offset (int): specifies the offset, default:0
            modifiedSince (int): unix timestamp

        :return: dictionary containing the data from specific Marvel endpoint or from the url
        """
        params = self.generate_hash()
        params["orderBy"] = "modified"
        params["limit"] = limit
        params["offset"] = offset

        # due to buggy API - if we set 0000-00-00 we get less results (total) for initial data
        if modifiedSince > 0:
            params["modifiedSince"] = datetime.utcfromtimestamp(modifiedSince).strftime(
                "%Y-%m-%d"
            )

        if url == "":
            url = "{root_url}{endpoint}".format(
                root_url=self.root_url, endpoint=endpoint
            )

        for retry in range(5):
            try:
                response = requests.get(url=url, params=params, timeout=120)
                if 200 <= response.status_code < 300:
                    break
                else:
                    time.sleep(5)
                    continue
            except:
                time.sleep(5)
                continue

        if response.status_code in [502, 503, 504]:
            raise ApiUnreachableError(response.reason)

        if response.status_code > 299:
            raise ApiServiceError(response.reason)

        marvel_data_json = response.json()
        return marvel_data_json

    def get_all_marvel_data(
        self,
        endpoint: str = "",
        url: str = "",
        offset: int = 0,
        modifiedSince: int = 0,
    ) -> list:
        """
        Loops trough and list all the data results of specific url (method that will be used to exhaust all the relations per id)
        :param:
            endpoint (str): specifies the API endpoint (with specific entity data) to be used in case of missing url
            url (str): specifies the API url to be used (in order to get the relations)
            offset (int): specifies the offset, default:0
            modifiedSince (int): unix timestamp

        :return:
            all_results (list): list of dictionaries with all the data results of specific Marvel endpoint/url
        """

        resp = self.get_marvel_data(
            endpoint=endpoint, url=url, offset=offset, modifiedSince=modifiedSince
        )

        raw_results = resp.get("data").get("results")
        all_results = raw_results
        total = resp.get("data").get("total")
        processed_items = resp.get("data").get("count")
        offset = resp.get("data").get("offset") + 100
        while processed_items < total and len(raw_results) > 0:
            resp = self.get_marvel_data(
                endpoint=endpoint, url=url, offset=offset, modifiedSince=modifiedSince
            )

            total = resp.get("data").get("total")
            offset = resp.get("data").get("offset") + 100
            processed_items += resp.get("data").get("count")
            raw_results = resp.get("data").get("results")
            all_results.extend(raw_results)

        return all_results
