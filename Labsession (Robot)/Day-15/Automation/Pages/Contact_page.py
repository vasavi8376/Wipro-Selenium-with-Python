from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # -------- Locators --------
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    subject = (By.NAME, "subject")
    message = (By.ID, "message")
    upload_file = (By.NAME, "upload_file")
    submit_btn = (By.NAME, "submit")

    success_message = (By.XPATH, "//div[contains(text(),'Success! Your details have been submitted successfully.')]")
    home_btn = (By.XPATH, "//a[contains(text(),'Home')]")

    # -------- Fill Form --------
    def fill_form(self):

        self.wait.until(EC.visibility_of_element_located(self.name)).send_keys("Maneesha")
        self.driver.find_element(*self.email).send_keys("maneesha2004@gmail.com")
        self.driver.find_element(*self.subject).send_keys("Test Subject")
        self.driver.find_element(*self.message).send_keys("This is automation test message")

        # Upload any file (you can change path)
        self.driver.find_element(*self.upload_file).send_keys("C:\\Windows\\notepad.exe")

        self.driver.find_element(*self.submit_btn).click()

        # HANDLE ALERT (IMPORTANT)
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

    # -------- Verify Message --------
    def success_msg(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_message)
        ).is_displayed()