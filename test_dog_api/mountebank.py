import requests
import json

"""
Актуальная команда для запуска (прописать нужные порты):
docker run --rm -p 2525:2525 -p 4545:4545 -p 4546:4546 -p 4547:45477 -p 4548:4548 -p 4549:4549 bbyars/mountebank:2.7.0 mb start
"""

# точки с валидными координатами
valid_points = {
    "all": "good"
}

# формируем конфигурацию imposter'a
imposter_cfg = {
    "port": 4550,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "GET",
                        "path": "/api/breeds/image/random"
                    }
                }
            ],
            "responses": [
                {
                    "is": {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json"},
                        "body": {
                            "message": "string",
                            "status": "string"
                        }
                    }
                }
            ]
        }
    ]
}

# отправляем в mountebank запрос на создание imposter'a
r = requests.request(
    'POST',
    'http://localhost:2525/imposters',
    data=json.dumps(imposter_cfg),
    headers={"content-type": "application/json"}
)

print("Mountebank response: ", r.text)
