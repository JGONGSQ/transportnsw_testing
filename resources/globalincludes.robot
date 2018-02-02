*** Settings ***
Variables         global.py    ${PROFILE}
Library           Web2Library    ${ROOT_DIR}    ${RESOURCES_DIR}    ${SELENIUM_TIMEOUT_MAX}    ${SELENIUM_TIMEOUT_IMPLICIT_WAIT}    action_timeout=${ACTION_TIMEOUT}    action_retry_interval=${ACTION_RETRY_INTERVAL}
Library           Collections
Library           YamlVariablesLibrary    ${ROOT_DIR}    ${RESOURCES_DIR}
Library           String
Library           OperatingSystem
Resource          ../common_keywords/includes.robot

*** Variables ***
${PROFILE}        local
${ENVIRONMENT}    testing
${UI_MAP}         trip_planner_ui.xml