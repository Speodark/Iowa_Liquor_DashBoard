from dash import html
from App_Components.Components.Card import Card
from DB.Select import getRevenueKPI, getSalesKPI, getCostKPI, getBottlesKPI, getProfitKPI
from App_Components.Pages.Sales.Components.KPIS.CallBacks import *


# Creates the simple kpi item with the value passed and format the value.
def create_kpi_item(kpi_name, kpi_value, className):
    # Formatting the value to be 15.2M or 26.94B and so on.
    def formatValue(value):
        value = float(value)

        if value >= 1000000000:
            value = "%.2f%s" % (value/1000000000.00, 'B')
        elif value >= 1000000:
            value = "%.2f%s" % (value/1000000.00, 'M')
        elif value >= 1000:
            value = "%.2f%s" % (value/1000.0, 'K')

        if str(value)[-2] == "0" and str(value)[-3] == "0":
            value = value.split(".")[0] + value[-1]
        elif str(value)[-2] == "0":
            value = value.split(".")[0] + "." + value[-3] + value[-1]

        return value
    return Card(
        className="center_items_vertical",
        children=[
            html.Button(
                id={'type': 'sales_kpi', 'index': kpi_name},
                className="sales__kpis-item center_items_vertical" + className,
                children=[
                    html.P(kpi_name),
                    html.P(formatValue(kpi_value))
                ]
            ),
        ]
    )


def generate_kpis():
    # KPI NAMES AND VALUES IT WILL BE IN THE SAME ORDER AS THE DICT
    kpi_dict = {"REVENUE": getRevenueKPI(), "SALES": getSalesKPI(),
                "COST": getCostKPI(), "BOTTLES": getBottlesKPI(), "PROFIT": getProfitKPI()}
    kpis = []
    for index, (kpi_name, kpi_value) in enumerate(kpi_dict.items()):
        if index == 0:
            # The space before the classname is important!
            kpis.append(create_kpi_item(
                kpi_name, kpi_value, " sales__kpis-item--active"))
        else:
            kpis.append(create_kpi_item(kpi_name, kpi_value, ""))
    return kpis
