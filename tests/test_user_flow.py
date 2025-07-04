import pytest
from app.api.v1 import schemas


def test_user_registration_and_login(client):
    user_data = {"email": "test@example.com", "password": "secret", "full_name": "Test User"}
    resp = client.post("/api/v1/users/", json=user_data)
    assert resp.status_code == 201
    user = schemas.User(**resp.json())
    assert user.email == user_data["email"]

    resp = client.post("/api/v1/auth/login", data={"username": user_data["email"], "password": user_data["password"]})
    assert resp.status_code == 200
    token = schemas.Token(**resp.json())
    assert token.access_token
