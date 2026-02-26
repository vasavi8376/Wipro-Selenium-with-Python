import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_radiobuttons():
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    radio2 = driver.find_element(By.XPATH, "//input[@value='radio2']")
    radio2.click()

    print("Radio2 Selected:", radio2.is_selected())

    checkbox1 = driver.find_element(By.XPATH, "//input[@value='option1']")
    checkbox1.click()

    print("Option1 Selected:", checkbox1.is_selected())

    time.sleep(2)
    driver.quit()