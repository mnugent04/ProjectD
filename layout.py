from dash import dcc, html
from figures import create_top_bar_chart, create_bottom_bar_chart, create_time_series_chart
from data import all_countries

def create_layout():
    return html.Div(style={
            'padding': '40px',
            'backgroundColor': '#f8f9fa',
            'fontFamily': 'Arial, sans-serif'
        }, children=[
            html.H1("Drink Coffee, Die Sooner: The Global Epidemic ☕", style={
                'textAlign': 'center',
                'color': '#343a40',
                'marginBottom': '5px'
            }),
            html.H4("By Meghan Nugent CS-150", style={
                'textAlign': 'center',
                'color': '#6c757d',
                'marginBottom': '40px'
            }),

            html.Div([
                html.H2("Comparative Bar Charts", style={'color': '#212529'}),
                html.Div([
                    dcc.Graph(id='top-bar-chart', figure=create_top_bar_chart(), config={'displayModeBar': False},
                              style={'width': '48%'}),
                    dcc.Graph(id='bottom-bar-chart', figure=create_bottom_bar_chart(), config={'displayModeBar': False},
                              style={'width': '48%'})
                ], style={
                    'display': 'flex',
                    'justifyContent': 'space-between',
                    'flexWrap': 'wrap',
                    'gap': '4%',
                    'alignItems': 'flex-start'
                }),
            ], style={
                'backgroundColor': 'white',
                'padding': '30px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 10px rgba(0, 0, 0, 0.1)',
                'marginBottom': '40px'
            }),

            html.Div([
                html.H2("Time Series for Selected Country", style={'color': '#212529'}),
                dcc.Graph(id='time-series-chart', figure=create_time_series_chart(all_countries[0]))
            ], style={
                'backgroundColor': 'white',
                'padding': '30px',
                'borderRadius': '10px',
                'boxShadow': '0 2px 10px rgba(0, 0, 0, 0.1)'
            })
        ])