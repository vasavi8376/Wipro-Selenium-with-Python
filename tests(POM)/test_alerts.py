import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Alerts:   # ✅ Should be class

    def test_alerts(self):   # ✅ Proper indentation

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        time.sleep(2)

        # -----------------------
        # Simple Alert
        # -----------------------
        simplealt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        simplealt.click()

        alt = driver.switch_to.alert
        alt.accept()

        # -----------------------
        # Confirmation Alert
        # -----------------------
        confalt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalt.click()

        alt = driver.switch_to.alert
        alt.dismiss()

        # -----------------------
        # Prompt Alert
        # -----------------------
        promptalt = driver.find_element(
            By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()

        alt = driver.switch_to.alert
        print("Alert Text:", alt.text)

        alt.send_keys("test hello")
        alt.accept()

        time.sleep(2)
        driver.quit()