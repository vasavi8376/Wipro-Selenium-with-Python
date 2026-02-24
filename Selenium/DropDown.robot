#selecting by visible text
#selecting by index
#selecting the value

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://rahulshettyacademy.com/AutomationPractice/

*** Test Cases ***
Verify drop downs
    Open Browser               ${url}    firefox
    Maximize Browser Window
    Wait Until Element Is Visible    id=dropdown-class-example

    # Get and log all current labels for verification
    @{labels}=    Get Selected List Labels    id=dropdown-class-example
    Log    ${labels}

    # Method 1: Select by Label (Visible Text)
    Select From List By Label    id=dropdown-class-example    Option3
    Sleep    2s

    # Method 2: Select by Index (starts from 0)
    Select From List By Index    id=dropdown-class-example    2
    Sleep    2s

    # Method 3: Select by Value attribute
    Select From List By Value    id=dropdown-class-example    option1
    Sleep    2s

    Close Browser