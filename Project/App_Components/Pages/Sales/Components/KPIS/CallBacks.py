from dash import Input, Output, State, MATCH, ALL
from MainDash import app


@app.callback(
    Output({'type': 'sales_kpi', 'index': MATCH}, 'className'),
    Input({'type': 'sales_kpi', 'index': MATCH}, 'n_clicks'),
    State({'type': 'sales_kpi', 'index': MATCH}, 'className'),
    State({'type': 'sales_kpi', 'index': ALL}, 'className'),
    prevent_initial_call=True
)
def display_output(_, className, kpis_classNames):
    if "sales__kpis-item--active" in className:
        # Checks how many kpis are active
        class_name_appears = 0
        for class_name in kpis_classNames:
            if "sales__kpis-item--active" in class_name:
                class_name_appears += 1
        # Disable the kpi if there is at least one more kpi active
        if class_name_appears > 1:
            className = className.split()
            className.remove("sales__kpis-item--active")
            className = " ".join(className)
    else:
        # Active the kpi
        className += " sales__kpis-item--active"
    return className
