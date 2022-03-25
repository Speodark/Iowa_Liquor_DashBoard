from dash import html
from Components.Pages.Sales.Sales import salesPage


activePage = html.Div(
    className="activePage",
    children=[
        salesPage()
    ]
)
