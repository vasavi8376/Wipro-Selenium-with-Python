*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    # maximize the browser window
    Maximize Browser Window
    # wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']

    # capture page screenshot
    Capture Page Screenshot    C:/Users/vasav/OneDrive/Desktop/Pictures/Screenshots/Screenshot 2026-02-12 111703.png

    # capture element screenshot
    Capture Element Screenshot    xpath://input[@id='file-upload']    C:/Users/vasav/OneDrive/Desktop/Pictures/Screenshots/Screenshot 2026-02-12 111703.png

    Sleep    2s
    # close browser
    Close Browser