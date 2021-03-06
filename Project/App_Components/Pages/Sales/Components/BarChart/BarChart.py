import plotly.express as px


def HBarChart(df=None, filters=None):
    colors = {
        "revenue": "#37AAFA",
        "sales": "#B79659",
        "cost": "#E17A51",
        "bottles": "#6C5197",
        "profit": "#22D69B"
    }
    filters = list((map(lambda x: x.lower(), filters)))
    mask = df["names"].isin(filters)
    x_labels = []
    for label in df[mask]["category_name"].drop_duplicates():
        x_labels.append(label.replace(' ', '<br>'))

    fig = px.bar(
        df[mask],
        x="category_name",
        y="Value",
        color="names",
        barmode="group",
        color_discrete_map=colors
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        legend=dict(
            orientation="h",
            yanchor="middle",
            y=1.1,
            xanchor="center",
            x=0.5,
            title={'text': None}
        ),
        margin={"t": 30, "b": 0, "r": 20, "l": 0, "pad": 0},
    )
    fig.update_yaxes(title_text='')
    fig.update_xaxes(
        title_text='', tickvals=df[mask]["category_name"], ticktext=x_labels)
    return fig
