import time
from logging import Logger
import pytest
from Pages.Login_page import LoginPage
from utilities import logger
from utilities.logger import get_logger

test_data = get_excel_data("", "Sheet1")
class TestLogin:
    def test_valid_login(self, driver):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)

        lp = LoginPage(driver)
        lp.login("Admin","admin123")

        time.sleep(2)
        assert "OrangeHRM" in driver.title

        def test_invalid_login(self, driver):
            driver.get("https://opensource-demo.orangehrmlive.com/")
            time.sleep(3)

            lp = LoginPage(driver)
            lp.login("Admin","wrongpassword")

            time.sleep(2)
            assert "Invalid Credentials" in lp.get_error_message()