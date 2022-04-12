from dash import html, dcc
from MainDash import app
from App_Components.Pages.ActivePage import activePage
from App_Components.NavBar.NavBar import navbar


# Generate the app layout
def generateAppLayout():
    return html.Div(
        className="container",
        children=[
            dcc.Location(id='url', refresh=False),
            navbar(),
            activePage
        ]
    )


app.layout = generateAppLayout

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")
