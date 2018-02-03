*** Settings ***
Suite Setup       Generic Test Suite Setup
Suite Teardown    Generic Test Suite Teardown
Test Setup        Generic Test Case Setup
Test Teardown     Generic Test Case Teardown
Resource          ../resources/globalincludes.robot
Resource          shared_keywords.robot

*** Test Cases ***
TEST001: A trip request can be executed and results returned
    a trip plan can be made    /trip    North Sydney Station, North Sydney    Town Hall Station, Sydney

*** Keywords ***
a trip plan can be made
    [Arguments]    ${page_url}    ${origin}    ${destination}
    Generic Open Browser
    Given a anonymous user to the ${page_url}
    When he excutes a trip plan from ${origin} to ${destination}
    Then a list of trips should be provided
