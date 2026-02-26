import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class Test_WindowHandling:

    def test_windowhandling(self):
        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        time.sleep(2)
        driver.implicitly_wait(10)
        # click "Click Here" link
        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        # fetch window handles of both tabs
        windows = driver.window_handles
        print(windows)

        # move to child window
        driver.switch_to.window(windows[1])

        # get text from child window
        text = driver.find_element(By.XPATH, "//h3[contains(text(),'New Window')]")
        print(text)

        # close child window
        driver.close()

        # get back to parent window
        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()