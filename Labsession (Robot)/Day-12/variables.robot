*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
# Scalar variables
${NAME}      Vasavi
${CITY}      Hyderabad

# List variable
@{FRUITS}    Apple    Mango    Banana

# Dictionary variable
&{USER}      name=Vasavi    age=22    city=Hyderabad


*** Test Cases ***

# 1. Create a scalar variable ${NAME} and print it
Print Scalar Variable
    Log    Name is ${NAME}

# 2. Assign two numbers and print their sum
Add Two Numbers
    ${num1}=    Set Variable    10
    ${num2}=    Set Variable    20
    ${sum}=     Evaluate    ${num1} + ${num2}
    Log    Sum is ${sum}

# 3. Use ${CITY} inside a sentence
Use City In Sentence
    Log    I live in ${CITY}.

# 4. Reassign a variable value and log updated value
Reassign Variable Value
    ${count}=    Set Variable    5
    Log    Initial value: ${count}
    ${count}=    Set Variable    10
    Log    Updated value: ${count}

# 5. Print first item from list variable
Print First Fruit
    Log    First fruit is ${FRUITS}[0]

# 6. Loop through list and print each element
Loop Through List
    FOR    ${fruit}    IN    @{FRUITS}
        Log    ${fruit}
    END

# 7. Find length of list variable
Find List Length
    ${length}=    Get Length    ${FRUITS}
    Log    Length of fruits list: ${length}

# 8. Print one key value from dictionary
Print Dictionary Value
    Log    User name is ${USER}[name]

# 9. Add new key-value pair to dictionary
Add Key To Dictionary
    Set To Dictionary    ${USER}    country=India
    Log    Updated dictionary: ${USER}

# 10. Access dictionary values in loop and print key and value
Loop Dictionary Values
    FOR    ${key}    ${value}    IN    &{USER}
        Log    ${key} = ${value}
    END
