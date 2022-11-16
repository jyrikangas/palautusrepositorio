*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Login Command
    Input  login
Input New Account Command
    Input  new

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
Input Credential
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}

