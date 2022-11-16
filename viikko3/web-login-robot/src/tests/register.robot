*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  username
    Set Password  password1
    Set Password Confirmation  password1
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  u
    Set Password  password1
    Set Password Confirmation  password1
    Submit Credentials
    Register Should Fail With Message  Username u is not valid

Register With Valid Username And Too Short Password
    Set Username  user
    Set Password  passwo1
    Set Password Confirmation  passwo1
    Submit Credentials
    Register Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  user
    Set Password  password1
    Set Password Confirmation  password2
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  pasi
    Set Password  password1
    Set Password Confirmation  password1
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  pasi
    Set Password  password1
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  in
    Set Password  valid
    Set Password Confirmation  valid
    Submit Credentials
    Register Should Fail With Message  Username in is not valid
    Go To Login Page
    Set Username  in
    Set Password  valid
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}