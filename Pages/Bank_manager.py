import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ManagerPage:

    ADD_CUSTOMER_TAB = (By.XPATH, "//button[@ng-class='btnClass1']")
    OPEN_ACCOUNT_TAB = (By.XPATH, "//button[@ng-class='btnClass2']")

    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    POST_CODE = (By.XPATH, "//input[@placeholder='Post Code']")
    ADD_CUSTOMER_BTN = (By.XPATH, "//button[@type='submit']")

    USER_SELECT = (By.ID, "userSelect")
    CURRENCY_SELECT = (By.ID, "currency")

    def __init__(self, driver):
        self.driver = driver

    def add_customer(self, first, last, post):
        self.driver.find_element(*self.ADD_CUSTOMER_TAB).click()
        time.sleep(2)

        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        time.sleep(1)

        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        time.sleep(1)

        self.driver.find_element(*self.POST_CODE).send_keys(post)
        time.sleep(1)

        self.driver.find_element(*self.ADD_CUSTOMER_BTN).click()
        time.sleep(2)

        self.driver.switch_to.alert.accept()
        time.sleep(2)

    def open_account(self, customer, currency):
        self.driver.find_element(*self.OPEN_ACCOUNT_TAB).click()
        time.sleep(2)

        Select(self.driver.find_element(*self.USER_SELECT)).select_by_visible_text(customer)
        time.sleep(2)

        Select(self.driver.find_element(*self.CURRENCY_SELECT)).select_by_visible_text(currency)
        time.sleep(2)

        self.driver.find_element(*self.ADD_CUSTOMER_BTN).click()
        time.sleep(2)

        self.driver.switch_to.alert.accept()
        time.sleep(2)