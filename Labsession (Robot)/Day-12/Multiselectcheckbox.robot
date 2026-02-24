*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/check-box.php

*** Test Cases ***
Auto Select Multi Level Checkboxes
    Open Browser    ${url}    firefox
    Maximize Browser Window

    # Wait for all checkboxes to load
    Wait Until Element Is Visible    xpath://input[@type='checkbox']

    # Get all checkboxes (main + sub + child)
    ${checkboxes}=    Get WebElements    xpath://input[@type='checkbox']

    # Automatically select all levels
    FOR    ${box}    IN    @{checkboxes}
        Select Checkbox    ${box}
    END

    Sleep    3s
    Close Browser
