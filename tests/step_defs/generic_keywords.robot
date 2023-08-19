*** Settings ***
Documentation     Generic keywords file

Library             Collections
Library             RequestsLibrary
Variables           ../../settings.py


*** Keywords ***
Run Post Request
    [Arguments]    ${host}  ${url}      ${body}
    
    Create Session  session  ${host}
    ${resp}=  POST On Session  session  ${url}  data=${body}      expected_status=any     headers=${contentType}      verify=${False}
    
    Status Should Be  200  ${resp}      ${resp.reason}
    Log     output: ${resp.json()}
    
    RETURN    ${resp.json()}


Email And Password Are Definied As ${email} And ${password}
    [documentation]     Generic Keyword to generate body with email and password
    
    ${body}=    Set Variable    {"email": "${email}", "password": "${password}"}
    Set Test Variable       ${email}     ${email}
    Set Test Variable       ${body}     ${body}


Registration Is Executed
    [documentation]     Generic Keyword to generate body with email and password

    ${resp}=    Run Post Request    ${API_HOST}     ${REGISTRATION_ENDPOINT}        ${body}
    Set Test Variable     ${resp}        ${resp}