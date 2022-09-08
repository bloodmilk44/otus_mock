update_add_imposter = {
    "port": 8080,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "POST",
                        "path": "/api/breeds/list/all"
                    }
                }
            ],
            "responses": [
                {
                    "is": {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json"},
                        "body": {
                            "status": "ok",
                            "data": {
                                "name": "test",
                                "surname": "test",
                            }
                        }
                    }
                }
            ]
        }
    ]
}
