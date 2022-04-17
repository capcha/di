from dash import Dash, dcc, html, Input, Output, callback

from request.TestAreaRequest import get_request
from request.page_1 import get_page_1
from request.page_2 import get_page_2
from request.index import get_index_page

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)
server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/page1':
        return get_page_1()
    elif pathname == '/page2':
        return get_page_2()
    elif pathname == '/':
        return get_index_page()
    elif pathname == '/request':
        return get_request('Алтайский край')
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
