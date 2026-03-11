from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class LoginPage(BasePage):

    sign_in = (By.ID, "signin")
    username_dropdown = (By.ID, "username")
    password_dropdown = (By.ID, "password")
    login_btn = (By.ID, "login-btn")
    logout_btn = (By.XPATH, "//span[text()='Logout']")

    def open_login(self):
        try:
            self.click(self.sign_in)
            self.get_element(self.username_dropdown)
            self.logger.info("Login popup opened successfully")
        except Exception as e:
            self.logger.exception(f"Failed to open login popup: {e}")
            raise

    def login(self, username, password):
        try:
            self.open_login()

            self.click(self.username_dropdown)
            self.click((By.XPATH, f"//div[contains(text(),'{username}')]"))

            self.click(self.password_dropdown)
            self.click((By.XPATH, f"//div[contains(text(),'{password}')]"))

            self.click(self.login_btn)

            username_label = (By.XPATH, f"//span[contains(text(),'{username}')]")
            self.get_element(username_label)

            self.logger.info(f"Login successful for user {username}")

        except Exception as e:
            self.logger.exception(f"Login failed for user {username}: {e}")
            raise
        time.sleep(1)

    def logout(self, username):
        try:
            username_label = (By.XPATH, f"//span[contains(text(),'{username}')]")
            self.click(username_label)
            self.click(self.logout_btn)

            self.get_element(self.sign_in)

            self.logger.info(f"Logout successful for user {username}")

        except Exception as e:
            self.logger.exception(f"Logout failed for user {username}: {e}")
            raise