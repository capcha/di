from dash import html, dcc


def get_index_page():
    return html.Div([
        html.H1('Project'),
        dcc.Link('Navigate to "/page-1"', href='/page1'),
        html.Br(),
        dcc.Link('Navigate to "/page-2"', href='/page2'),
        html.Br(),
        dcc.Link('Navigate to "/request"', href='/request'),
        html.Div(id='page-index-display-value')
    ])
