from dash import html
from App_Components.Pages.Sales.Sales import salesPage


activePage = html.Div(
    id="activePage",
    className="activePage",
    children=salesPage()
)
