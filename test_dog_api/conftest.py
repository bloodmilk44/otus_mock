import pytest
import requests
import json
import imposters

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


@pytest.fixture
def set_mock(base_api_url):
    if "localhost" in base_api_url:

        # We set imposter to mountebank
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(imposters.update_add_imposter_api_breeds_list_all_200),
            headers={"content-type": "application/json"}
        )
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(imposters.update_add_imposter_api_breeds_list_all_404),
            headers={"content-type": "application/json"}
        )
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(imposters.update_add_imposter_api_breeds_image_random_200),
            headers={"content-type": "application/json"}
        )
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data = json.dumps(imposters.update_add_imposter_api_breeds_image_random_1_200),
            headers = {"content-type": "application/json"}
        )
        requests.request(
            'POST',
            'http://localhost:2525/imposters',
            data=json.dumps(imposters.update_add_imposter_api_breed_hound_list_200),
            headers={"content-type": "application/json"}
        )

        yield

        requests.delete("http://localhost:2525/imposters/4545")
        requests.delete("http://localhost:2525/imposters/4546")
        requests.delete("http://localhost:2525/imposters/4547")
        requests.delete("http://localhost:2525/imposters/4548")
        requests.delete("http://localhost:2525/imposters/4549")
        requests.delete("http://localhost:2525/imposters/4550")
    #else:
    #    try:
    #        return request.config.getoption("--url")
    #    except ValueError:
    #        pass


