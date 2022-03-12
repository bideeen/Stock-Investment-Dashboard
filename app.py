import dash
from dash import dcc as doc
from dash import html
from datetime import date as dt



app = dash.Dash(__name__)


server = app.server

item1 = html.Div(
        [
            html.P("Welcome to the Stoxk Dash App!", className="start"),
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
                    html.DatePickerRange(
                        id="date-picker-range", 
                        min_date_allowed=dt(1990, 1, 1),
                        max_date_allowed=dt(250,12,30),
                        initial_visible_month=dt.now(),
                        end_date=dt(2022,12, 9)
                    )
                ]
            ),
            html.Div(
                [
                    # Stock price button
                    # Indicator button
                    # Number of days of forecast input
                    # Forecast button
                ]
            ),
        ],
        className="nav"
    )

item2 = html.Div(
        [
            html.Div(
                [
                    # Logo
                    # Company Name
                ],
                className="Header"
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
        className="content"
    )

app.layout = html.Div([item1, item2])





if __name__ == '__main__':
    app.run_server(debug=True)
    