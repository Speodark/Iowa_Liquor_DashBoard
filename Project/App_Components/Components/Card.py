from dash import html


def Card(id=None, className="", style={}, children=None):
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
