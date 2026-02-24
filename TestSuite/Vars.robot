*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${name}       John
${city}       Hyderabad
${address}    St Peters Road

@{list1}      green    red       blue
@{list2}      apple    banana    grapes

&{creds}      username=admin    password=admin123

*** Test Cases ***
Verify the variables
    Log    ${name}
    Log    ${city}
    Log    ${address}

    # Looping through List 1
    FOR    ${element}    IN    @{list1}
        Log    ${element}
    END

    # Looping through List 2
    FOR    ${element}    IN    @{list2}
        Log    ${element}
    END

    # Accessing List items by Index (Starts at 0)
    Log    ${list1}[0]
    Log    ${list1}[1]

    # Accessing Dictionary items by Key
    Log    ${creds}[username]
    Log    ${creds}[password]