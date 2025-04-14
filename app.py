import dash
from dash import dcc, html, Input, Output
import plotly.graph_objects as go
from figures import create_top_bar_chart, create_bottom_bar_chart, create_time_series_chart
from data import all_countries

app = dash.Dash(__name__)

app.layout = html.Div(style={
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


@app.callback(
    Output('time-series-chart', 'figure'),
    Input('top-bar-chart', 'clickData'),
    Input('bottom-bar-chart', 'clickData')
)
def update_time_series(top_click, bottom_click):
    triggered_id = dash.ctx.triggered_id

    if triggered_id == 'top-bar-chart' and top_click:
        return create_time_series_chart(top_click['points'][0]['x'])
    elif triggered_id == 'bottom-bar-chart' and bottom_click:
        return create_time_series_chart(bottom_click['points'][0]['x'])
    else:
        # Return a placeholder
        fig = go.Figure()
        fig.update_layout(
            title="Click a country above to see its data",
            xaxis_title="Year",
            yaxis_title="Coffee Consumption",
            template="plotly_white"
        )
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
