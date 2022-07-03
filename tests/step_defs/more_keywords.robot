*** Settings ***
Documentation     Generic keywords file

Library             Collections
Library             RequestsLibrary
Variables           ../../settings.py


*** Keywords ***
the correct token is returned: ${token}
    [documentation]     Generic Keyword to validate login token
    should be equal    ${resp}[token]         ${token}        Token returned isn't the expected: ${token}