import requests
import json

"""
Актуальная команда для запуска (прописать нужные порты):
docker run -p 2525:2525 -p 8080:8080 -p 8081:8081 bbyars/mountebank start
"""

# точки с валидными координатами
valid_points = {
    "all": "good"
}

# формируем конфигурацию imposter'a
imposter_cfg = {
    "port": 8080,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "GET",
                        "path": "/api/breeds/list/all"
                    }
                }
            ],
            "responses": [
                {
                    "is": {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json"},
                        "body": valid_points
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
