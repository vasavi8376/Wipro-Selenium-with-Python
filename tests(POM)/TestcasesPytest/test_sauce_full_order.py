import os
import pytest
from utilities.excel_utils import ExcelReader
from utilities.logger import LogGen
from Pages.Sauce_login_page import LoginPage
from Pages.Sauce_addto_cart_page import InventoryPage
from Pages.Sauce_checkout_page import CheckoutPage


class TestSauceDemo:

    logger = LogGen.loggen()

    @pytest.mark.parametrize("row", [4])
    def test_complete_order_flow(self, driver, row):

        file_path = "C:/Users/vasav/Downloads/LoginData.xlsx"
        sheet_name = "Sheet1"

        excel = ExcelReader(file_path, sheet_name)
        username = excel.get_cell_data(row, 1)
        password = excel.get_cell_data(row, 2)

        self.logger.info("Opening SauceDemo website")
        driver.get("https://www.saucedemo.com/")

        # Login
        login_page = LoginPage(driver)
        login_page.login(username, password)
        self.logger.info("Login successful")

        # Add to cart
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart()
        inventory_page.open_cart()
        self.logger.info("Product added to cart")

        # Checkout
        checkout_page = CheckoutPage(driver)
        checkout_page.checkout()
        checkout_page.enter_details()
        checkout_page.finish_order()

        success_message = checkout_page.get_success_message()
        self.logger.info("Order completed")

        assert "Thank you for your order!" in success_message