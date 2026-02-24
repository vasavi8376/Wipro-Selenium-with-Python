*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}            https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}        chrome
${VALID_USER}     Admin
${INVALID_PASS}   wrong123

*** Test Cases ***
TC_02 Verify Error Message On Invalid Login

    [Documentation]    Verify error message when valid username and invalid password are used.

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    20s

    # Step 1: Enter valid username
    Wait Until Element Is Visible    xpath=//input[@name='username']
    Sleep    3s
    Input Text    xpath=//input[@name='username']    ${VALID_USER}
    Sleep    3s

    # Step 2: Enter invalid password
    Input Text    xpath=//input[@name='password']    ${INVALID_PASS}
    Sleep    3s
    # Step 3: Click Login
    Click Button    xpath=//button[@type='submit']
    Sleep    3s

    # Expected Result:
    # Verify exact error message
    Wait Until Element Is Visible    xpath=//p[contains(@class,'oxd-alert-content-text')]
    Element Text Should Be    xpath=//p[contains(@class,'oxd-alert-content-text')]    Invalid credentials

    # Verify user is NOT logged in
    Page Should Not Contain    Dashboard

    Close Browser