from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class ProductPage(BasePage):

    add_product = (By.CSS_SELECTOR, ".shelf-item__buy-btn")
    checkout_btn = (By.XPATH, "//div[@class='buy-btn']")

    def add_item(self):
        try:
            buttons = self.driver.find_elements(*self.add_product)

            if not buttons:
                raise Exception("No products found on the page")

            buttons[0].click()
            self.logger.info("First product added to cart successfully")

        except Exception as e:
            self.logger.exception(f"Failed to add item to cart: {e}")
            raise
        time.sleep(1)

    def click_checkout(self):
        try:
            checkout = self.get_element(self.checkout_btn)

            self.driver.execute_script("arguments[0].click();", checkout)
            self.logger.info("Checkout button clicked successfully")

        except Exception as e:
            self.logger.exception(f"Failed to click checkout button: {e}")
            raise