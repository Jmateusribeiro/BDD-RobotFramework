*** Settings ***
Documentation     Generic keywords file

Library             Collections
Library             RequestsLibrary
Variables           ../../settings.py


*** Keywords ***
run post request
    [Arguments]    ${host}  ${url}      ${body}
    Create Session  session  ${host}
    ${resp}=  POST On Session  session  ${url}  data=${body}      expected_status=any     headers=${contentType}      verify=${False}
    Status Should Be  200  ${resp}      ${resp.reason}
    log     resposta: ${resp.json()}
    [Return]    ${resp.json()}


email and password are definied as ${email} and ${password}
    [documentation]     Generic Keyword to generate body with email and password
    ${body}=    set Variable    {"email": "${email}", "password": "${password}"}
    set test variable       ${body}     ${body}


registration is executed
    [documentation]     Generic Keyword to generate body with email and password

    ${resp}=    run post request    ${API_HOST}     ${REGISTRATION_ENDPOINT}        ${body}
    set test variable     ${resp}        ${resp}


#the correct token is returned: ${token}
#    [documentation]     Generic Keyword to validate login token
#    should be equal    ${resp}[token]         ${token}        Token returned isn't the expected: ${token}