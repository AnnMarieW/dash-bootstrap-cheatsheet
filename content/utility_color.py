"""
This is the card and content of the code snippets and preview content for

Utility:Color
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


text_color_code = """
```
html.P("text-primary", className="text-primary")
html.P("text-secondary", className="text-secondary")
html.P("text-success", className="text-success")
html.P("text-danger", className="text-danger")
html.P("text-warning", className="text-warning")
html.P("text-info", className="text-info")
html.P("text-light", className="text-light")
html.P("text-dark", className="text-dark")
```"""

text_color_preview = html.Div(
    [
        html.P("text-primary", className="text-primary"),
        html.P("text-secondary", className="text-secondary"),
        html.P("text-success", className="text-success"),
        html.P("text-danger", className="text-danger"),
        html.P("text-warning", className="text-warning"),
        html.P("text-info", className="text-info"),
        html.P("text-light", className="text-light bg-dark"),
        html.P("text-dark", className="text-dark"),
        html.P("text-white", className="text-white bg-dark"),
        html.P("text-black", className="text-black"),
        html.P("text-body", className="text-body"),
        html.P("text-muted", className="text-muted"),
    ]
)

text_body_code = """
```
html.P("text-body", className="text-body")
```"""


text_body_preview = html.Div([html.P("text-body", className="text-body"),])

text_muted_code = """
```
html.P("text-muted", className="text-muted")
html.P("default text color")
```"""


text_muted_preview = html.Div(
    [html.P("text-muted", className="text-muted"), html.P("default text color")]
)


text_white_50_code = """
Note: Deprecated use "opacity-*" instead
```
html.P("text-white-50", className="text-white-50")
```"""


text_white_50_preview = html.Div(
    [
        html.P("text-white", className="text-white bg-dark"),
        html.P("text-white-50", className="text-white-50 bg-dark"),
    ]
)

text_black_50_code = """

Note: Deprecated use "opacity-*" instead
```
html.P("text-black-50", className="text-black-50")
```"""


text_black_50_preview = html.Div(
    [
        html.P("text-black", className="text-black bg-white"),
        html.P("text-black-50", className="text-black-50 bg-white"),
    ]
)


# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
utility_color = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Color"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/colors/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "text-{color}",
                    "{primary|secondary|success|danger|warning|info|light|dark|white}",
                ),
                make_listgroup_item("text-body", "Text color used in the body"),
                make_listgroup_item("text-muted", "Text color muted"),
                make_listgroup_item("text-black-50", "deprecated - use opacity"),
                make_listgroup_item("text-white-50", "deprecated - use opacity"),

            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
