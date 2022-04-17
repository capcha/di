from dash import html, dcc


def get_page_2():
    return html.Div([
        html.H3('Page 2'),
        dcc.Dropdown(
            {f'Page 2 - {i}': f'{i}' for i in ['London', 'Berlin', 'Paris']},
            id='page-2-dropdown'
        ),
        html.Div(id='page-2-display-value'),
        dcc.Link('Go to Page 1', href='/page1'),
        html.Br(),
        dcc.Link('Go to Index', href='/')
    ])

