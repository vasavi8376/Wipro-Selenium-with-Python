*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/drag_and_drop
*** Test Cases ***
Verify File Upload
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Sleep    3s
    Wait Until Element Is Visible    xpath://div[@id='column-a']
    Sleep    2s
    Drag And Drop    xpath://div[@id='column-a']    xpath://div[@id='column-b']
    Sleep    2s
    Close Browser