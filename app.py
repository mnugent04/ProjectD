import dash
from callbacks import register_callbacks
from layout import create_layout

app = dash.Dash(__name__)

app.layout = create_layout()

register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
