*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://www.tutorialspoint.com/selenium/practice/droppable.php

*** Test Cases ***
Verify Drag And Drop
    Open Browser    ${url}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    id:draggable    10s

    Drag And Drop    id:draggable    id:droppable

    Sleep    2s

    # Verify drop happened
    Element Text Should Be    id:droppable    Dropped!

    Close Browser