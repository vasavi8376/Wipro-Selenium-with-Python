*** Settings ***
#setting we add the external library details , resources, set up and tear down

Library   SeleniumLibrary


*** Test Cases ***
#name of the testcase
Verify login with valid credentials
    Log         Enter username
    Log         Enter password
    Log         click on login button
    Log         user is on th home page
Verify add to cart functionality
    Log         User selects the product
    Log         User add the product to the cart
    Log         User verifies that the product with details is added to the cart

*** Keywords ***
    Log         Enter username
    Log         Enter password
    Log         click on login button
    Log         user is on th home page
