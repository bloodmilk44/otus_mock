update_add_imposter_api_breeds_list_all_200 = {
    "port": 4545,
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
update_add_imposter_api_breeds_list_all_404 = {
    "port": 4546,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "GET",
                        "path": "/api/breeds/list/all444"
                    }
                }
            ],
            "responses": [
                {
                    "is": {
                        "statusCode": 404,
                        "headers": {"Content-Type": "application/json"},
                        "body": {
                            "status": "error",
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
update_add_imposter_api_breeds_image_random_200 = {
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
update_add_imposter_api_breed_hound_list_200 = {
    "port": 4548,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "GET",
                        "path": "/api/breed/hound/list"
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
update_add_imposter_api_breeds_image_random_1_200 = {
    "port": 4549,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "GET",
                        "path": "/api/breeds/image/random/1"
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