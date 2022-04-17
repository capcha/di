from dash import html, dcc


def get_page_1():
    return html.Div([
        html.H3('Page 1'),
        dcc.Dropdown(
            {f'Page 1 - {i}': f'{i}' for i in ['New York City', 'Montreal', 'Los Angeles']},
            id='page-1-dropdown'
        ),
        html.Div(id='page-1-display-value'),
        dcc.Link('Go to Page 2', href='/page2'),
        html.Br(),
        dcc.Link('Go to Index', href='/')
    ])
