import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestRahulSimple:

    def test_rahul_e2e(self):

        driver = None

        try:
            chrome_options = Options()
            chrome_options.add_argument("--guest")

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            driver.maximize_window()
            driver.implicitly_wait(5)

            wait = WebDriverWait(driver, 10)

            driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
            time.sleep(1)

            products = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//button[text()='ADD TO CART']")
                )
            )

            for i in range(3):
                products[i].click()
                time.sleep(1)

            driver.find_element(By.CLASS_NAME, "cart-icon").click()
            time.sleep(1)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
                )
            ).click()
            time.sleep(1)

            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[text()='Place Order']")
                )
            ).click()
            time.sleep(1)

            Select(
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "select")))
            ).select_by_visible_text("India")
            time.sleep(1)

            driver.find_element(By.CLASS_NAME, "chkAgree").click()
            time.sleep(1)

            driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
            time.sleep(2)

            assert "Thank you" in driver.page_source

        except Exception as e:
            print("Test Failed:", e)
            assert False

        finally:
            if driver:
                driver.quit()