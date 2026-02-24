import pytest


@pytest.fixture(params=["chrome","Edge"])

def browser(request):

        print("Current browser:", request.param)
        return request.param
def test_browser(browser):
    assert browser in ["chrome" , "Edge"]




