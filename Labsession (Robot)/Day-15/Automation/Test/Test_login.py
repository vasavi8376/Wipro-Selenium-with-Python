from Pages.Homepage import HomePage
from Pages.Login_page import LoginPage

def test_valid_login(driver):

    home = HomePage(driver)
    home.open_login()

    login = LoginPage(driver)
    login.login("maneesha400@gmail.com", "Test@123")

    assert login.verify_login_success()


def test_invalid_login(driver):

    home = HomePage(driver)
    home.open_login()

    login = LoginPage(driver)
    login.login("wrong@gmail.com", "wrong123")

    assert login.verify_login_error()