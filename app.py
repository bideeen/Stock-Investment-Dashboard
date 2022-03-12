from logging import PlaceHolder
import dash
from dash import dcc as doc
from dash import html
from datetime import date as dt



app = dash.Dash(__name__)


server = app.server

item1 = html.Div(
        className="nav",
        children=[
            html.P("Welcome to the Stock Investment App!", className="start"),
            html.Div(
                [
                    # stock code input
                    html.P("Input stock code:"),
                    doc.Input(
                        id="stock-code", type="text", 
                    ),
                    html.Button(
                        'Submit', id="submit-stock", n_clicks=0
                    )
                ]
            ),
            html.Div(
                [
                    # Date range picker input
                    doc.DatePickerRange(
                        id="date-picker-range", 
                        min_date_allowed=dt(1990, 1, 1),
                        max_date_allowed=dt(250,12,30),
                        initial_visible_month=dt(2022,2, 9),
                        end_date=dt(2022,12, 9)
                    )
                ]
            ),
            html.Div(
                [
                    # Stock price button
                    html.Button(
                        'Stock Price', id="stock-price", n_clicks=0
                    ),
                    # Indicator button
                    html.Button(
                        'Indicators', id="indicator", n_clicks=0
                    ),
                    # Number of days of forecast input
                    doc.Input(
                        id="nod", type="text", placeholder="numbers of days"
                    ),
                    # Forecast button
                    html.Button(
                        'Forecast', id="forecast", n_clicks=0
                    )
                ]
            ),
        ],
    )

item2 = html.Div(
        className="content",
        children=[
            html.Div(
                className="Header",
                children=[
                    # Logo
                    # Company Name
                ],
            ),
            html.Div(
                # Description 
                id="description", className="description_ticker"
            ),
            html.Div(
                [
                    # Stock price plot
                ],
                id="graphs--content"
            ),
            html.Div(
                [
                    # Indicator plot
                ],
                id="main-content"
            ),
            html.Div(
                [
                    # Forecast plot
                ],
                id="forecast-content"
            )
        ],
    )

app.layout = html.Div([item1, item2], className="container")





if __name__ == '__main__':
    app.run_server(debug=True)
    