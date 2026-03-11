import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from utilities.excel_utilities import get_login_data
from utilities.logger import get_logger


logger = get_logger()
login_data = get_login_data("login_data.xlsx")


test_data = [
    pytest.param(
        username, password, browser, first_name, last_name, address, province, postal_code, browser,
        id=f"{username}-{browser}"
    )
    for username, password, browser, first_name, last_name, address, province, postal_code in login_data
]


class TestCheckoutFlow:

    @pytest.mark.parametrize(
        "username,password,browser,first_name,last_name,address,province,postal_code,driver",
        test_data,
        indirect=["driver"]
    )
    def test_complete_checkout_flow(
        self, driver, username, password, browser, first_name, last_name, address, province, postal_code
    ):
        try:
            logger.info(f"Starting complete checkout flow for {username} on {browser}")

            login = LoginPage(driver)
            product = ProductPage(driver)
            checkout = CheckoutPage(driver)

            assert "bstackdemo" in driver.current_url.lower(), "BStackDemo site did not open properly"

            logger.info("Login started")
            login.login(username, password)

            logger.info("Adding item to cart")
            product.add_item()

            logger.info("Proceeding to checkout")
            product.click_checkout()

            logger.info("Filling shipping details")
            checkout.fill_shipping_details(first_name, last_name, address, province, postal_code)

            logger.info("Downloading invoice")
            checkout.download_invoice_pdf()

            logger.info("Continue shopping")
            checkout.continue_shopping_click()

            logger.info("Logout started")
            login.logout(username)

            assert "bstackdemo" in driver.current_url.lower(), "User is not on BStackDemo site after logout"

            logger.info("Test completed successfully")

        except Exception as e:
            logger.exception(f"Test failed for user {username} on {browser}: {e}")
            raise