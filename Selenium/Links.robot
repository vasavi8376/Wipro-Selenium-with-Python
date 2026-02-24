*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com

*** Test Cases ***
Verify link texts
    Open Browser    ${url}    firefox
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

    # get all links
    @{links}=    Get WebElements    xpath://a

    # loop through each link
    FOR    ${link}    IN    @{links}
        ${text}=    Get Text    ${link}
        ${link_url}=    Get Element Attribute    ${link}    href

        Log To Console    ${text}
        Log To Console    ${link_url}
    END

    Close Browser