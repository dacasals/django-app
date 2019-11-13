*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary

*** Variables ***
${LOGIN URL}      http://main_appfw.com/login
${PROFILE URL}    http://main_appfw.com/profile/update
${BROWSER}        Chrome

*** Test Cases ***
Valid Login
    Open Browser To Login Page
    Input Username    daniel
    Input Password    Explorer123
    Submit Credentials
    Check Some Things

#    Open Browser To Profile Page
#    [Teardown]    Close Browser

Valid Profile Update
    Open Browser To Login Page
    Input Username    daniel
    Input Password    Explorer123
    Submit Credentials
    Open Browser To Profile Page
    


*** Keywords ***
Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Title Should Be    main_appvuetify

Input Username
    [Arguments]    ${username}
    Input Text    name:username    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    name:password    ${password}

Submit Credentials
    Click Button    Login

Check Some Things
    Capture Page Screenshot
    Wait Until Page Contains Element 	css:div.v-toolbar__title
    Capture Page Screenshot


Capture Page Screenshot filename=selenium-screenshot-{index}.png

Open Browser To Profile Page
    Open Browser  ${PROFILE URL} ${BROWSER}
    Title Should Be    main_appvuetify
