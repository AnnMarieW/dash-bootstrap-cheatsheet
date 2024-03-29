"""
Main APP

This is the starting point for the Dash Boostrap 5 Cheatsheet

The main layout is defined here.
See the content folder for the content of the offcanvas component.
See index_examples.py for the links between the name of the item in the
cheatsheet cards content of the offcanvas component.

"""

from dash import Dash, html, dcc, Input, Output, MATCH, callback_context, State
import dash_bootstrap_components as dbc
import json

from utilities import new_items, dbc_home_url
from index_examples import examples

from content.utility_border import utility_border
from content.utility_background import utility_background
from content.utility_color import utility_color
from content.utility_display import utility_display
from content.utility_sizing import utility_sizing
from content.utility_spacing import utility_spacing_margin, utility_spacing_padding
from content.utility_opacity import utility_opacity
from content.utility_position import utility_position
from content.utility_text import utility_text
from content.misc_helpers import misc_helpers
from content.utility_flex import utility_flex
from content.utility_gutter import utility_gutter
from content.dbc_components import dbc_components1, dbc_components2, dbc_components3
from content.plotly_components import plotly_links
from content.about import about, book
from content.typography import typography

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])
app.title = "Cheatsheet"
dbc_logo = "https://user-images.githubusercontent.com/72614349/133677816-5ea52424-bfd3-4405-9ccf-8ad0dbd18020.png"
bootstrap_logo = "https://user-images.githubusercontent.com/72614349/133683669-eef08b42-2eff-49df-b0a5-33a7754a2b86.png"
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
dash_url = "https://dash.plotly.com/"

header = html.Div(
    dbc.Container(
        [
            html.H1("Dash Bootstrap Cheatsheet", className="display-3 text-white",),
            html.P(
                "A guide for using Bootstrap 5 utility classes in Plotly Dash Apps",
                className="fst-italic lead",
            ),
            html.Div(
                [
                    html.A(
                        html.Img(src=plotly_logo, height=80, className="me-2"),
                        href=dash_url,
                        target="_blank",
                    ),
                    html.A(
                        html.Img(src=dbc_logo, height=80, className="me-2"),
                        href=dbc_home_url,
                        target="_blank",
                    ),
                    html.A(
                        html.Img(src=bootstrap_logo, height=80),
                        href="https://getbootstrap.com/docs/5.1/getting-started/introduction/",
                        target="blank",
                    ),
                ], className="text-nowrap"
            ),
            html.Div(
                [
                    dbc.Button(
                        "Go To Dash Bootstrap Theme Explorer",
                        color="secondary",
                        href="https://hellodash.pythonanywhere.com/",
                        external_link=True,
                        target="_blank",
                        className="me-2",
                        size="sm"

                    ),
                ],
                className="mt-4"
            ),
            dbc.Button(
                "Highlight New",
                id="new",
                n_clicks=0,
                color="secondary",
                className="position-absolute bottom-0 end-0 p-3",
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-primary text-light rounded-3 mb-4  position-relative",
    style={"height": 425},
)


"""
=====================================================================
Layout and Callbacks
"""


app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(utility_background),
                dbc.Col(utility_border),
                dbc.Col(utility_color),
                dbc.Col(utility_display),
                dbc.Col(utility_gutter),
                dbc.Col(utility_opacity),
                dbc.Col(utility_position),
                dbc.Col(utility_sizing),
                dbc.Col(utility_spacing_margin),
                dbc.Col(utility_spacing_padding),
                dbc.Col(utility_text),
                dbc.Col(typography),
                dbc.Col(misc_helpers),
                dbc.Col(utility_flex),
                dbc.Col(dbc_components1),
                dbc.Col(dbc_components2),
                dbc.Col(dbc_components3),
                dbc.Col(plotly_links),
            ]
        ),

        dbc.Row(dbc.Col([about, book]))

    ],
    fluid=True,
)


@app.callback(
    Output({"type": "off-canvas", "index": MATCH}, "is_open"),
    Output({"type": "off-canvas", "index": MATCH}, "style"),
    Output({"type": "code", "index": MATCH}, "children"),
    Output({"type": "preview", "index": MATCH}, "children"),
    Input({"type": "list-item", "index": MATCH}, "n_clicks"),
    Input({"type": "button", "index": MATCH}, "n_clicks"),
    prevent_initial_call=True,
)
def open_card_modal(example_click, fullscreen_click):
    """ opens offcanvas content for item in card & controls screen size """

    # This gets the name of the clicked on example (I know it's ugly)
    input_id = callback_context.triggered[0]["prop_id"].split(".")[0]
    example_name = json.loads(input_id)["index"] if "index" in input_id else ""

    style = (
        {"position": "absolute", "height": 1000}
        if fullscreen_click
        else {"position": "absolute", "height": 400}
    )
    open_offcanvas = True if example_click else False

    return open_offcanvas, style, examples[example_name][0], examples[example_name][1]


@app.callback(
    [Output({"type": "list-item", "index": n}, "className") for n in new_items],
    Input("new", "n_clicks"),
    State({"type": "list-item", "index": "vstack"}, "className"),
    prevent_initial_call=True,
)
def show_new(n, current_class):
    new_className = (
        "bg-secondary text-white border-0"
        if current_class == "border-0"
        else "border-0"
    )
    return [new_className] * len(new_items)


def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)
