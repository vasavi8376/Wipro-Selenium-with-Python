from selenium.webdriver.common.by import By

def test_subscription(driver):

    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.ID,"susbscribe_email").send_keys("test@gmail.com")
    driver.find_element(By.ID,"subscribe").click()