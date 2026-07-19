import os

import pytest
from dotenv import load_dotenv
import requests

load_dotenv()


@pytest.fixture(scope="session")
def reqres_headers():
    api_key = os.getenv("REQRES_API_KEY")

    if not api_key:
        pytest.fail("REQRES_API_KEY environment variable missing")

    return {
        "x-api-key": api_key,
        "Accept": "application/json"
    }


def test_get_users(reqres_headers):
    response = requests.get(
        "https://reqres.in/api/users",
        params={"page": 2},
        headers=reqres_headers,
        timeout=10
    )

    response.raise_for_status()

    body = response.json()

    assert "data" in body
    assert isinstance(body["data"], list)
    assert len(body["data"]) > 0
