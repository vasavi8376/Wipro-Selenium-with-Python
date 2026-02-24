import pytest


@pytest.fixture(scope="class")
def openbrowser():
    print("\nOpening Browser")
    yield
    print("\nClosing Browser")


@pytest.mark.usefixtures("openbrowser")
class TestLogin:

    def test_login(self):
        print("enter the username")
        print("enter the password")
        print("click on the login button")

    def test_logout(self):
        print("User is logged out")
