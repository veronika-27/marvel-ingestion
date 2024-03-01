import sys
from pathlib import Path
import pytest
import requests
import time
from mockito import when, mock, verify

source_path = Path(__file__).resolve()
base_dir = source_path.parent.parent
src_path = str(base_dir) + "/src"
sys.path.append(src_path)

from marvelapi import MarvelAPI, ApiUnreachableError, ApiServiceError

marvelAPI = MarvelAPI(
    public_key="test",
    private_key="test",
)


def test_fetching_where_get_marvel_data_raises_exception_if_api_is_unreachable():
    print("running")
    code = {"status_code": 502}
    code_to_return_mock = mock(code)

    when(time).sleep(...).thenReturn(0)

    with when(requests).get(...).thenReturn(code_to_return_mock):
        with pytest.raises(ApiUnreachableError):
            marvelAPI.get_marvel_data(endpoint="characters", limit=1)
        verify(requests, times=5).get(...)


def test_fetching_where_get_marvel_data_raises_exception_in_case_of_api_server_error():
    code = {"status_code": 301}
    code_to_return_mock = mock(code)

    when(time).sleep(...).thenReturn(0)

    with when(requests).get(...).thenReturn(code_to_return_mock):
        with pytest.raises(ApiServiceError):
            marvelAPI.get_marvel_data(endpoint="characters", limit=1)
        verify(requests, times=5).get(...)


def test_fetching_where_get_marvel_all_marvel_data_raises_exception_in_case_of_api_server_error():
    code = {"status_code": 301}
    code_to_return_mock = mock(code)

    when(time).sleep(...).thenReturn(0)

    with when(requests).get(...).thenReturn(code_to_return_mock):
        with pytest.raises(ApiServiceError):
            marvelAPI.get_all_marvel_data()(endpoint="characters")
        verify(requests, times=5).get(...)


def test_fetching_where_get_all_marvel_data_raises_exception_if_api_is_unreachable():
    code = {"status_code": 504}
    code_to_return_mock = mock(code)

    when(time).sleep(...).thenReturn(0)

    with when(requests).get(...).thenReturn(code_to_return_mock):
        with pytest.raises(ApiUnreachableError):
            marvelAPI.get_all_marvel_data(endpoint="characters")
        verify(requests, times=5).get(...)


def test_fetching_where_get_marvel_data_returns_expected_json_when_response_status_ok():
    expected_response = {
        "data": {"results": [{"test": "test"}], "total": 190, "count": 100, "offset": 0}
    }
    mocked_response = mock({"status_code": 200, "json": lambda: expected_response})

    when(time).sleep(...).thenReturn(0)

    with when(requests).get(...).thenReturn(mocked_response):
        data_response = marvelAPI.get_all_marvel_data(endpoint="characters")
        assert len(data_response) == 2
