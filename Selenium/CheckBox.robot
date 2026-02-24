*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Select Only One Checkbox Automatically
    Open Browser    ${url}    firefox
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://input[@type='checkbox']

    # Select only one checkbox (first one)
    Click Element    xpath:(//input[@type='checkbox'])[1]

    Sleep    3s
    Close Browser



