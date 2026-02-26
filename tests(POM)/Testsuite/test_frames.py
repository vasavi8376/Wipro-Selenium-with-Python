import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Test_Frames:

    def test_frames(self):
        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)


        # Switch to iframe (there's only 1 iframe on this page)
        frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(frame)

        # Interact with datepicker
        datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()

        time.sleep(2)

        # Close browser
        driver.close()