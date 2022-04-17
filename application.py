from dash import Dash, dcc, html, Input, Output, callback

from request.bachelor_magistracy_ratio_request import BachelorMagistracyRatioRequest
from route import area_selection_proxy
from route.index import get_index_page

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

server = app.server

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname: str):
    if pathname == '/':
        return get_index_page()
    elif pathname.startswith('/request-'):
        return area_selection_proxy.get_area_selection_page()
    else:
        return '404'


@callback(
    Output('area_id', 'children'),
    Input('area_name', 'value'),
    Input('url', 'pathname'),
)
def area_selection_callback(value, pathname):
    if value is None:
        return
    elif pathname == '/request-bachelor-magistracy-ratio':
        ratio = BachelorMagistracyRatioRequest()
    else:
        return
    return ratio.get_result(value)


if __name__ == '__main__':
    app.run_server(debug=True)
