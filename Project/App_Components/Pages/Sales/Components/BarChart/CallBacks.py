import dash
from MainDash import app
from dash import Input, Output, ALL, State, MATCH
from App_Components.Pages.Sales.Components.BarChart.BarChart import HBarChart
import pandas as pd


# Connects Grouped bar chart to Kpis
@app.callback(
    Output({'type': 'sales_graph', 'index': ALL}, 'figure'),
    Input({'type': 'sales_kpi', 'index': ALL}, 'className'),
    State({'type': 'memory_storage', 'index': ALL}, 'data'),
    prevent_initial_call=True
)
def display_output(_, graphs_data):
    # Checking what filters to active
    filters_list = []
    for kpi in dash.callback_context.inputs_list[0]:
        if 'sales__kpis-item--active' in kpi['value']:
            filters_list.append(kpi['id']['index'])
    # Making the new figure
    figures = []
    for data in graphs_data:
        df = pd.read_json(data, orient='records')
        figures.append(HBarChart(df, filters_list))

    return figures
