from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    # -------- Locators --------
    all_products_title = (By.XPATH, "//h2[contains(text(),'All Products')]")
    product_list = (By.CLASS_NAME, "features_items")

    search_box = (By.ID, "search_product")
    search_btn = (By.ID, "submit_search")
    searched_products = (By.XPATH, "//h2[contains(text(),'Searched Products')]")

    product_name = (By.XPATH, "//div[@class='product-information']/h2")
    product_category = (By.XPATH, "//p[contains(text(),'Category')]")
    product_price = (By.XPATH, "//span[contains(text(),'Rs')]")
    product_availability = (By.XPATH, "//b[contains(text(),'Availability')]")
    product_condition = (By.XPATH, "//b[contains(text(),'Condition')]")
    product_brand = (By.XPATH, "//b[contains(text(),'Brand')]")

    # -------- Verify Products Page --------
    def verify_products_page(self):
        self.wait.until(EC.visibility_of_element_located(self.all_products_title))
        return self.driver.find_element(*self.product_list).is_displayed()

    # -------- Open First Product (Stable Click) --------
    def open_first_product(self):

        # Scroll to products
        self.driver.execute_script("window.scrollTo(0,700);")

        # Hover on product card
        product_card = self.wait.until(
            lambda d: d.find_elements(By.CLASS_NAME, "product-image-wrapper")[0]
        )

        ActionChains(self.driver).move_to_element(product_card).perform()

        # JS click on View Product
        view_btn = self.driver.find_elements(
            By.XPATH,
            "//a[contains(@href,'product_details')]"
        )[0]

        self.driver.execute_script("arguments[0].click();", view_btn)

    # -------- Verify Product Detail --------
    def verify_product_details(self):
        self.wait.until(EC.visibility_of_element_located(self.product_name))
        return (
            self.driver.find_element(*self.product_name).is_displayed()
            and self.driver.find_element(*self.product_category).is_displayed()
            and self.driver.find_element(*self.product_price).is_displayed()
            and self.driver.find_element(*self.product_availability).is_displayed()
            and self.driver.find_element(*self.product_condition).is_displayed()
            and self.driver.find_element(*self.product_brand).is_displayed()
        )

    # -------- Search Product --------
    def search_product(self, product):
        self.wait.until(EC.visibility_of_element_located(self.search_box)).clear()
        self.driver.find_element(*self.search_box).send_keys(product)
        self.driver.find_element(*self.search_btn).click()

    def search_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.searched_products)
        ).is_displayed()