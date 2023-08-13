*** Settings ***
Documentation     Generic keywords file

Library             Collections
Library             RequestsLibrary
Variables           ../../settings.py


*** Keywords ***
The Correct Token Is Returned: ${token}
    [documentation]     Generic Keyword to validate login token
    Should Be Equal    ${resp}[token]         ${token}        Token returned isn't the expected: ${token}