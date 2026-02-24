*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.amazon.in/

*** Test Cases ***
Verify Scroll On Amazon
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Page Contains    Amazon    15s

    Sleep    2s

    # Scroll down little
    Execute Javascript    window.scrollBy(0,500)
    Sleep    2s

    # Scroll to bottom
    Execute Javascript    window.scrollTo(0, document.body.scrollHeight)
    Sleep    3s

    # Scroll back to top
    Execute Javascript    window.scrollTo(0,0)
    Sleep    2s

    Close Browser