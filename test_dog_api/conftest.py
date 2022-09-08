import pytest
import requests
import json
from imposters import update_add_imposter

# Test API: https://dog.ceo/api/breeds
def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://dog.ceo",
        help="This is request url"
    )


@pytest.fixture(scope="session")
def base_api_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="session")
def set_mock(base_api_url):
    if "localhost" in base_api_url:

        # We set imposter to mountebank
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(update_add_imposter),
            headers={"content-type": "application/json"}
        )

        yield

        requests.delete("http://localhost:2525/imposters/8080")

