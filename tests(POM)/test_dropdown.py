import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    time.sleep(2)
    yield driver
    driver.quit()


def test_dropdown_selection(setup):
    driver = setup

    # Locate dropdown
    dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))

    # Select by Visible Text
    dropdown.select_by_visible_text("Option1")
    print("Selected Option1 using visible text")
    time.sleep(2)

    # Select by Value
    dropdown.select_by_value("option2")
    print("Selected Option2 using value")
    time.sleep(2)

    # Select by Index
    dropdown.select_by_index(3)
    print("Selected Option3 using index")
    time.sleep(2)