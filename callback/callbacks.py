from dash import callback, Output, Input


@callback(
    Output('page-index-display-value', 'children'))
def display_value(value):
    return f'You have selected {value}'


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'


@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value(value):
    return f'You have selected {value}'


@callback(
    Output('example-graph', 'children'))
def display_value(value):
    return f'You have selected {value}'
