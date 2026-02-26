import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.devtools.v143.browser import BrowserContextID
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
class Test_Webtable:
    def test_webtable(self):

        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.maximize_window()
        driver.implicitly_wait(10)
        time.sleep(2)
        # Fetch number of rows
        rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")

        for i in rows:
            print(i.text)

        # Fetch number of columns (cells in first row)
        cols = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr[1]/td")

        for i in cols:
            print(i.text)

        # Fetch specific cell data (3rd row, 4th column)
        cell_data = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[4]")

        assert "$100.00" in cell_data.text

        # Close browser
        driver.quit()