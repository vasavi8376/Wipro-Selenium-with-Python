import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    inventory_title = (By.CLASS_NAME, "title")  # appears after login

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username_value, password_value):

        # Wait for username field
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username)
        )
        username_field.clear()
        username_field.send_keys(username_value)

        time.sleep(2)

        # Wait for password field
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.password)
        )
        password_field.clear()
        password_field.send_keys(password_value)

        time.sleep(2)

        # Click login
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.login_btn)
        )
        login_button.click()

        # Wait for next page to load
        self.wait.until(
            EC.visibility_of_element_located(self.inventory_title)
        )

        time.sleep(2)