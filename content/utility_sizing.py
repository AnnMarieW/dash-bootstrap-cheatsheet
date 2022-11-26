"""
This is the card and content of the code snippets and preview content for

Utility Sizing
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item



w_option_code = """
```
html.Div("Width 25%", className="w-25 p-3 bg-light border")
html.Div("Width 50%", className="w-50 p-3 bg-light border")
html.Div("Width 75%", className="w-75 p-3 bg-light border")
html.Div("Width 100%", className="w-100 p-3 bg-light border")
html.Div("Width auto", className="w-auto p-3 bg-light border")
```"""

w_option_preview = html.Div(
    [
        html.Div("Width 25%", className="w-25 p-3 bg-light border"),
        html.Div("Width 50%", className="w-50 p-3 bg-light border"),
        html.Div("Width 75%", className="w-75 p-3 bg-light border"),
        html.Div("Width 100%", className="w-100 p-3 bg-light border"),
        html.Div("Width auto", className="w-auto p-3 bg-light border"),
    ]
)


h_option_code = """
```
html.Div(
    [
        html.Div("Height 25%", className="h-25 d-inline-block bg-light border", style={"width":120}),
        html.Div("Height 50%", className="h-50 d-inline-block bg-light border", style={"width":120}),
        html.Div("Height 75%", className="h-75 d-inline-block bg-light border", style={"width":120}),
        html.Div("Height 100%", className="h-100 d-inline-block bg-light border", style={"width":120}),
        html.Div("Height auto", className="h-auto d-inline-block bg-light border", style={"width":120}),
    ],className="border", style={"height":100}
)
```"""

h_option_preview = html.Div(
    [
        html.Div(
            "Height 25%",
            className="h-25 d-inline-block bg-light border",
            style={"width": 120},
        ),
        html.Div(
            "Height 50%",
            className="h-50 d-inline-block bg-light border",
            style={"width": 120},
        ),
        html.Div(
            "Height 75%",
            className="h-75 d-inline-block bg-light border",
            style={"width": 120},
        ),
        html.Div(
            "Height 100%",
            className="h-100 d-inline-block bg-light border",
            style={"width": 120},
        ),
        html.Div(
            "Height auto",
            className="h-auto d-inline-block bg-light border",
            style={"width": 120},
        ),
    ],
    className="border",
    style={"height": 100},
)


mw_100_code = """

This is commonly used with images
```
html.Div(
    html.Div("max width 100%", className="mh-100 bg-info", style={"height": 100}),
    style={"height": 200},
    className="bg-light border"
)

```"""

mw_100_preview = html.Div(
    html.Div("max width 100%", className="mh-100 bg-info", style={"height": 100}),
    style={"height": 200},
    className="bg-light border",
)


mh_100_code = """

This is commonly used with images
```
html.Div(
    html.Div("max height 100%", className="mh-100 bg-info", style={"width": 100, "height": 200}),
    style={"height": 100},
    className="bg-light border"
)

```"""

mh_100_preview = html.Div(
    html.Div(
        "max height 100%",
        className="mh-100 bg-info",
        style={"width": 100, "height": 200},
    ),
    style={"height": 100},
    className="bg-light border",
)

viewport_code = """

Click full screen button  or scroll down to see preview
```
html.Div("Min-width 100vw", className="min-vw-100 bg-light mb-3 border")
html.Div("Min-height 100vh", className="min-vh-100 bg-light mb-3 border")
html.Div("Width 100vw", className="vw-100 bg-light mb-3 border")
html.Div("Height 100vh", className="vh-100 bg-light border")
```"""

viewport_preview = html.Div(
    [
        html.Div("Min-width 100vw", className="min-vw-100 bg-light mb-3 border"),
        html.Div("Min-height 100vh", className="min-vh-100 bg-light mb-3 border"),
        html.Div("Width 100vw", className="vw-100 bg-light mb-3 border"),
        html.Div("Height 100vh", className="vh-100 bg-light border"),
    ]
)


# ----------------------------------------------------------

utility_sizing = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility Sizing"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/sizing/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "w-{option}", "width relative to parent {25|50|75|100|auto}"
                ),
                make_listgroup_item(
                    "h-{option}", "height relative to parent {25|50|75|100|auto}"
                ),
                make_listgroup_item(
                    "mw-100", "max width relative to parent {25|50|75|100|auto}"
                ),
                make_listgroup_item(
                    "mh-100", "max height relative to parent {25|50|75|100|auto}"
                ),
                make_listgroup_item(
                    "viewport",
                    "relative to the viewport {min-vw-100|min-vh-100|vw-100|vh-100}",
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
