"""
This is the card and content of the code snippets and preview content for

Utility:Background
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


bg_color_code = """
```
html.P("bg-primary", className="bg-primary")
html.P("bg-secondary", className="bg-secondary")
html.P("bg-success", className="bg-success")
html.P("bg-danger", className="bg-danger")
html.P("bg-warning", className="bg-warning")
html.P("bg-info", className="bg-info")
html.P("bg-light", className="bg-light")
html.P("bg-dark", className="bg-dark")

```"""


bg_color_preview = html.Div(
    [
        html.P("bg-primary", className="bg-primary"),
        html.P("bg-secondary", className="bg-secondary"),
        html.P("bg-success", className="bg-success"),
        html.P("bg-danger", className="bg-danger"),
        html.P("bg-warning", className="bg-warning"),
        html.P("bg-info", className="bg-info"),
        html.P("bg-light", className="bg-light"),
        html.P("bg-dark", className="bg-dark text-white"),
    ]
)


bg_transparent_code = """
```
html.P("bg-transparent", className="bg-transparent")
```"""


bg_transparent_preview = html.Div(
    [html.P("bg-transparent", className="bg-transparent"),]
)


bg_gradient_code = """
```
html.P("bg-primary", className="bg-primary text-white"),
html.P("bg-primary bg-gradient", className="bg-primary bg-gradient text-white")
```"""


bg_gradient_preview = html.Div(
    [
        html.P("bg-primary", className="bg-primary text-white", style={"height": 100}),
        html.P(
            "bg-primary bg-gradient",
            className="bg-primary bg-gradient text-white",
            style={"height": 100},
        ),
    ]
)


bg_opacity_code = """
```
html.Div("default", className="p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("75%", className="bg-opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded")
html.Div("50%", className="bg-opacity-50 p-2 m-1 bg-primary text-dark fw-bold rounded")
html.Div("25%", className="bg-opacity-25 p-2 m-1 bg-primary text-dark fw-bold rounded")
html.Div("10%", className="bg-opacity-10 p-2 m-1 bg-primary text-dark fw-bold rounded")

```"""

bg_opacity_preview = html.Div(
    [
        html.Div("default", className="p-2 m-1 bg-primary text-light fw-bold rounded"),
        html.Div(
            "75%",
            className="bg-opacity-75 p-2 m-1 bg-primary text-light fw-bold rounded",
        ),
        html.Div(
            "50%",
            className="bg-opacity-50 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
        html.Div(
            "25%",
            className="bg-opacity-25 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
        html.Div(
            "10%",
            className="bg-opacity-10 p-2 m-1 bg-primary text-dark fw-bold rounded",
        ),
    ]
)



# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
utility_background = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Background"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/background/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "bg-{color}",
                    "background {primary|secondary|success|danger|warning|info|light|dark|white}",
                ),
                make_listgroup_item("bg-transparent", "background transparent"),
                make_listgroup_item("bg-gradient", "background gradient"),
            ],
            flush=True,
            className="border-0",
        ),
        make_listgroup_item(
            "bg-opacity-{val}", "background opacity {100|75|50|25|0}"
        ),
    ],
    className="class-card",
)
