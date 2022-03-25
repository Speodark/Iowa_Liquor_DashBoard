from dash import html
from MainDash import app
from Components.Pages.ActivePage import activePage
from Components.NavBar.NavBar import navbar


# Generate the app layout
def generateAppLayout():
    return html.Div(
        className="container",
        children=[
            navbar(),
            activePage
        ]
    )


app.layout = generateAppLayout

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")
