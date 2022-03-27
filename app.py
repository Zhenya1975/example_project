import pandas as pd
# import numpy as np
from dash import Dash, dcc, html, Input, Output, callback_context, State, callback_context
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import ThemeSwitchAIO
from dash_bootstrap_templates import load_figure_template



# import fig_coverage

# select the Bootstrap stylesheet2 and figure template2 for the theme toggle here:
# template_theme1 = "sketchy"
template_theme1 = "flatly"
template_theme2 = "darkly"
# url_theme1 = dbc.themes.SKETCHY
url_theme1 = dbc.themes.FLATLY
url_theme2 = dbc.themes.DARKLY

loading_style = {
    # 'position': 'absolute',
    # 'align-self': 'center'
}

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
    "sandstone"
]

load_figure_template(templates)

dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.1/dbc.min.css"
)
app = Dash(__name__, external_stylesheets=[url_theme1, dbc_css])

"""
===============================================================================
Layout
"""



app.layout = dbc.Container(
    dbc.Row([
        dbc.Col(
            [
                html.H4("ЗАГОЛОВОК"),
                ThemeSwitchAIO(
                    aio_id="theme", themes=[url_theme1, url_theme2],
                ),

                html.Div(
                    [
                        dbc.Input(id="input_id", placeholder="Type something...", type="text"),
                        html.Br(),
                        html.P(id="output_id"),
                    ]),



            ]
        )
    ]
    ),
    className="m-4 dbc",
    # fluid=True,

)


######################### ОСНОВНОЙ ОБРАБОТЧИК ##############################
@app.callback([
    Output("output_id", "children"),

],
    [
        Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
        Input("input_id", "value")
    ],
)

def main_function(theme_selector, input_value):
    if theme_selector:
        graph_template = 'sandstone'
    text_output = ""
    if input_value != None:
        text_output = input_value


    return [text_output]



if __name__ == "__main__":
    # app.run_server(debug=True)
    app.run_server(host='0.0.0.0', debug=True)