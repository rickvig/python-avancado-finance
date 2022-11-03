# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG])


app.layout = dbc.Container(
    [
        html.H1("Iris k-means clustering"),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(dcc.Dropdown(
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': u'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value='MTL'
                    ), md=3),
                dbc.Col(dcc.Dropdown(
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': u'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value=['MTL', 'SF'],
                        multi=True
                    ), md=3),
                dbc.Col(dcc.Checklist(
                        options=[
                            {'label': 'New York City', 'value': 'NYC'},
                            {'label': u'Montréal', 'value': 'MTL'},
                            {'label': 'San Francisco', 'value': 'SF'}
                        ],
                        value=['MTL', 'SF']
                    ), md=3),
                dbc.Col(dcc.Slider(
                        min=0,
                        max=9,
                        marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
                        value=5,
                    ), md=3),
            ],
            align="center",
        ),
    ],
    fluid=True,
)


# app.layout = html.Div([
#     html.Div(children=[
#         html.Label('Dropdown'),
        

#         html.Br(),
#         html.Label('Multi-Select Dropdown'),
#         ,

#         html.Br(),
#         html.Label('Radio Items'),
#         dcc.RadioItems(
#             options=[
#                 {'label': 'New York City', 'value': 'NYC'},
#                 {'label': u'Montréal', 'value': 'MTL'},
#                 {'label': 'San Francisco', 'value': 'SF'}
#             ],
#             value='MTL'
#         ),
#     ], style={'padding': 10, 'flex': 1}),

#     html.Div(children=[
#         html.Label('Checkboxes'),
#         dcc.Checklist(
#             options=[
#                 {'label': 'New York City', 'value': 'NYC'},
#                 {'label': u'Montréal', 'value': 'MTL'},
#                 {'label': 'San Francisco', 'value': 'SF'}
#             ],
#             value=['MTL', 'SF']
#         ),

#         html.Br(),
#         html.Label('Text Input'),
#         dcc.Input(value='MTL', type='text'),

#         html.Br(),
#         html.Label('Slider'),
#         dcc.Slider(
#             min=0,
#             max=9,
#             marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
#             value=5,
#         ),
#     ], style={'padding': 10, 'flex': 1})
# ], style={'display': 'flex', 'flex-direction': 'row'})

if __name__ == '__main__':
    app.run_server(debug=True)
