import pytest


@pytest.fixture(scope="module")
def browser_module():
    print("\n[MODULE] Open browser for module")
    yield
    print("\n[MODULE] Close browser for module")



@pytest.mark.usefixtures("browser_module")
def test_login():
    print("Login: enter username, enter password, click login")


@pytest.mark.usefixtures("browser_module")
def test_logout():
    print("Logout: user is logged out")


@pytest.mark.usefixtures("browser_module")
def test_another_action():
    print("Performing another action in the same module")

    @pytest.fixture(scope="module")
    def setupapi():
        print("Authorize apis with username and password")  # setup
        yield
        print("Unauthorize apis with username and password")  # tear do
