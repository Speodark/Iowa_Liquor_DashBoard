from dash import html
import itertools


def Card(id=None, className="", style={}, children=None, header=None):
    if not isinstance(children, list) and header:
        header = html.Div(
            className="card__header",
            children=[
                html.Img(
                    className="navbar__time--icon",
                    src="assets/cube.svg",
                ),
                html.P(
                    children=header
                )
            ]
        )
        children = [children]
        children.insert(0, header)
    elif isinstance(children, list) and header:
        children.insert(0, header)
    if id:
        return html.Div(
            id=id,
            className=className + " card",
            style=style,
            children=children
        )
    else:
        return html.Div(
            className=className + " card",
            style=style,
            children=children
        )


def timeFilterCard(id=None, className="", style={}, children=None):
    if id:
        return html.Div(
            id=id,
            className=className + " card",
            style=style,
            children=children
        )
    else:
        return html.Div(
            className=className + " card",
            style=style,
            children=children
        )
