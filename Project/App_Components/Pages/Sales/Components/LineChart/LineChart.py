import plotly.express as px


def LineAndBarChart(df=None):
    fig = px.line(
        df,
        x="month",
        y="sales",
    )
    fig.add_bar(x=df["month"], y=df["bottles_sold"])
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
    fig.update_xaxes(title_text='')
    return fig
