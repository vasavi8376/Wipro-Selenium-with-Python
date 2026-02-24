*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/hovers

*** Test Cases ***
Verify Mouse Hover
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath://div[@class='example']/div[1]//img    10s

    Mouse Over    xpath://div[@class='example']/div[1]//img
    Sleep    2s

    Element Should Be Visible    xpath://h5[contains(text(),'name: user1')]

    Close Browser