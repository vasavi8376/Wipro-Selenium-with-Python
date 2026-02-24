*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://jqueryui.com/datepicker/

*** Test Cases ***
Verify Date Picker
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    3s

    # Switch to frame (datepicker is inside iframe)
    Select Frame    xpath://iframe[@class='demo-frame']

    # Click date field to open calendar
    Click Element    xpath://input[@id='datepicker']

    Sleep    2s

    # Select date 21
    Click Element    xpath://a[text()='21']

    Sleep    2s
    Close Browser