*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}   https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Verify drop downs
    Open Browser   ${url}   chrome
    Maximize Browser Window
    Wait Until Element Is Visible   xpath=(//button)[1]
    Click Element    xpath:(//button)[1]
    #informational alert -acept is for ok button
    Handle Alert   action=ACCEPT   timeout=3
    Sleep    2s
    Click Element    xpath:(//button)[2]
    Handle Alert   action=DISMISS   timeout=3
    Sleep    2s
    Click Element    xpath:(//button)[3]
    Input Text Into Alert    Hello
    Sleep    2s
    Close Browser