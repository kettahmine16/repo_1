import requests
import pytest

BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = ""
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


# POST
@pytest.mark.positive
def test_create_project_post():
    payload = {
        "title": "ГосУслуги",
        "users": {
            "356dd37d-b48b-4c65-a431-16bc92c60027": "admin"
        }
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]


@pytest.mark.negative
def test_create_project_post_invalid():
    # Невалидный user id

    payload = {
        "title": "ГосУслуги",
        "users": {
            "356dd37d-b48b-4c65-16bc92c60027": "admin"
        }
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 400, r.text


# PUT
@pytest.mark.positive
def test_edit_project_id():
    ID = "c67453f1-f485-4c51-841c-25af0b011200"

    payload = {
        "title": "Новое название"
    }

    r = requests.put(f"{BASE_URL}/projects/{ID}",
                     json=payload,
                     headers=HEADERS,
                     )
    assert r.status_code == 200, r.text


@pytest.mark.negative
def test_edit_project_invalid_id():
    ID = "c67453f1-f485-4c51-647c-25af0b011200"

    payload = {
        "title": "Новое название"
    }

    r = requests.put(f"{BASE_URL}/projects/{ID}",
                     json=payload,
                     headers=HEADERS,
                     )
    assert r.status_code == 404, r.text


# GET
@pytest.mark.positive
def test_get_progect_id():
    ID = "c67453f1-f485-4c51-841c-25af0b011200"

    payload = {
        "title": "ГосУслуги",
        "timestamp": 1763729779300,
        "id": "c67453f1-f485-4c51-841c-25af0b011200"
    }

    r = requests.get(f"{BASE_URL}/projects/{ID}",
                     json=payload,
                     headers=HEADERS,
                     )

    assert r.status_code == 200, r.text


@pytest.mark.negative
def test_get_progect_id_invalid():
    # Поиск по невалидному id
    ID = "f6be3f5d-1f33-4c83-a43d-300c160e154e"

    payload = {
        "title": "ГосУслуги",
        "timestamp": 1763735363927,
        "users": {
                "356dd37d-b48b-4c65-a431-16bc92c60027": "admin"
            },
        "id": "f6be3f5d-1f33-4c83-a44b-300c160e154e"
    }

    r = requests.get(f"{BASE_URL}/projects/{ID}",
                     json=payload,
                     headers=HEADERS,
                     )

    assert r.status_code == 404, r.text
