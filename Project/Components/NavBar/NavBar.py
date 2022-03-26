from dash import html, dcc


def navbar():
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
    )
