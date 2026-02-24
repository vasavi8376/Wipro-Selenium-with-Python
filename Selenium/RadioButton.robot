*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify radio buttons
    Open Browser               ${url}    firefox
    Maximize Browser Window

    # Wait for the specific radio button to load
    Wait Until Element Is Visible    xpath://input[@value = 'radio1']

    # Selecting a Radio Button
    Click Element              xpath://input[@value = 'radio1']

    # Selecting a Checkbox (using ID locator)
    Click Element              id=checkBoxOption3

    Close Browser