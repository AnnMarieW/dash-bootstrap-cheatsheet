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

from utilities import new_items
from index_examples import examples
from content.utility_border import utility_border
from content.utility_color import utility_color
from content.utility_display import utility_display
from content.utility_spacing import utility_spacing
from content.utility_opacity import utility_opacity
from content.utility_position import utility_position
from content.utility_text import utility_text
from content.utility_misc import utility_misc
from content.utility_flex import utility_flex
from content.utility_grid import utility_grid
from content.dbc_components import dbc_components1, dbc_components2
from content.plotly_components import plotly_links

app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP])

header = html.Div(
    dbc.Container(
        [
            html.H1("Dash Bootstrap 5 Cheatsheet", className="display-3 text-white",),
            html.P(
                "A guide for using Bootstrap 5 Utility classes in Dash Bootstrap Components V1",
                className="fst-italic lead",
            ),
            dbc.Button(
                "Highlight New",
                id="new",
                n_clicks=0,
                color="secondary",
                className="position-absolute bottom-0 start-0 p-3",
            ),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-primary text-light rounded-3 mb-4  position-relative",
    style={"height": 400},
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
                dbc.Col(utility_grid),
                dbc.Col(utility_border),
                dbc.Col(utility_color),
                dbc.Col(utility_display),
                dbc.Col(utility_misc),
                dbc.Col(utility_opacity),
                dbc.Col(utility_position),
                dbc.Col(utility_spacing),
                dbc.Col(utility_text),
                dbc.Col(utility_flex),
                dbc.Col(dbc_components1),
                dbc.Col(dbc_components2),
                dbc.Col(plotly_links),
            ]
        ),
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
