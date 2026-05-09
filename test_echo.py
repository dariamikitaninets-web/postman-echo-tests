

import pytest
import requests
import allure


BASE = "https://postman-echo.com"




@allure.title("GET /get without params returns 200 and empty args")
@allure.description(
    "Sends GET request to /get without query parameters and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'url' equals the endpoint URL\n"
    "- response 'args' is an empty object"
)
def test_get_no_params_status_and_url():
    with allure.step("Send GET request to /get without query params"):
        r = requests.get(f"{BASE}/get", timeout=10)


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify response 'url' equals expected URL"):
        assert data["url"] == f"{BASE}/get"


    with allure.step("Verify response 'args' is empty"):
        assert data["args"] == {}




@allure.title("GET /get echoes query parameters in args")
@allure.description(
    "Sends GET request to /get with query parameters and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'args' equals sent params\n"
    "- response 'url' contains expected query string fragment"
)
def test_get_with_query_params_echoed_in_args():
    params = {"foo": "bar", "num": "123"}


    with allure.step(f"Prepare query params: {params}"):
        pass


    with allure.step("Send GET request to /get with query params"):
        r = requests.get(f"{BASE}/get", params=params, timeout=10)


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify response 'args' matches sent params"):
        assert data["args"] == params


    with allure.step("Verify response 'url' contains 'foo=bar'"):
        assert "foo=bar" in data["url"]




@allure.title("GET /get echoes custom headers in response headers")
@allure.description(
    "Sends GET request to /get with a custom header and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'headers' contains the header value (lower-cased key in Postman Echo)"
)
def test_get_with_headers_echoed():
    headers = {"X-Test-Header": "Hello"}


    with allure.step(f"Prepare request headers: {headers}"):
        pass


    with allure.step("Send GET request to /get with custom header"):
        r = requests.get(f"{BASE}/get", headers=headers, timeout=10)


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify custom header is echoed back in response headers"):
        # Postman Echo returns headers under 'headers' with lower-cased keys
        assert data["headers"]["x-test-header"] == "Hello"




@allure.title("POST /post echoes JSON body in 'json' field")
@allure.description(
    "Sends POST request to /post with JSON body and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'json' equals sent payload\n"
    "- response 'data' is not empty (usually string representation of payload)"
)
def test_post_json_body_echoed_in_json_field():
    payload = {"name": "Eryka", "role": "QA"}


    with allure.step(f"Prepare JSON payload: {payload}"):
        pass


    with allure.step("Send POST request to /post with JSON payload"):
        r = requests.post(f"{BASE}/post", json=payload, timeout=10)


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify response 'json' equals sent payload"):
        assert data["json"] == payload


    with allure.step("Verify response 'data' is not empty"):
        assert data["data"] != ""




@allure.title("POST /post echoes form-urlencoded body in 'form' field")
@allure.description(
    "Sends POST request to /post with form-urlencoded body and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'form' equals sent payload"
)
def test_post_form_urlencoded_echoed_in_form():
    payload = {"a": "1", "b": "2"}


    with allure.step(f"Prepare form payload: {payload}"):
        pass


    with allure.step("Send POST request to /post with form-urlencoded payload"):
        r = requests.post(f"{BASE}/post", data=payload, timeout=10)


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify response 'form' equals sent payload"):
        assert data["form"] == payload




@allure.title("POST /post echoes raw text in 'data' field")
@allure.description(
    "Sends POST request to /post with raw text body and verifies:\n"
    "- HTTP status code is 200\n"
    "- response 'data' equals sent text"
)
def test_post_raw_text_echoed_in_data():
    text = "hello from pytest"


    with allure.step(f"Prepare raw text payload: '{text}'"):
        pass


    with allure.step("Send POST request to /post with raw text and Content-Type text/plain"):
        r = requests.post(
            f"{BASE}/post",
            data=text,
            headers={"Content-Type": "text/plain"},
            timeout=10,
        )


    with allure.step("Verify HTTP status code is 200"):
        assert r.status_code == 200


    with allure.step("Parse response JSON"):
        data = r.json()


    with allure.step("Verify response 'data' equals sent text"):
        assert data["data"] == text
