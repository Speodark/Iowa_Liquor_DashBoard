from dash import html, dcc
from matplotlib.axis import YAxis
import plotly.express as px
from App_Components.Components.Card import Card
from App_Components.Pages.Sales.Components.KPIS.KPIS import generate_kpis
from DB.Select import getCategoriesData
import dash
from MainDash import app
from dash import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate
from App_Components.Pages.Sales.Components.BarChart.BarChart import HBarChart
from App_Components.Pages.Sales.Components.BarChart.CallBacks import *
import dash_bootstrap_components as dbc


def salesPage():
    HBarChartCallBack()
    return html.Div(
        className="sales",
        children=[
            html.Div(
                className="sales__kpis",
                children=generate_kpis()
            ),
            Card(
                className="sales__categories",
                children=[
                    dcc.Tabs(
                        children=[
                            dcc.Tab(
                                label='Categories',
                                children=dcc.Graph(
                                    id={'type': "sales_graph",
                                        "index": "bar_chart_categories"},
                                    figure=HBarChart(["revenue"]),
                                    className="fill-parent-div"
                                ),
                            ),
                            dcc.Tab(
                                label='Stores',
                                # children=dcc.Graph(
                                #     id={'type': "sales_graph",
                                #         "index": "bar_chart_stores"},
                                #     figure=HBarChart(["revenue"]),
                                #     className="fill-parent-div"
                                # ),
                            ),
                            dcc.Tab(
                                label='Vendors',
                                # children=dcc.Graph(
                                #     id={'type': "sales_graph",
                                #         "index": "bar_chart_vendors"},
                                #     figure=HBarChart(["revenue"]),
                                #     className="fill-parent-div"
                                # ),
                            ),
                        ]
                    )

                ]
            ),
            Card(
                className="sales__expense-overview",
                children=[

                ]
            ),
            Card(className="sales__overview"),
            Card(className="sales__counties")
        ]
    )
