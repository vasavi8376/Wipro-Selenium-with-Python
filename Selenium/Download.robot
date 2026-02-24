*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/download

*** Test Cases ***
Verify File Download Link
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//a[normalize-space()='sample-zip-file.zip']
    Click Element    xpath=//a[normalize-space()='sample-zip-file.zip']

    Sleep    5s
    Close Browser