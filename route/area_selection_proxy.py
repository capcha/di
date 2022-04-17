import pandas as pd
from dash import html, dcc
from sqlalchemy import text

from config.database_config import conn_string


def get_area_names():
    sql_result = text("select * from area")
    result = pd.read_sql(sql_result, conn_string)
    return pd.DataFrame(result)


def get_area_selection_page():
    return html.Div([
        html.Header(),
        html.H3('Выберите регион:'),
        html.Div([
            dcc.Dropdown(
                {f'{i}': f'{i}' for i in get_area_names().get('name')},
                id='area_name'
            )],
            style={"width": "25%"}),
        html.Div(id='area_id'),
        html.Footer('НГТУ 2022')
    ], className='page-div')