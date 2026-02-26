import time
from selenium.webdriver.common.by import By

class LoginPage:

    URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    BANK_MANAGER_LOGIN = (By.XPATH, "//button[text()='Bank Manager Login']")
    CUSTOMER_LOGIN = (By.XPATH, "//button[text()='Customer Login']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)
        time.sleep(2)

    def click_bank_manager_login(self):
        self.driver.find_element(*self.BANK_MANAGER_LOGIN).click()
        time.sleep(2)

    def click_customer_login(self):
        self.driver.find_element(*self.CUSTOMER_LOGIN).click()
        time.sleep(2)