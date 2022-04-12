from dash import html, dcc
from datetime import datetime
from pytz import timezone
from App_Components.NavBar.CallBacks import *


def navbar():
    date_time = datetime.now(timezone('Israel')).strftime("%d/%m/%Y %H:%M")
    return html.Div(
        className="navbar",
        children=[
            html.H3(
                className="navbar__item navbar__header heading-4",
                children=html.P("Iowa Liquor")
            ),
            html.Div(
                className="navbar__icons-container",
                children=[
                    html.Div(),
                    html.Div(),
                    html.Div(),
                    html.Div(),
                    html.Div()
                ]
            ),
            html.Div(
                className="navbar__links",
                children=[
                    dcc.Link(
                        className="navbar__item navbar__link",
                        children=html.P("Sales"),
                        href="/Sales"
                    ),
                    dcc.Link(
                        className="navbar__item navbar__link",
                        children=html.P("Inventory"),
                        href="/Inventory"
                    ),
                    dcc.Link(
                        className="navbar__item navbar__link",
                        children=html.P("Page"),
                        href="/Page"
                    ),
                ]
            ),
            html.Div(
                className="navbar__time",
                children=[
                    html.Img(
                        className="navbar__time--icon",
                        src="assets/clock.svg",
                    ),
                    html.P(
                        className="navbar__time--datetime",
                        id="navbar-time-datetime",
                        children=f"{date_time}"
                    ),
                    dcc.Interval(
                        id='navbar-time-interval',
                        interval=1*5000,  # in milliseconds
                        n_intervals=0
                    )
                ]
            ),


        ]
    )
