*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem
Library    Collections

*** Variables ***
${url}    https://the-internet.herokuapp.com/upload

*** Test Cases ***
Verify radio buttons
    Open Browser    ${url}    chrome
    Maximize Browser Window

    # wait till the element is loaded
    Sleep    3s
    Wait Until Element Is Visible    xpath://input[@id='file-upload']

    # choose the file
   Choose File    xpath://input[@id='file-upload']      C:/Users/vasav/OneDrive/Desktop/Pictures/Screenshots/Screenshot 2026-02-12 111703.png

    # click the upload button
    Click Element    xpath://input[@id='file-submit']
    Sleep    2s

    # verify upload success message
    Element Text Should Be    xpath://h3[normalize-space()='File Uploaded!']    File Uploaded!
    Sleep    2s

    # close browser
    Close Browser