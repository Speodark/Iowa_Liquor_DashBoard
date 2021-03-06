from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px


def ChoroplethMap():
    with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
        counties = json.load(response)
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                     dtype={"fips": str})
    fig = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                        color_continuous_scale="Viridis",
                        range_color=(0, 12),
                        scope="usa",
                        labels={'unemp': 'unemployment rate'}
                        )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )
    return fig
