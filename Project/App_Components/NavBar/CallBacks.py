from dash.dependencies import Input, Output
from datetime import datetime
from pytz import timezone
from MainDash import app
from App_Components.Pages.Sales.Sales import salesPage


@app.callback(
    Output('navbar-time-datetime', 'children'),
    Input('navbar-time-interval', 'n_intervals')
)
def update_datetime(n):
    return str(datetime.now(timezone('Israel')).strftime("%d/%m/%Y %H:%M"))


@app.callback(
    Output('activePage', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/Sales':
        return salesPage()
    elif pathname == '/Inventory':
        return None
    else:
        return None
