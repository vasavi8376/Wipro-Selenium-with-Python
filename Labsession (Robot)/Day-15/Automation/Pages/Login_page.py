from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_btn = (By.XPATH, "//button[@data-qa='login-button']")

    logged_in_user = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    login_error = (By.XPATH, "//p[contains(text(),'incorrect')]")

    # Now accepts email & password
    def login(self, email, password):
        self.driver.find_element(*self.login_email).clear()
        self.driver.find_element(*self.login_email).send_keys(email)

        self.driver.find_element(*self.login_password).clear()
        self.driver.find_element(*self.login_password).send_keys(password)

        self.driver.find_element(*self.login_btn).click()

    def verify_login_success(self):
        return self.driver.find_element(*self.logged_in_user).is_displayed()

    def verify_login_error(self):
        return self.driver.find_element(*self.login_error).is_displayed()