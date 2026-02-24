*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}        https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

*** Test Cases ***
Verify Login Scenario With Valid Credentials
    Open Browser    ${URL}    edge
    Maximize Browser Window

    # wait till page loads
    Wait Until Element Is Visible    xpath://input[@name='username']

    # enter username
    Input Text    xpath://input[@name='username']    admin

    # enter password
    Input Text    xpath://input[@name='password']    admin123

    # click login
    Click Element    xpath://button[@type='submit']

    # validate home page loaded (Dashboard heading visible)
    Wait Until Element Is Visible    xpath://body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='oxd-grid-3 orangehrm-dashboard-grid']/div[2]
    Element Should Be Visible    xpath://body/div[@id='app']/div[@class='oxd-layout orangehrm-upgrade-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='oxd-grid-3 orangehrm-dashboard-grid']/div[2]

    Close Browser