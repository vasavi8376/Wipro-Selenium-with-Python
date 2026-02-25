import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestSauceDemoSimple:

    def test_sauce_e2e(self):

        driver = None

        try:
            chrome_options = Options()
            chrome_options.add_argument("--guest")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            driver.maximize_window()
            driver.implicitly_wait(5)

            wait = WebDriverWait(driver, 10)

            # URL
            driver.get("https://www.saucedemo.com/")
            time.sleep(1)

            # Login
            wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
            driver.find_element(By.ID, "password").send_keys("secret_sauce")
            driver.find_element(By.ID, "login-button").click()
            time.sleep(1)

            # Add product
            wait.until(
                EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
            ).click()
            time.sleep(1)

            # Cart
            driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
            time.sleep(1)

            # Checkout
            wait.until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            ).click()
            time.sleep(1)

            driver.find_element(By.ID, "first-name").send_keys("Vasavi")
            driver.find_element(By.ID, "last-name").send_keys("Tester")
            driver.find_element(By.ID, "postal-code").send_keys("523001")
            driver.find_element(By.ID, "continue").click()
            time.sleep(1)

            wait.until(
                EC.element_to_be_clickable((By.ID, "finish"))
            ).click()
            time.sleep(1)

            confirmation = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
            ).text

            assert "Thank you" in confirmation

        except Exception as e:
            print("Test Failed:", e)
            assert False

        finally:
            if driver:
                driver.quit()