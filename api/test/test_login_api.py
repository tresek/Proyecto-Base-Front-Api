import requests
import pytest

API_URL = "https://petstore.swagger.io/v2/pet/1"  # ← cambia a la URL real si es distinta

@pytest.mark.api
def test_login_exitoso():
    payload = {
        "email": "solyner28@yopmail.com",
        "password": "123456"  # ← usa una válida si tienes
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "token" in data
    assert data["user"]["email"] == payload["email"]

@pytest.mark.api
def test_login_contraseña_incorrecta():
    payload = {
        "email": "solyner28@yopmail.com",
        "password": "incorrecta"
    }

    response = requests.post(API_URL, json=payload)

    assert response.status_code == 401
    assert "error" in response.json() or "message" in response.json()
