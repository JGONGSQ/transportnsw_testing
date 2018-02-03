*** Keywords ***
a anonymous user to the ${page_url}
    Go To Page    /trip_planner_home


he excutes a trip plan from ${origin} to ${destination}
    Input Text    from_origin    ${origin}
    Input Text    to_destination    ${destination}
    Capture Page Screenshot
    Click    go    /trip_planner_home    Trip Planner



a list of trips should be provided
    should be visible    result_list
