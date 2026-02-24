from Pages.Homepage import HomePage
from Pages.Contact_page import ContactPage

def test_contact_form(driver):

    home = HomePage(driver)
    home.open_contact()

    contact = ContactPage(driver)
    contact.fill_form()

    assert contact.success_msg()