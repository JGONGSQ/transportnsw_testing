*** Settings ***
Resource          ../resources/globalincludes.robot

*** Keywords ***
Generic Test Suite Setup
    Get Data    environment/${ENVIRONMENT}

Generic Test Suite Teardown
    Close All Browsers

Generic Test Case Teardown
    Capture Page Screenshot
    Close All Browsers

Generic Test Case Setup
    Get Data    environment/${ENVIRONMENT}

Generic Open Browser
    Run Keyword If    '${PROFILE}' == 'BUILD_BAMBOO_BROWSERSTACK'    Open Browser    ${UI_MAP}    browser=${BROWSER}    remote_url=${REMOTE_URL}
    ...    desired_capabilities=${DESIRED_CAPABILITIES}   enable_auto_visual_checks=${TRUE}     default_frame=default_iframe
    Run Keyword Unless    '${PROFILE}' == 'BUILD_BAMBOO_BROWSERSTACK'    Open Browser    ${UI_MAP}    remote_url=${REMOTE_URL}    desired_capabilities=${DESIRED_CAPABILITIES}    browser=${BROWSER}
    ...    enable_auto_visual_checks=${TRUE}    default_frame=default_iframe    ff_profile_dir=${FIREFOX_PROFILE}
