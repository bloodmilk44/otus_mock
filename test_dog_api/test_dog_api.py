import pytest
import requests
import random
from jsonschema import validate


schema_api = {
        "type": "object",
        "properties": {
            "message": {
                "type": "string"
            },
            "status": {
                "type": "string"
            }
        },
        "required": [
            "message",
            "status"
        ]
    }
@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /list/all (получение списка всех
# пород)
def test_dog_api_list_all_breeds(base_api_url, status_code, set_mock):
    if 'localhost' in base_api_url:
        res = requests.get(
            base_api_url + ":4545/api/breeds/list/all"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code
    else:
        res = requests.get(
            base_api_url + "/api/breeds/list/all"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [404])  # Тестирование на код ответа метода /list/all (получение списка всех
# пород)
def test_dog_api_list_all_breeds_negative(base_api_url, status_code, set_mock):
    if 'localhost' in base_api_url:
        res = requests.get(
            base_api_url + ":4546/api/breeds/list/all444"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code
    else:
        res = requests.get(
            base_api_url + "/api/breeds/list/all444"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])
def test_dog_api_image(base_api_url, status_code, set_mock):  # Валидация JSON схемы ответа метода /image/random
    if 'localhost' in base_api_url:
        res = requests.get(
            base_api_url + ":4550/api/breeds/image/random"
        )
        schema = schema_api
        validate(instance=res.json(), schema=schema)
        status_code_get = res.status_code
        assert status_code_get == status_code
    else:
        res = requests.get(
            base_api_url + "/api/breeds/image/random"
        )
        schema = schema_api
        validate(instance=res.json(), schema=schema)
        status_code_get = res.status_code
        assert status_code_get == status_code

@pytest.mark.parametrize('status_code', [200])  # Тестирование запроса разного количества изображений image/random/х
def test_dog_api_ramdom_count_image(base_api_url, status_code, set_mock):
    if 'localhost' in base_api_url:
        res = requests.get(
            base_api_url + ":4549/api/breeds/image/random/1"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code
    else:
        res = requests.get(
            base_api_url + "/api/breeds/image/random/" + str(random.randint(1, 10))
        )
        status_code_get = res.status_code
        assert status_code_get == status_code


@pytest.mark.parametrize('status_code', [200])  # Тестирование на код ответа метода /breed/hound/list (получение
# списка всех метисов породы hound
def test_dog_api_list_all_sub_breeds(base_api_url, status_code, set_mock):
    if 'localhost' in base_api_url:
        res = requests.get(
            base_api_url + ":4548/api/breed/hound/list"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code
    else:
        res = requests.get(
            base_api_url + "/api/breed/hound/list"
        )
        status_code_get = res.status_code
        assert status_code_get == status_code
