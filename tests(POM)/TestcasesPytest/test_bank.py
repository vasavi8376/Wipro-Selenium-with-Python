import time
from Pages.Bank_login import LoginPage
from Pages.Bank_manager import ManagerPage
from Pages.Bank_customer import CustomerPage

def test_complete_banking_flow(driver):

    home = LoginPage(driver)
    manager = ManagerPage(driver)
    customer = CustomerPage(driver)

    # Open Application
    home.open()
    time.sleep(2)

    # Bank Manager Login
    home.click_bank_manager_login()
    time.sleep(2)

    # Add Customer
    manager.add_customer("Alex", "Smith", "12001")
    time.sleep(2)

    # Open Account
    manager.open_account("Alex Smith", "Dollar")
    time.sleep(2)

    # Customer Login
    home.open()
    home.click_customer_login()
    time.sleep(2)

    customer.login("Alex Smith")
    time.sleep(2)

    # Deposit
    customer.deposit("100")
    time.sleep(2)

    # Withdraw
    customer.withdraw("40")
    time.sleep(2)

    # Validate Balance
    balance = customer.get_balance()
    assert balance == "60"