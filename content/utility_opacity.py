"""
This is the card and content of the code snippets and preview content for

Utility:Opacity
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


opacity_code = """
```
html.Div("100%", className="opacity-100 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("75%", className="opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("50%", className="opacity-50 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("25%", className="opacity-25 p-2 m-1 bg-primary text-light fw-bold rounded")

```"""

opacity_preview = html.Div(
    [
        html.Div(
            "100%",
            className="opacity-100 p-2 m-1 bg-primary text-light fw-bold rounded",
        ),
        html.Div(
            "75%", className="opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded"
        ),
        html.Div(
            "50%", className="opacity-50 p-2 m-1 bg-primary text-light fw-bold rounded"
        ),
        html.Div(
            "25%", className="opacity-25 p-2 m-1 bg-primary text-light fw-bold rounded"
        ),
    ]
)


bg_opacity_code = """
```
html.Div("default", className="p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("75%", className="opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("50%", className="opacity-50 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("25%", className="opacity-25 p-2 m-1 bg-primary text-light fw-bold rounded")

```"""

bg_opacity_preview = html.Div(
    [
        html.Div("default", className="p-2 m-1 bg-primary text-light fw-bold rounded"),
        html.Div(
            "75%",
            className="bg_opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded",
        ),
        html.Div(
            "50%",
            className="bg_opacity-50 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
        html.Div(
            "25%",
            className="bg_opacity-25 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
        html.Div(
            "10%",
            className="bg_opacity-10 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
    ]
)


text_opacity_code = """
```
html.Div("default", className="text-primary p-2")
html.Div("75% opacity", className="opacity-75 text-primary p-2")
html.Div("50% opacity", className="opacity-50 text-primary p-2")
html.Div("25% opacity", className="opacity-25 text-primary p-2")

```"""

text_opacity_preview = html.Div(
    [
        html.Div("default", className="text-primary p-2"),
        html.Div("75% opacity", className="opacity-75 text-primary p-2"),
        html.Div("50% opacity", className="opacity-50 text-primary p-2"),
        html.Div("25% opacity", className="opacity-25 text-primary p-2"),
    ]
)

utility_opacity = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Opacity"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/opacity/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("opacity-{value}", "opacity of elements"),
                make_listgroup_item("bg-opacity-{value}", "background opacity {100|75|50|25|0}"),
                make_listgroup_item("text-opacity-{value}","text opacity {100|75|50|25|0}"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
