import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# create a fixture for Invoice chrome browser and close the chrome browser

@pytest.fixture(scope = "class")
def driver(request):
    service = Service(ChromeDriverManager().install())
    # driver instance is created to use web driver globally in the test script
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")

    request.cls.driver = driver
    yield
    driver.quit()