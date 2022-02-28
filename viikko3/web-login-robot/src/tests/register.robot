*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  silja
    Set Password  silja123
    Confirm Password  silja123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  si
    Set Password  silja123
    Confirm Password  silja123
    Submit Registration
    Registration Should Fail With Message  Username has to consist of characters a-z and be at least 3 characters

Register With Valid Username And Too Short Password
    Set Username  rontti
    Set Password  rontti
    Confirm Password  rontti
    Submit Registration
    Registration Should Fail With Message  Password has to be at least 8 characters and contain at least one non-letter

Register With Nonmatching Password And Password Confirmation
    Set Username  rontti
    Set Password  rontti123
    Confirm Password  kalle123
    Submit Registration
    Registration Should Fail With Message  Passwords don't match

Login After Successful Registration
    Create User  yuzuru  4axel2022
    Go To Login Page
    Set Username  yuzuru
    Set Password  4axel2022
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Create User  kaori  saka
    Go To Login Page
    Set Username  kaori
    Set Password  saka
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}