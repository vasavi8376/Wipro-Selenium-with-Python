*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}     chrome
${USERNAME}    Admin
${PASSWORD}    admin123

*** Test Cases ***
TC_01 Verify Successful Employee Login

    [Documentation]    Verify Successful ESS Employee Login to OrangeHRM

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Timeout    20s

    # Step 1: Enter Username
    Wait Until Element Is Visible    xpath=//input[@name='username']
    Sleep    3s
    Input Text    xpath=//input[@name='username']    ${USERNAME}
    Sleep    2s

    # Step 2: Enter Password
    Input Text    xpath=//input[@name='password']    ${PASSWORD}
    Sleep    2s

    # Step 3: Click Login Button
    Click Button    xpath=//button[@type='submit']
    Sleep    3s

    # Expected Result: Dashboard is displayed
    Wait Until Page Contains    Dashboard    20s
    Sleep    3s
    Page Should Contain    Dashboard
    Sleep    3s
    # Verify user dropdown visible (confirms login)
    Element Should Be Visible    xpath=//p[@class='oxd-userdropdown-name']

    Close Browser