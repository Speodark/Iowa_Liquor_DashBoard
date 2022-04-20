from dash.dependencies import Input, Output, State, ALL
from datetime import datetime
from pytz import timezone
from MainDash import app
import dash
from App_Components.Pages.Sales.Sales import salesPage


@app.callback(
    Output('navbar-time-datetime', 'children'),
    Input('navbar-time-interval', 'n_intervals')
)
def update_datetime(n):
    return str(datetime.now(timezone('Israel')).strftime("%d/%m/%Y %H:%M"))


@app.callback(
    Output({"type": "navlink", "index": ALL}, "className"),
    Output('activePage', 'children'),
    Input('url', 'pathname'),
    State({"type": "navlink", "index": ALL}, "className")
)
def display_page(pathname, navlink_classnames):
    # Getting a list of the navlink indexes from the output
    # using that i can return and remove the classname from each index
    # that should be active or disabled
    active_link = []
    for output in dash.callback_context.outputs_list:
        if isinstance(output, list):
            for index, sub_output in enumerate(output):
                sub_output = sub_output["id"]
                if sub_output["type"] == "navlink":
                    if sub_output["index"] == pathname[1:]:
                        active_link.append(
                            navlink_classnames[index] + " navbar__link--active")
                    elif "navbar__link--active" in navlink_classnames[index]:
                        active_link.append(
                            navlink_classnames[index].replace("navbar__link--active", ""))
                    else:
                        active_link.append(navlink_classnames[index])
                else:
                    break

    if pathname == '/Sales':
        return [active_link, salesPage()]
    elif pathname == '/Inventory':
        return [active_link, None]
    else:
        return [active_link, None]
