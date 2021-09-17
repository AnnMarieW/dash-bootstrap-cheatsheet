"""
This is the card and content of the code snippets and preview content for

Utility:Border
"""


from dash import html
import dash_bootstrap_components as dbc

from utilities import make_link, make_listgroup_item

border_code = """
```
html.Span(className="border")
```"""
border_preview = html.Div(html.Span(className="border"), className="border-utils")


border_direction_code = """
```python
html.Span(className="border-top")
html.Span(className="border-end")
html.Span(className="border-bottom")
html.Span(className="border-start")
```"""


border_direction_preview = html.Div(
    [
        html.Span(className="border-top"),
        html.Span(className="border-end"),
        html.Span(className="border-bottom"),
        html.Span(className="border-start"),
    ],
    className="border-utils",
)


border_0_code = """
```
html.Span(className="border-0")
```"""
border_0_preview = html.Div(html.Span(className="border-0"), className="border-utils")


border_direction_0_code = """
```python
html.Span(className=" border border-top-0 ")
html.Span(className="border border-end-0")
html.Span(className="border border-bottom-0")
html.Span(className="border border-start-0")
"""


border_direction_0_preview = html.Div(
    [
        html.Span(className="border border-top-0"),
        html.Span(className="border border-end-0"),
        html.Span(className="border border-bottom-0"),
        html.Span(className="border border-start-0"),
    ],
    className="border-utils",
)

border_color_code = """
```
html.Span(className="border border-primary")
html.Span(className="border border-secondary")
html.Span(className="border border-success")
html.Span(className="border border-danger")
html.Span(className="border border-warning")
html.Span(className="border border-info")
html.Span(className="border border-light")
html.Span(className="border border-dark")
html.Span(className="border border-white")
```"""
border_color_preview = html.Div(
    [
        html.Span(className="border border-primary"),
        html.Span(className="border border-secondary"),
        html.Span(className="border border-success"),
        html.Span(className="border border-danger"),
        html.Span(className="border border-warning"),
        html.Span(className="border border-info"),
        html.Span(className="border border-light"),
        html.Span(className="border border-dark"),
        html.Span(className="border border-white"),
    ],
    className="border-utils",
)

border_size_code = """
```
html.Span(className="border border-1")
html.Span(className="border border-2")
html.Span(className="border border-3")
html.Span(className="border border-4")
html.Span(className="border border-5")
```"""
border_size_preview = html.Div(
    [
        html.Span(className="border border-1"),
        html.Span(className="border border-2"),
        html.Span(className="border border-3"),
        html.Span(className="border border-4"),
        html.Span(className="border border-5"),
    ],
    className="border-utils",
)

border_rounded_code = """
```
html.Span(className="border rounded")
```"""
border_rounded_preview = html.Div(
    [html.Span(className="border rounded"),], className="border-utils"
)


border_rounded_corner_code = """
```
html.Span(className="border rounded-top")
html.Span(className="border rounded-end")
html.Span(className="border rounded-bottom")
html.Span(className="border rounded-start")
html.Span(className="border rounded-circle")
html.Span(className="border rounded-pill")
```"""
border_rounded_corner_preview = html.Div(
    [
        html.Span(className="border rounded-top"),
        html.Span(className="border rounded-end"),
        html.Span(className="border rounded-bottom"),
        html.Span(className="border rounded-start"),
        html.Span(className="border rounded-circle"),
        html.Span(className="pill border rounded-pill"),
    ],
    className="border-utils",
)


border_rounded_size_code = """
```
html.Span(className="border rounded-0")
html.Span(className="border rounded-1")
html.Span(className="border rounded-2")
html.Span(className="border rounded-3")
```"""
border_rounded_size_preview = html.Div(
    [
        html.Span(className="border rounded-0"),
        html.Span(className="border rounded-1"),
        html.Span(className="border rounded-2"),
        html.Span(className="border rounded-3"),
    ],
    className="border-utils",
)


utility_border = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Border"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/borders/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("border", "border all sides"),
                make_listgroup_item("border-{direction}", "border on {top|end|bottom|start}"),
                make_listgroup_item("border-0", "no border"),
                make_listgroup_item("border-{direction}-0", "no border {top|end|bottom|start} "),
                make_listgroup_item("border-{color}", "{primary|secondary|success|danger|warning|info|light|dark|white}"),
                make_listgroup_item("border-{size}", "border width {1|2|3|4|5}"),
                make_listgroup_item("rounded", "border radius all corners"),
                make_listgroup_item("rounded-{corner}", " radius at {top|end|bottom|start|circle|pill}"),
                make_listgroup_item("rounded-{size}", "border radius size {0|1|2|3}"
),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
