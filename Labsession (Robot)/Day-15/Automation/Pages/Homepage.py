from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # -------- Navigation Menu --------
    signup_login_btn = (By.XPATH, "//a[@href='/login']")
    products_btn = (By.XPATH, "//a[@href='/products']")
    contact_btn = (By.XPATH, "//a[@href='/contact_us']")
    testcases_btn = (By.XPATH, "//a[@href='/test_cases']")
    logout_btn = (By.XPATH, "//a[@href='/logout']")

    # -------- Validations --------
    home_logo = (By.XPATH, "//img[@alt='Website for automation practice']")
    logged_user = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    # -------- Actions --------

    # verify homepage loaded
    def verify_home_page(self):
        return self.driver.find_element(*self.home_logo).is_displayed()

    # open login/signup page
    def open_login(self):
        self.driver.find_element(*self.signup_login_btn).click()

    # open products page
    def open_products(self):
        self.driver.find_element(*self.products_btn).click()

    # open contact page
    def open_contact(self):
        self.driver.find_element(*self.contact_btn).click()

    # open testcases page
    def open_testcases(self):
        self.driver.find_element(*self.testcases_btn).click()

    # logout user
    def logout(self):
        self.driver.find_element(*self.logout_btn).click()

    # check login success
    def is_logged_in(self):
        return self.driver.find_element(*self.logged_user).is_displayed()