import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Download folder path
DOWNLOAD_DIR = "C:/Users/vasav/Downloads"

class TestDownload:

    def test_download(self):

        # Launch browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        # Click file to download
        alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        alert.click()
        time.sleep(5)   # wait for download

        # Verify file downloaded
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)

        print("File Download Verified Successfully")

        time.sleep(2)
        driver.close()
