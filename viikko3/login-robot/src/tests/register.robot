*** Settings ***
Resource  resource.robot
Test Setup  Input New Account Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  password12
    Output Should Contain  New user registered
Register With Already Taken Username And Valid Password
    Input Credential  user  password1
    Input New Account Command
    Input Credentials  user  password1
    Output Should Contain  User with username user already exists
Register With Too Short Username And Valid Password
    Input Credentials  u  password12
    Output Should Contain  Username u is not valid
Register With Valid Username And Too Short Password
    Input Credentials  user  pass
    Output Should Contain  Password is not valid
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password is not valid