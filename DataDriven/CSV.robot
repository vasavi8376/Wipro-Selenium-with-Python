*** Settings ***
Library      SeleniumLibrary
Library      DataDriver     file=C:/Users/vasav/PycharmProjects/Robot Framework/TestData/ddtLogindataCSV.csv    sheet_name=ddtLogindataCSV
#test template provide a data-driven aproach to testing by allowing a single keyword
#to be executed multiple times with different data sets.

Test Template     Login Test
Test Setup         Open Browser                                https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
Suite Teardown   Close Browser

*** Test Cases ***
Login with user       ${username}and    ${password}
*** Keywords ***
Login Test
        [Arguments]        ${username}       ${password}
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