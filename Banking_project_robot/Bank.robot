*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}           https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login
${BROWSER}        chrome
${FIRST_NAME}     Jane
${LAST_NAME}      Doe
${POST_CODE}      523110
${DEPOSIT_AMT}    500
${WITHDRAW_AMT}   200

*** Test Cases ***
Complete Banking Workflow Test
    [Documentation]    Test Login, Add Customer, Open Account, and Transactions.
    Open Bank Application
    Manager: Add New Customer
    Manager: Open New Account
    Customer: Login and Perform Transactions
    [Teardown]    Close Browser

*** Keywords ***
Open Bank Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Manager: Add New Customer
    Click Button    xpath://button[text()='Bank Manager Login']
    Click Button    xpath://button[contains(.,'Add Customer')]
    Input Text      xpath://input[@placeholder='First Name']    ${FIRST_NAME}
    Input Text      xpath://input[@placeholder='Last Name']     ${LAST_NAME}
    Input Text      xpath://input[@placeholder='Post Code']     ${POST_CODE}
    Click Button    xpath://button[@type='submit']
    Handle Alert    ACCEPT

Manager: Open New Account
    Click Button    xpath://button[contains(.,'Open Account')]
    Select From List By Label    id:userSelect    ${FIRST_NAME} ${LAST_NAME}
    Select From List By Label    id:currency      Dollar
    Click Button    xpath://button[@type='submit']
    Handle Alert    ACCEPT

Customer: Login and Perform Transactions
    Click Button    xpath://button[contains(.,'Home')]
    Click Button    xpath://button[text()='Customer Login']
    Select From List By Label    id:userSelect    ${FIRST_NAME} ${LAST_NAME}
    Click Button    xpath://button[@type='submit']

    # Validate Initial Balance
    Element Text Should Be    xpath://strong[2]    0

    # Deposit
    Click Button    xpath://button[contains(.,'Deposit')]
    Input Text      xpath://input[@placeholder='amount']    ${DEPOSIT_AMT}
    Click Button    xpath://button[@type='submit']
    Element Text Should Be    xpath://span[@ng-show='message']    Deposit Successful

    # Validate Balance after Deposit
    Element Text Should Be    xpath://strong[2]    ${DEPOSIT_AMT}

    # Withdraw
    Click Button    xpath://button[contains(.,'Withdrawl')]
    # Wait for the withdrawal input to appear (Angular delay)
    Sleep    2s
    Input Text      xpath://input[@placeholder='amount']    ${WITHDRAW_AMT}
    Click Button    xpath://button[@type='submit']
    Element Text Should Be    xpath://span[@ng-show='message']    Transaction successful

    # Validate Final Balance
    # Formula: 500 - 200 = 300
    Element Text Should Be    xpath://strong[2]    300