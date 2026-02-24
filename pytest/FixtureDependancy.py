import pytest  # <--- This line was missing

@pytest.fixture()
def fixture_a():
    return "Data from A"

@pytest.fixture()
def fixture_b(fixture_a):
    return f"{fixture_a} + Data from B"

def test(fixture_b):
    assert fixture_b == "Data from A + Data from B"