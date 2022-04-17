import pandas as pd
from dash import html, dcc
from sqlalchemy import text
import plotly.graph_objs as go

from config.database_config import conn_string


def get_request(area_name):
    t = text(
        "select sum(total_fed_amount) + sum(contract_amount) sum, year "
        "from p2124 p join subject s on p.subject_id = s.id "
        "join vpo_spo_report vsr on s.area_id = vsr.id "
        "join area a on vsr.area_name_id = a.id "
        "where s.code like '%Б%' and a.name = :area_name "
        "group by year "
        "union "
        "select sum(total_fed_amount) + sum(contract_amount) sum, year "
        "from old_p212 p join subject s on p.subject_id = s.id "
        "join vpo_spo_report vsr on s.area_id = vsr.id "
        "join area a on vsr.area_name_id = a.id "
        "where s.code like '%Б%' and a.name = :area_name "
        "group by year "
        "order by year"
    )

    result = pd.read_sql(t, conn_string, params={'area_name': area_name})
    df = pd.DataFrame(result)
    fig = go.Figure(data=[go.Scatter(x=df.get('year'), y=df.get('sum'))])

    return html.Div(children=[
        dcc.Graph(
            id='example-graph',
            figure=fig
        )
    ])


# -- Общоее количество бакалавров и магистров в году, в области (для новых годов p2124, для старых old_p212)
# select bachelor.sum Бакалавр, master.sum Магистратура, bachelor.name Область, bachelor.year Год
# from (select sum(total_fed_amount) + sum(contract_amount) sum, year, a.name
#       from p2124 p
#                join subject s on p.subject_id = s.id
#                join vpo_spo_report vsr on s.area_id = vsr.id
#                join area a on vsr.area_name_id = a.id
#       where s.code like '%Б%'
#       group by year, a.name) bachelor
#         full join (
#     select sum(total_fed_amount) + sum(contract_amount) sum, year, a.name
#     from p2124 p
#              join subject s on p.subject_id = s.id
#              join vpo_spo_report vsr on s.area_id = vsr.id
#              join area a on vsr.area_name_id = a.id
#     where s.code like '%M%'
#     group by year, a.name) master on master.name = bachelor.name and master.year = bachelor.year
# order by bachelor.name, bachelor.year;