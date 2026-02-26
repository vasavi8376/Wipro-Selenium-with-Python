import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CustomerPage:

    USER_SELECT = (By.ID, "userSelect")
    LOGIN_BTN = (By.XPATH, "//button[text()='Login']")
    DEPOSIT_TAB = (By.XPATH, "//button[normalize-space()='Deposit']")
    WITHDRAW_TAB = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    BALANCE = (By.XPATH, "//strong[2]")

    def __init__(self, driver):
        self.driver = driver

    def login(self, customer):
        Select(self.driver.find_element(*self.USER_SELECT)).select_by_visible_text(customer)
        time.sleep(2)

        self.driver.find_element(*self.LOGIN_BTN).click()
        time.sleep(2)

    def deposit(self, amount):
        self.driver.find_element(*self.DEPOSIT_TAB).click()
        time.sleep(2)

        self.driver.find_element(*self.AMOUNT_FIELD).send_keys(amount)
        time.sleep(2)

        self.driver.find_element(*self.SUBMIT_BTN).click()
        time.sleep(2)

    def withdraw(self, amount):
        self.driver.find_element(*self.WITHDRAW_TAB).click()
        time.sleep(2)

        self.driver.find_element(*self.AMOUNT_FIELD).send_keys(amount)
        time.sleep(2)

        self.driver.find_element(*self.SUBMIT_BTN).click()
        time.sleep(2)

    def get_balance(self):
        time.sleep(2)
        return self.driver.find_element(*self.BALANCE).text