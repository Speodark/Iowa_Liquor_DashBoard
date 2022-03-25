import dash

app = dash.Dash(__name__, assets_folder=".", suppress_callback_exceptions=True)
app.title = 'Iowa Liquor'
