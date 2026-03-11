from utilities.logger import get_logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        try:
            self.logger.info(f"Clicking element {locator}")
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            self.logger.exception(f"Failed to click element {locator}: {e}")
            raise

    def send_keys(self, locator, text):
        try:
            self.logger.info(f"Typing '{text}' into {locator}")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.exception(f"Failed to type '{text}' into {locator}: {e}")
            raise

    def get_element(self, locator):
        try:
            self.logger.info(f"Getting element {locator}")
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            self.logger.exception(f"Failed to get element {locator}: {e}")
            raise