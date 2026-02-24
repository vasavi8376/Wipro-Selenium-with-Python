*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}          https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${BROWSER}      chrome
${USERNAME}     Admin
${PASSWORD}     admin123
${NEW_NAME}     Vasavi Katragadda

*** Test Cases ***
TC_03 Modify First Name In Personal Details

    Open Browser    ${URL}    ${BROWSER}
    Sleep    3s
    Maximize Browser Window
    Sleep    3s

    Wait Until Element Is Visible    xpath=//input[@name='username']
    Input Text    xpath=//input[@name='username']    ${USERNAME}
    Sleep    2s
    Input Text    xpath=//input[@name='password']    ${PASSWORD}
    Sleep    2s
    Click Button    xpath=//button[@type='submit']
    Sleep    5s

    Click Element    xpath=//span[text()='My Info']
    Sleep    5s

    # React-safe clear and set
    Execute JavaScript
    ...    var input = document.getElementsByName('firstName')[0];
    ...    input.value = '';
    ...    input.dispatchEvent(new Event('input', { bubbles: true }));
    ...    input.value = '${NEW_NAME}';
    ...    input.dispatchEvent(new Event('input', { bubbles: true }));
    Sleep    3s

    Scroll Element Into View    xpath=(//button[@type='submit'])[1]
    Sleep    2s

    Click Button    xpath=(//button[@type='submit'])[1]
    Sleep    5s

    Element Attribute Value Should Be
    ...    xpath=//input[@name='firstName']
    ...    value
    ...    ${NEW_NAME}
    Sleep    3s

    Close Browser