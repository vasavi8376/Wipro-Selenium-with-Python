from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class CheckoutPage(BasePage):

    first_name = (By.ID, "firstNameInput")
    last_name = (By.ID, "lastNameInput")
    address = (By.ID, "addressLine1Input")
    province = (By.ID, "provinceInput")
    postal_code = (By.ID, "postCodeInput")
    submit_btn = (By.ID, "checkout-shipping-continue")

    download_invoice = (By.XPATH, "//a[contains(text(),'Download')]")
    continue_shopping = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")

    def fill_shipping_details(self, first_name, last_name, address, province, postal_code):
        try:
            self.send_keys(self.first_name, first_name)
            self.send_keys(self.last_name, last_name)
            self.send_keys(self.address, address)
            self.send_keys(self.province, province)
            self.send_keys(self.postal_code, str(postal_code))
            self.click(self.submit_btn)

            self.get_element(self.download_invoice)

            self.logger.info("Shipping details filled successfully")


        except Exception as e:
            self.logger.exception(f"Failed to fill shipping details: {e}")
            raise


    def download_invoice_pdf(self):
        try:
            self.get_element(self.download_invoice)
            self.click(self.download_invoice)

            self.logger.info("Invoice download clicked successfully")

        except Exception as e:
            self.logger.exception(f"Failed to download invoice PDF: {e}")
            raise

    def continue_shopping_click(self):
        try:
            self.get_element(self.continue_shopping)
            self.click(self.continue_shopping)
            self.logger.info("Continue shopping clicked successfully")
        except Exception as e:
            self.logger.exception(f"Failed to click continue shopping: {e}")
            raise