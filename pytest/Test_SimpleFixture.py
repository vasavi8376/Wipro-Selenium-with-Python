import pytest



#testcase using the simple fixture
def testcase1(simple_data):
    assert simple_data == 46

@pytest.fixture()
def api_url():
    return "https://api.example.com"

def test_api(api_url):
    assert "https" in api_url



