import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager



class Test_DragDrop:

    def test_dragdrop(self):
        # Launch Chrome browser
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Open website
        driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        driver.maximize_window()
        time.sleep(2)

        # Create ActionChains object
        actions = ActionChains(driver)

        # Locate source and destination elements
        source = driver.find_element(By.XPATH, "//div[@id='column-a']")
        dest = driver.find_element(By.XPATH, "//div[@id='column-b']")

        # Perform drag and drop
        actions.drag_and_drop(source, dest).perform()

        time.sleep(4)

        # Close browser
        driver.close()