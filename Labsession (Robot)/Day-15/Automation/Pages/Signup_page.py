from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignupPage:

    def __init__(self, driver):
        self.driver = driver

    # First Screen
    name = (By.NAME, "name")
    email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_btn = (By.XPATH, "//button[@data-qa='signup-button']")

    # Account Info
    title = (By.ID, "id_gender1")
    password = (By.ID, "password")
    days = (By.ID, "days")
    months = (By.ID, "months")
    years = (By.ID, "years")

    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    address1 = (By.ID, "address1")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")

    create_account = (By.XPATH, "//button[@data-qa='create-account']")
    account_created = (By.XPATH, "//b[contains(text(),'Account Created')]")

    def start_signup(self):
        self.driver.find_element(*self.name).send_keys("Ramya123")
        self.driver.find_element(*self.email).send_keys("Ramya400@gmail.com")
        self.driver.find_element(*self.signup_btn).click()

    def complete_registration(self):

        self.driver.find_element(*self.title).click()
        self.driver.find_element(*self.password).send_keys("Test@123")

        Select(self.driver.find_element(*self.days)).select_by_value("10")
        Select(self.driver.find_element(*self.months)).select_by_value("5")
        Select(self.driver.find_element(*self.years)).select_by_value("1998")

        self.driver.execute_script("window.scrollBy(0,500)")

        self.driver.find_element(*self.first_name).send_keys("Maneesha")
        self.driver.find_element(*self.last_name).send_keys("User")
        self.driver.find_element(*self.address1).send_keys("Street 1")

        Select(self.driver.find_element(*self.country)).select_by_visible_text("India")

        self.driver.find_element(*self.state).send_keys("Telangana")
        self.driver.find_element(*self.city).send_keys("Hyderabad")
        self.driver.find_element(*self.zipcode).send_keys("500001")
        self.driver.find_element(*self.mobile).send_keys("9876543210")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*self.create_account).click()

    def verify_account_created(self):
        return self.driver.find_element(*self.account_created).is_displayed()