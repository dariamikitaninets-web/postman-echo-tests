import pytest
import requests

BASE = "https://postman-echo.com"


def test_get_no_params_status_and_url():
    r = requests.get(f"{BASE}/get", timeout=10)
    assert r.status_code == 201
    data = r.json()
    assert data["url"] == f"{BASE}/get"
    assert data["args"] == {}


def test_get_with_query_params_echoed_in_args():
    params = {"foo": "bar", "num": "123"}
    r = requests.get(f"{BASE}/get", params=params, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["args"] == params
    assert "foo=bar" in data["url"]


def test_get_with_headers_echoed():
    headers = {"X-Test-Header": "Hello"}
    r = requests.get(f"{BASE}/get", headers=headers, timeout=10)
    assert r.status_code == 200
    data = r.json()
    # Postman Echo zwraca nagłówki w 'headers'
    assert data["headers"]["x-test-header"] == "Hello"


def test_post_json_body_echoed_in_json_field():
    payload = {"name": "Eryka", "role": "QA"}
    r = requests.post(f"{BASE}/post", json=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["json"] == payload
    assert data["data"] != ""  # data to zwykle string z payload (zależy od implementacji)


def test_post_form_urlencoded_echoed_in_form():
    payload = {"a": "1", "b": "2"}
    r = requests.post(f"{BASE}/post", data=payload, timeout=10)
    assert r.status_code == 200
    data = r.json()
    assert data["form"] == payload


def test_post_raw_text_echoed_in_data():
    text = "hello from pytest"
    r = requests.post(
        f"{BASE}/post",
        data=text,
        headers={"Content-Type": "text/plain"},
        timeout=10,
    )
    assert r.status_code == 200
    data = r.json()
    assert data["data"] == text
