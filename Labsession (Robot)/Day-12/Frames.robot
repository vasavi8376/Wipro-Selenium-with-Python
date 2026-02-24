*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://www.tutorialspoint.com/selenium/practice/frames.php
${BROWSER}    chrome

*** Test Cases ***
Verify Multiple Frames

    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    3s

    # FRAME 1
    Select Frame    xpath=(//iframe)[1]
    Sleep    2s

    ${text1}=    Get Text    xpath=//h1
    Log To Console    Frame 1 Text: ${text1}
    Sleep    2s

    Unselect Frame
    Sleep    2s

    # FRAME 2
    Select Frame    xpath=(//iframe)[2]
    Sleep    2s

    ${text2}=    Get Text    xpath=//h1
    Log To Console    Frame 2 Text: ${text2}
    Sleep    2s

    Unselect Frame
    Sleep    2s

    # Verify main page content
    Page Should Contain    Frames
    Sleep    2s

    Close Browser