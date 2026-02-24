*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.saucedemo.com/


*** Test Cases ***
Verify Login Scenario With Valid Credentials
    Open Browser    ${URL}    edge
    Maximize Browser Window

    # wait till page loads
    Wait Until Element Is Visible    xpath://input[@name='user-name']

    # enter username
    Input Text    xpath://input[@name='user-name']    standard_user

    # enter password
    Input Text    xpath://input[@id='password']    secret_sauce

    # click login
    Click Element    xpath://input[@id='login-button']

    # validate home page loaded (Dashboard heading visible)
    Wait Until Element Is Visible    //span[@class='title']
    Element Should Be Visible    xpath://body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='inventory_container']/div/div[@id='inventory_container']/div[@class='inventory_list']/div[1]/div[2]

    Close Browser