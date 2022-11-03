# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from re import template
import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')



fig_scatter = px.scatter(df, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60,
                 template='plotly_dark')

fig_bar = px.bar(df, x="country", y="life expectancy", color="gdp per capita", barmode="group")


fig_scatter.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)
fig_bar.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

def header():
    return html.Div(
        style={
            'backgroundColor': colors['background'],
            'padding': 10, 
            'flex': 1
        }, 
        children=[
            html.H1(
                children='Análise de desnsidade Populacional',
                style={
                    'textAlign': 'center',
                    'color': colors['text']
                }
            ),
        ]
    )

def body():
    return html.Div(
        style={'display': 'flex', 'flex-direction': 'row'}, 
        children = [
            html.Div(
                style={
                    'backgroundColor': colors['background'],
                    'padding': 10, 
                    'flex': 1
                }, 
                children=[
                    dcc.Graph(
                        id='example-graph-2',
                        figure=fig_scatter
                    ),
                ]
            ),
            html.Div(
                style={
                    'backgroundColor': colors['background'],
                    'padding': 10, 
                    'flex': 1
                }, 
                children=[
                    dcc.Graph(
                        id='example-graph-1',
                        figure=fig_bar
                    ),
                ]
            )            
    ])

def footer():
    return html.Div(
        style={
            'backgroundColor': colors['background'],
            'padding': 10, 
            'flex': 1
        }, 
        children=[
            dash_table.DataTable(
                id='table',
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict('records'),
            )
        ]
    )

app.layout = html.Div([
    header(),

    body(),
    
    footer()
])


if __name__ == '__main__':
    app.run_server(debug=True)