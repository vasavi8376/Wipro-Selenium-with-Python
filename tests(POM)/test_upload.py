import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_Upload:

    def test_upload(self):

        # Launch browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        # Browse file
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C:/Users/vasav/OneDrive/Desktop/Pictures/Screenshots/Screenshot 2026-02-12 115312.png")
        time.sleep(2)

        # Click upload button
        upload = driver.find_element(By.XPATH, "//input[@id='file-submit']")
        upload.click()
        time.sleep(2)

        # Verify upload success message
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()