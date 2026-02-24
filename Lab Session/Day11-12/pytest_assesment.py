import pytest
import requests


# Q3. Validate JSON response schema
def test_json_schema_validation(base_url):
    response = requests.get(f"{base_url}/users/1")
    data = response.json()

    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)


# Q4. Parametrized status code validation
@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_status_codes(status_code):
    response = requests.get(f"https://httpbin.org/status/{status_code}")
    assert response.status_code == status_code


# Q5. Fixture chain test
def test_fixture_chain(base_url, auth_token, user):
    assert user is not None
