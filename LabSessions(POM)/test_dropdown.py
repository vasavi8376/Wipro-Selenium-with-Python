import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_dropdown():

    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.get("https://trytestingthis.netlify.app")
    time.sleep(2)

    # First dropdown (single select)
    Select(driver.find_element(By.ID, "option")).select_by_visible_text("Option 2")
    time.sleep(2)

    # Second dropdown (multiple select)
    multi = Select(driver.find_element(By.ID, "owc"))
    multi.select_by_visible_text("Option 1")
    multi.select_by_visible_text("Option 3")
    time.sleep(2)

    driver.quit()