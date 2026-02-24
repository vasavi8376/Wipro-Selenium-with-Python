import pytest
import requests


# Q1. Authentication token fixture (runs once per session)
@pytest.fixture(scope="session")
def auth_token():
    print("Auth token generated")
    return "dummy_token_12345"


# Q5. Base URL fixture
@pytest.fixture(scope="session")
def base_url():
    print("Base URL created")
    return "https://jsonplaceholder.typicode.com"


# Q2. Create user before test and delete after test
@pytest.fixture
def user(base_url):
    payload = {
        "name": "pytest_user",
        "email": "pytest@test.com"
    }

    response = requests.post(f"{base_url}/users", json=payload)
    created_user = response.json()

    print("User created")

    yield created_user

    print("User deleted")
