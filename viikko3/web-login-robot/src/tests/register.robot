*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  silja
    Set Password  silja123
    Confirm Password  silja123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  si
    Set Password  silja123
    Confirm Password  silja123
    Submit Credentials
    Registration Should Fail With Message  Username has to consist of characters a-z and be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  silja
    Set Password  silja
    Confirm Password  silja
    Submit Credentials
    Registration Should Fail With Message  Password has to be at least 8 characters and contain at least one non-letter

Register With Nonmatching Password And Password Confirmation
    Set Username  silja
    Set Password  silja123
    Confirm Password  kalle123
    Submit Credentials
    Registration Should Fail With Message  Passwords don't match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register