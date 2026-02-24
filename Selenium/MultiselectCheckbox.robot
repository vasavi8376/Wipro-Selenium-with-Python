*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify multiselect check boxes
    Open Browser               ${url}    firefox
    Maximize Browser Window

    # Identify all common elements by attribute
    ${elements}=    Get WebElements    xpath://input[@type = 'checkbox']

    # Loop to click every checkbox found
    FOR    ${element}    IN    @{elements}
        Click Element    ${element}
        Sleep    2s
    END

    Close Browser