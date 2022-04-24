from dash import html, dcc
from App_Components.Components.Card import Card
from App_Components.Pages.Sales.Components.KPIS.KPIS import generate_kpis
from DB.Select import getCategoriesData
import dash
from App_Components.Pages.Sales.Components.BarChart.BarChart import HBarChart
from App_Components.Pages.Sales.Components.BarChart.CallBacks import *
from App_Components.Pages.Sales.Components.LineChart.LineChart import LineAndBarChart
from App_Components.Pages.Sales.Components.LineChart.CallBacks import *
from App_Components.Pages.Sales.Components.AreaChart.AreaChart import AreaChart
from App_Components.Pages.Sales.Components.AreaChart.CallBacks import *
from App_Components.Pages.Sales.Components.ChoroplethMap.ChoroplethMap import ChoroplethMap
from App_Components.Pages.Sales.Components.ChoroplethMap.CallBacks import *
from DB.Select import getCategoriesData, getVendorsData, getStoresData, salesAndBottlesPerMonth, revenueAndCostPerMonth


def salesPage():
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
                                children=[
                                    dcc.Store(
                                        id={'type': "memory_storage",
                                            "index": "bar_chart_categories"},
                                        data=getCategoriesData().to_json(orient='records')
                                    ),
                                    dcc.Graph(
                                        id={'type': "sales_graph",
                                            "index": "bar_chart_categories"},
                                        figure=HBarChart(
                                            getCategoriesData(), ["revenue"]),
                                        className="fill-parent-div"
                                    )
                                ]
                            ),
                            dcc.Tab(
                                label='Stores',
                                children=[
                                    dcc.Store(
                                        id={'type': "memory_storage",
                                            "index": "bar_chart_stores"},
                                        data=getVendorsData().to_json(orient='records')
                                    ),
                                    dcc.Graph(
                                        id={'type': "sales_graph",
                                            "index": "bar_chart_stores"},
                                        figure=HBarChart(
                                            getVendorsData(), ["revenue"]),
                                        className="fill-parent-div"
                                    )
                                ]
                            ),
                            dcc.Tab(
                                label='Vendors',
                                children=[
                                    dcc.Store(
                                        id={'type': "memory_storage",
                                            "index": "bar_chart_vendors"},
                                        data=getStoresData().to_json(orient='records')
                                    ),
                                    dcc.Graph(
                                        id={'type': "sales_graph",
                                            "index": "bar_chart_vendors"},
                                        figure=HBarChart(
                                            getStoresData(), ["revenue"]),
                                        className="fill-parent-div"
                                    )
                                ]
                            ),
                        ]
                    )

                ]
            ),
            Card(
                className="sales__expense-overview",
                header="Sales Expenses",
                children=html.Div(
                    children=dcc.Graph(
                        id={'type': "sales_expense-overview--graph",
                            "index": "sales__expense-overview"},
                        figure=AreaChart(revenueAndCostPerMonth()),
                        className="fill-parent-div"
                    ),
                    style={"width": "100%", "height": "100%", "min-height": 0}
                )
            ),
            Card(
                className="sales__overview",
                header="Sales Overview",
                children=html.Div(
                    children=dcc.Graph(
                        id={'type': "sales_overview_graph",
                            "index": "sales__overview"},
                        figure=LineAndBarChart(salesAndBottlesPerMonth()),
                        className="fill-parent-div"
                    ),
                    style={"width": "100%", "height": "100%", "min-height": 0}
                )
            ),
            Card(
                className="sales__counties",
                # children=dcc.Graph(
                #     figure=ChoroplethMap(),
                #     className="fill-parent-div"
                # )
            )
        ]
    )
