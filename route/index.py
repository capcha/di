from dash import html, dcc


def get_index_page():
    return html.Div([
        html.Header(),
        html.H1('Система сбора показателей образовательных организаций', style={'text-align': 'center'}),

        html.Div([
            html.H5(
                'Система основана на итегральных ежегодных показателях деятельности образовательных организаций высшего образования (ВУЗов)'
                ' и среднего профессионального образования (колледжей).')
        ], style={
            'text-align': 'center',
            'margin-left': '20%',
            'margin-right': '20%',
        }),

        html.H5('Выберите сводную диаграмму:'),

        html.Br(),

        html.Div([
            dcc.Link('1. Как менялось соотношение обучающихся по программам бакалавриата и магистратуры',
                     href='/request-bachelor-magistracy-ratio', className='link'),
            html.Br(),
            dcc.Link('2. Как менялись предпочтения студентов, выбирающих высшее образование на контрактной основе',
                     href='/request-high-education-contract', className='link')
        ], id='page-index-display-value', style={'text-align': 'left'}),

        html.Footer('НГТУ 2022')
    ], className='page-div')
