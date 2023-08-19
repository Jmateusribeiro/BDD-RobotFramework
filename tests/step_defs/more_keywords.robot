*** Settings ***
Documentation     Generic keywords file

Library             Collections
Library             OperatingSystem
Library             RequestsLibrary
Variables           ../../settings.py
Library             dotenv


*** Keywords ***
The Correct Token Is Returned
    [Documentation]     Keyword to validate login token
    
    Set Log Level    NONE
    Load Environment Variables
    ${token}=    Get Environment Variable    ${email}
    Set Log Level    INFO
    
    Should Be Equal    ${resp}[token]         ${token}        
    ...                msg=Token returned '${resp}[token]' isn't the expected    
    ...                values=${False}

Load Environment Variables
    [Documentation]    Load environment variables from a .env file
    
    File Should Exist   ${PROJECT_DIR}/credentials.env    
    ...    msg=The file 'credentials.env' was not found in the root dir of the project

    Load Dotenv    ${PROJECT_DIR}/credentials.env