import dash
from dash import Input, Output
import plotly.graph_objects as go
from figures import create_time_series_chart


def register_callbacks(app):
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