import pandas as pd
import plotly.graph_objs as go
from dash import html, dcc
from sqlalchemy import text

from config.database_config import conn_string
from request.abstract_request import AbstractRequest


class BachelorMagistracyRatioRequest(AbstractRequest):
    def _AbstractRequest__get_data_frame(self, area_name: str):
        sql_result = text(
            "select (B.sum + M.sum) a_sum, B.sum::real / M.sum ratio, B.year "
            "from (select sum(total_fed_amount) + sum(contract_amount) sum, year "
            "from p2124 p "
            "join subject s on p.subject_id = s.id "
            "join vpo_spo_report vsr on s.area_id = vsr.id "
            "join area a on vsr.area_name_id = a.id "
            "where s.code like '%Б%' "
            "and a.name = :area_name "
            "group by year) B "
            "join "
            "(select sum(total_fed_amount) + sum(contract_amount) sum, year "
            "from p2124 p "
            "join subject s on p.subject_id = s.id "
            "join vpo_spo_report vsr on s.area_id = vsr.id "
            "join area a on vsr.area_name_id = a.id "
            "where s.code like '%M%' "
            "and a.name = :area_name "
            "group by year) M on B.year = M.year "
            "union "
            "select (B.sum + M.sum) a_sum, B.sum::real / M.sum ratio, B.year "
            "from (select sum(total_fed_amount) + sum(contract_amount) sum, year "
            "from old_p212 p "
            "join subject s on p.subject_id = s.id "
            "join vpo_spo_report vsr on s.area_id = vsr.id "
            "join area a on vsr.area_name_id = a.id "
            "where s.code like '%Б%' "
            "and a.name = :area_name "
            "group by year) B "
            "join "
            "(select sum(total_fed_amount) + sum(contract_amount) sum, year from old_p212 p "
            "join subject s on p.subject_id = s.id "
            "join vpo_spo_report vsr on s.area_id = vsr.id "
            "join area a on vsr.area_name_id = a.id "
            "where s.code like '%M%' "
            "and a.name = :area_name "
            "group by year) M on B.year = M.year "
            "order by year"
        )

        result = pd.read_sql(sql_result, conn_string, params={'area_name': area_name})
        return pd.DataFrame(result)

    def _AbstractRequest__get_layout(self):
        return go.Layout(
            title='График количества студентов бакалавриата, в зависимости от года',
            hovermode='closest',
            xaxis=dict(title='Отношение количества студентов магистратуры к количеству студенов бакалавриата',
                       type='log', autorange=True),
            yaxis=dict(title='Общее количество', type='log', autorange=True))

    def _AbstractRequest__get_figure(self, layout, df):
        return go.Figure(data=[go.Scatter(x=df.get('ratio'), y=df.get('a_sum'))], layout=layout)

    def _AbstractRequest__get_request(self, fig):
        return html.Div(children=[
            dcc.Graph(
                id='bachelor-magistracy-ratio-graph',
                figure=fig
            )
        ])
