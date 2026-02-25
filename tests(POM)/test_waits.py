import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    driver.implicitly_wait(5)  # Implicit wait (global)

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    yield driver
    driver.quit()


# Custom wait function
def element_has_text(locator):
    def _predicate(driver):
        element = driver.find_element(*locator)
        return element if element.text != "" else False
    return _predicate


def test_all_waits(setup):

    driver = setup

    # Click Start button
    driver.find_element(By.TAG_NAME, "button").click()

    # Explicit wait (wait for visibility)
    wait = WebDriverWait(driver, 15)
    element = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    print("Using Explicit Wait:", element.text)

    # Custom wait (wait until text is not empty)
    element2 = wait.until(
        element_has_text((By.ID, "finish"))
    )

    print("Using Custom Wait:", element2.text)

    time.sleep(2)

    assert "Hello World!" in element2.text