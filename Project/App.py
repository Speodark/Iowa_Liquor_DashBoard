from dash import html
from MainDash import app


# Generate the app layout
def generateAppLayout():
    return html.Div(
        className="main_container",
        children=html.Div(
            className="layout",
            children=[]
        )
    )


app.layout = generateAppLayout

if __name__ == "__main__":
    app.run_server(debug=True, port=8080, host="0.0.0.0")
