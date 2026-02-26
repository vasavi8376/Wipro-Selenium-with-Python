import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    add_to_cart = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_title = (By.CLASS_NAME, "title")  # appears in cart page

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_to_cart(self):

        # Wait until Add to Cart button clickable
        add_button = self.wait.until(
            EC.element_to_be_clickable(self.add_to_cart)
        )
        add_button.click()

        # Wait until cart badge appears (item count = 1)
        self.wait.until(
            EC.visibility_of_element_located(self.cart_badge)
        )

        time.sleep(2)

    def open_cart(self):

        # Wait until cart icon clickable
        cart_button = self.wait.until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        cart_button.click()

        # Wait for cart page to load
        self.wait.until(
            EC.visibility_of_element_located(self.cart_title)
        )

        time.sleep(2)