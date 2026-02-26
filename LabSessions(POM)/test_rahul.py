import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def setup():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")
    yield driver
    driver.quit()


def test_full_automation(setup):

    driver = setup
    wait = WebDriverWait(driver, 15)
    actions = ActionChains(driver)

    # -------- Suggestion Class --------
    driver.find_element(By.ID, "autocomplete").send_keys("ind")
    suggestions = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "li.ui-menu-item div"))
    )

    for option in suggestions:
        if option.text == "India":
            option.click()
            break

    time.sleep(2)  # Pause to see selection
    print("India selected successfully")

    # -------- Switch Window --------
    parent = driver.current_window_handle
    driver.find_element(By.ID, "openwindow").click()
    wait.until(EC.number_of_windows_to_be(2))

    for window in driver.window_handles:
        if window != parent:
            driver.switch_to.window(window)
            break

    time.sleep(2)
    print("New Window Loaded Successfully")

    driver.close()
    driver.switch_to.window(parent)
    time.sleep(1)

    # -------- Switch Tab --------
    driver.find_element(By.ID, "opentab").click()
    wait.until(EC.number_of_windows_to_be(2))

    tabs = driver.window_handles
    driver.switch_to.window(tabs[-1])

    time.sleep(2)
    print("New Tab Loaded Successfully")

    driver.close()
    driver.switch_to.window(parent)
    time.sleep(1)

    # -------- Alert --------
    driver.find_element(By.ID, "name").send_keys("Surya")
    driver.find_element(By.ID, "alertbtn").click()

    alert = wait.until(EC.alert_is_present())
    print("Alert Text:", alert.text)
    time.sleep(2)
    alert.accept()

    # -------- Web Table --------
    rows = driver.find_elements(By.XPATH, "//table[@name='courses']//tr")

    for row in rows:
        if "Advanced Selenium Framework Pageobject, TestNG, Maven, Jenkins,C" in row.text:
            print("Course Found:", row.text)

    time.sleep(2)

    # -------- Fixed Header Table --------
    chennai = driver.find_element(
        By.XPATH, "//div[@class='tableFixHead']//td[text()='Chennai']"
    ).text

    print("Fixed Header City:", chennai)
    time.sleep(2)

    # -------- Mouse Hover --------
    mouse_hover = driver.find_element(By.ID, "mousehover")
    actions.move_to_element(mouse_hover).perform()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Top").click()
    time.sleep(2)

    assert "AutomationPractice" in driver.current_url
    print("Mouse hover Top validated")

    # -------- iFrame --------
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "courses-iframe")))
    time.sleep(2)

    home_text = driver.find_element(By.XPATH, "//a[text()='Home']").text
    print("iFrame Home Text:", home_text)

    assert "Home" in home_text
    driver.switch_to.default_content()

    print("All scenarios executed successfully")