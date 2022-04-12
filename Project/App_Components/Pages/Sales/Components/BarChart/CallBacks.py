import dash
from MainDash import app
from dash import Input, Output, ALL
from App_Components.Pages.Sales.Components.BarChart.BarChart import HBarChart


# @app.callback(
#     Output({'type': 'sales_graph', 'index': 'bar_chart_categories'}, 'figure'),
#     Input({'type': 'sales_kpi', 'index': ALL}, 'className'),
#     prevent_initial_call=True
# )
# def display_output(_):
#     # Checking what filters to active
#     filters_list = []
#     for kpi in dash.callback_context.inputs_list[0]:
#         if "sales__kpis-item--active" in kpi['value']:
#             filters_list.append(kpi['id']['index'])
#     # Making the new figure
#     fig = HBarChart(filters_list)

#     return fig

def HBarChartCallBack():
    app.callback(
        Output({'type': 'sales_graph', 'index': 'bar_chart_categories'}, 'figure'),
        Input({'type': 'sales_kpi', 'index': ALL}, 'className'),
        prevent_initial_call=True
    )(display_output)


def display_output(_):
    print("CALLED")
    # Checking what filters to active
    filters_list = []
    for kpi in dash.callback_context.inputs_list[0]:
        if "sales__kpis-item--active" in kpi['value']:
            filters_list.append(kpi['id']['index'])
    # Making the new figure
    fig = HBarChart(filters_list)

    return fig
