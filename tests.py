# -*- coding: utf-8 -*-
""" Sanic camelcase middleware tests module
"""
import json
from humps import camelize
from main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_get_request():
    """test_get_request function tests get requests for middleware
    The purpose of this test is to check if the module would work if the request
    has no payload in case of "GET" requests.
    However the respons should be camilized.
    """
    response = client.get("/user/get")
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "John",
        "lastName": "Doe",
        "age": 30,
    }


def test_request_post_body_snakecased():
    """test_request_post_body_snakecased function tests post request with snake_cased keys.
    The expected return should be camelCased response body
    """
    data = {"first_name": "Ahmed", "last_name": "Okasha", "age": 30}
    response = client.post("/user/create", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "Ahmed",
        "lastName": "Okasha",
        "age": 30,
    }


def test_request_post_body_camelcased():
    """test_request_post_body_camelcased function tests post request with camelCased keys.
    The expected return should be camelCased response body as well
    """
    data = {"firstName": "Ahmed", "lastName": "Okasha", "age": 30}
    response = client.post("/user/create", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "firstName": "Ahmed",
        "lastName": "Okasha",
        "age": 30,
    }
