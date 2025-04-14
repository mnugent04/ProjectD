import plotly.express as px
import plotly.graph_objects as go
from data import df_all, top_countries, bottom_countries, time_series_data

def create_top_bar_chart():
    df_top = df_all[df_all['Country'].isin(top_countries)]
    fig = px.bar(df_top, x='Country', y='Coffee',
                 hover_data=['Death'], title="Top Coffee Consumers (High Death Rates)",
                 labels={'Coffee': 'Coffee Consumption (kg/year)'})
    fig.update_traces(marker_color='brown')
    # Annotations for death rates
    for i, row in df_top.iterrows():
        fig.add_annotation(x=row['Country'], y=row['Coffee'],
                           text=f"Death Rate: {row['Death']}",
                           showarrow=True, arrowhead=2, ax=0, ay=-30,
                           font=dict(color="red"))

        fig.update_yaxes(range=[0, 6000])

    return fig

def create_bottom_bar_chart():
    df_bottom = df_all[df_all['Country'].isin(bottom_countries)]
    fig = px.bar(df_bottom, x='Country', y='Coffee',
                 hover_data=['Death'], title="Bottom Coffee Consumers (Low Death Rates)",
                 labels={'Coffee': 'Coffee Consumption (kg/year)'})
    fig.update_traces(marker_color='lightblue')
    # Annotations for death rates
    for i, row in df_bottom.iterrows():
        fig.add_annotation(x=row['Country'], y=row['Coffee'],
                           text=f"Death Rate: {row['Death']}",
                           showarrow=True, arrowhead=2, ax=0, ay=-30,
                           font=dict(color="red"))

    fig.update_yaxes(range=[0, 6000])
    return fig


def create_time_series_chart(selected_country):
    data = time_series_data[selected_country]
    years = data["Year"]
    coffee_values = data["Coffee"]
    death_values = data["Death"]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=years,
        y=coffee_values,
        mode="lines+markers",
        name="Coffee Consumption (kg/year)",
        line=dict(color="brown")
    ))

    fig.add_trace(go.Scatter(
        x=years,
        y=death_values,
        mode="lines+markers",
        name="Death Rate (per 1,000 people)",
        line=dict(color="red"),
        yaxis="y2"
    ))

    fig.update_layout(
        title=f"Time Series Data for {selected_country}",
        xaxis_title="Year",
        yaxis=dict(
            title="Coffee Consumption (kg/year)",
            tickfont=dict(color="brown")
        ),
        yaxis2=dict(
            title="Death Rate (per 1,000)",
            overlaying="y",
            side="right",
            tickfont=dict(color="red"),
            range=[min(death_values)-0.1, max(death_values)+0.1]
        ),
        xaxis=dict(
            tickmode="array",
            tickvals=years,
            ticktext=[str(year) for year in years],
            range=[min(years), max(years)]
        ),
        template="plotly_white"
    )

    return fig

