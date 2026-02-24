from Pages.Homepage import HomePage
from Pages.Products_page import ProductPage

def test_products_page(driver):

    home = HomePage(driver)
    home.open_products()

    product = ProductPage(driver)
    assert product.verify_products_page()


def test_view_product_details(driver):

    home = HomePage(driver)
    home.open_products()

    product = ProductPage(driver)
    product.open_first_product()

    assert product.verify_product_details()


def test_search_product(driver):

    home = HomePage(driver)
    home.open_products()

    product = ProductPage(driver)
    product.search_product("dress")

    assert product.search_visible()