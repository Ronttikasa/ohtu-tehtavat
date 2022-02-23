*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  silja  silja123
    Output Should Contain  New user registered

Register With Too Short Username And Valid Password
    Input Credentials  si  silja123
    Output Should Contain  Username has to consist of characters a-z and be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  silja  silja1
    Output Should Contain  Password has to be at least 8 characters and contain at least one non-letter

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  silja  salasana
    Output Should Contain  Password has to be at least 8 characters and contain at least one non-letter

Register With Already Taken Username And Valid Password
    Input Credentials  kaori  salasana!
    Output Should Contain  User with username kaori already exists

*** Keywords ***
Input New Command And Create User
    Create User  kaori  kaori123
    Input New Command

