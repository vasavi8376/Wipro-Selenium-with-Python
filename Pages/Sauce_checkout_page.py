import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    checkout_btn = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")
    overview_title = (By.CLASS_NAME, "title")  # appears in overview page

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def checkout(self):

        # Wait and click checkout
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.checkout_btn)
        )
        checkout_button.click()

        # Wait for first name field to appear (new page loaded)
        self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        )

        time.sleep(2)

    def enter_details(self):

        # Enter first name
        first_name_field = self.wait.until(
            EC.visibility_of_element_located(self.first_name)
        )
        first_name_field.clear()
        first_name_field.send_keys("Rahul")

        time.sleep(1)

        # Enter last name
        last_name_field = self.wait.until(
            EC.visibility_of_element_located(self.last_name)
        )
        last_name_field.clear()
        last_name_field.send_keys("Bommali")

        time.sleep(1)

        # Enter postal code
        postal_field = self.wait.until(
            EC.visibility_of_element_located(self.postal_code)
        )
        postal_field.clear()
        postal_field.send_keys("560001")

        time.sleep(1)

        # Click continue
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.continue_btn)
        )
        continue_button.click()

        # Wait for overview page to load
        self.wait.until(
            EC.visibility_of_element_located(self.overview_title)
        )

        time.sleep(2)

    def finish_order(self):

        # Wait and click finish
        finish_button = self.wait.until(
            EC.element_to_be_clickable(self.finish_btn)
        )
        finish_button.click()

        # Wait for success message
        self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        )

        time.sleep(2)

    def get_success_message(self):

        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).text