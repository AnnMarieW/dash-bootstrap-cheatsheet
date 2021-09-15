"""
This is the card and content of the code snippets and preview content for

Utility:Display
"""


from dash import html
import dash_bootstrap_components as dbc

from utilities import make_link, make_listgroup_item


d_none_code = """
```python
Change screen size to see responsive content

html.Div("d-none", className="d-none")
html.Div("d-sm-none", className="d-sm-none")
html.Div("d-md-none", className="d-md-none")
html.Div("d-lg-none", className="d-lg-none")
html.Div("d-xl-none", className="d-xl-none")
html.Div("d-xxl-none", className="d-xxl-none")
```"""


d_none_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Div("d-none", className="d-none border bg-light m-1"),
        html.Div("d-sm-none", className="d-sm-none border bg-light m-1"),
        html.Div("d-md-none", className="d-md-none border bg-light m-1"),
        html.Div("d-lg-none", className="d-lg-none border bg-light m-1"),
        html.Div("d-xl-none", className="d-xl-none border bg-light m-1"),
        html.Div("d-xxl-none", className="d-xxl-none border bg-light m-1"),
    ]
)


d_inline_code = """
```python
Change screen size to see responsive content

html.Div("d-inline", className="d-inline")
html.Div("d-sm-inline", className="d-sm-inline")
html.Div("d-md-inline", className="d-md-inline")
html.Div("d-lg-inline", className="d-lg-inline")
html.Div("d-xl-inline", className="d-xl-inline")
html.Div("d-xxl-inline", className="d-xxl-inline")
```"""


d_inline_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Div("d-inline", className="d-inline border bg-light m-1"),
        html.Div("d-sm-inline", className="d-sm-inline border bg-light m-1"),
        html.Div("d-md-inline", className="d-md-inline border bg-light m-1"),
        html.Div("d-lg-inline", className="d-lg-inline border bg-light m-1"),
        html.Div("d-xl-inline", className="d-xl-inline border bg-light m-1"),
        html.Div("d-xxl-inline", className="d-xxl-inline border bg-light m-1"),
    ]
)


d_inline_block_code = """
```python
Change screen size to see responsive content

html.Div("d-inline-block", className="d-inline-block")
html.Div("d-sm-inline-block", className="d-sm-inline-block")
html.Div("d-md-inline-block", className="d-md-inline-block")
html.Div("d-lg-inline-block", className="d-lg-inline-block")
html.Div("d-xl-inline-block", className="d-xl-inline-block")
html.Div("d-xxl-inline-block", className="d-xxl-inline-block")
```"""


d_inline_block_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Div("d-inline-block", className="d-inline-block border bg-light m-1"),
        html.Div(
            "d-sm-inline-block", className="d-sm-inline-block border bg-light m-1"
        ),
        html.Div(
            "d-md-inline-block", className="d-md-inline-block border bg-light m-1"
        ),
        html.Div(
            "d-lg-inline-block", className="d-lg-inline-block border bg-light m-1"
        ),
        html.Div(
            "d-xl-inline-block", className="d-xl-inline-block border bg-light m-1"
        ),
        html.Div(
            "d-xxl-inline-block", className="d-xxl-inline-block border bg-light m-1"
        ),
    ]
)


d_block_code = """
```python
Change screen size to see responsive content

html.Span("d-block", className="d-block")
html.Span("d-sm-block", className="d-sm-block")
html.Span("d-md-block", className="d-md-block")
html.Span("d-lg-block", className="d-lg-block")
html.Span("d-xl-block", className="d-xl-block")
html.Span("d-xxl-block", className="d-xxl-block")
```"""


d_block_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Span("d-block", className="d-block border bg-light m-1"),
        html.Span("d-sm-block", className="d-sm-block border bg-light m-1"),
        html.Span("d-md-block", className="d-md-block border bg-light m-1"),
        html.Span("d-lg-block", className="d-lg-block border bg-light m-1"),
        html.Span("d-xl-block", className="d-xl-block border bg-light m-1"),
        html.Span("d-xxl-block", className="d-xxl-block border bg-light m-1"),
    ]
)


d_grid_code = """
```python
Change screen size to see responsive content

html.Span("d-grid", className="d-grid")
html.Span("d-sm-grid", className="d-sm-grid")
html.Span("d-md-grid", className="d-md-grid")
html.Span("d-lg-grid", className="d-lg-grid")
html.Span("d-xl-grid", className="d-xl-grid")
html.Span("d-xxl-grid", className="d-xxl-grid")
```"""


d_grid_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Span("d-grid", className="d-grid border bg-light m-1"),
        html.Span("d-sm-grid", className="d-sm-grid border bg-light m-1"),
        html.Span("d-md-grid", className="d-md-grid border bg-light m-1"),
        html.Span("d-lg-grid", className="d-lg-grid border bg-light m-1"),
        html.Span("d-xl-grid", className="d-xl-grid border bg-light m-1"),
        html.Span("d-xxl-grid", className="d-xxl-grid border bg-light m-1"),
    ]
)


d_flex_code = """
```python
Change screen size to see responsive content

html.Span("d-flex", className="d-flex")
html.Span("d-sm-flex", className="d-sm-flex")
html.Span("d-md-flex", className="d-md-flex")
html.Span("d-lg-flex", className="d-lg-flex")
html.Span("d-xl-flex", className="d-xl-flex")
html.Span("d-xxl-flex", className="d-xxl-flex")
```"""


d_flex_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Span("d-flex", className="d-flex border bg-light m-1"),
        html.Span("d-sm-flex", className="d-sm-flex border bg-light m-1"),
        html.Span("d-md-flex", className="d-md-flex border bg-light m-1"),
        html.Span("d-lg-flex", className="d-lg-flex border bg-light m-1"),
        html.Span("d-xl-flex", className="d-xl-flex border bg-light m-1"),
        html.Span("d-xxl-flex", className="d-xxl-flex border bg-light m-1"),
    ]
)


d_inline_flex_code = """
```python
Change screen size to see responsive content

html.Div("d-inline-flex", className="d-inline-flex")
html.Div("d-sm-inline-flex", className="d-sm-inline-flex")
html.Div("d-md-inline-flex", className="d-md-inline-flex")
html.Div("d-lg-inline-flex", className="d-lg-inline-flex")
html.Div("d-xl-inline-flex", className="d-xl-inline-flex")
html.Div("d-xxl-inline-flex", className="d-xxl-inline-flex")
```"""


d_inline_flex_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Div("d-inline-flex", className="d-inline-flex border bg-light m-1"),
        html.Div("d-sm-inline-flex", className="d-sm-inline-flex border bg-light m-1"),
        html.Div("d-md-inline-flex", className="d-md-inline-flex border bg-light m-1"),
        html.Div("d-lg-inline-flex", className="d-lg-inline-flex border bg-light m-1"),
        html.Div("d-xl-inline-flex", className="d-xl-inline-flex border bg-light m-1"),
        html.Div(
            "d-xxl-inline-flex", className="d-xxl-inline-flex border bg-light m-1"
        ),
    ]
)


d_print_display_code = """
```python
Change screen size to see responsive content

html.Div("d-print-none", className="d-print-none")
html.Div("d-print-inline", className="d-print-inline")
html.Div("d-print-inline-block", className="d-print-inline-block")
html.Div("d-print-block", className="d-print-block")
html.Div("d-print-grid", className="d-print-grid")
html.Div("d-print-flex", className="d-print-flex")
html.Div("d-print-inline-flex", className="d-print-inline-flex")
```"""


d_print_display_preview = html.Div(
    [
        html.P("Change screen size to see responsive content"),
        html.Div("d-print-none", className="d-print-none border bg-light m-1"),
        html.Div("d-print-inline", className="d-print-inline border bg-light m-1"),
        html.Div(
            "d-print-inline-block", className="d-print-inline-block border bg-light m-1"
        ),
        html.Div("d-print-block", className="d-print-block border bg-light m-1"),
        html.Div("d-print-grid", className="d-print-grid border bg-light m-1"),
        html.Div("d-print-flex", className="d-print-flex border bg-light m-1"),
        html.Div(
            "d-print-inline-flex", className="d-print-inline-flex border bg-light m-1"
        ),
    ]
)


utility_display = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Display"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/display/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("d-*-none"),
                make_listgroup_item("d-*-inline"),
                make_listgroup_item("d-*-inline-block"),
                make_listgroup_item("d-*-block"),
                make_listgroup_item("d-*-grid"),
                make_listgroup_item("d-*-flex"),
                make_listgroup_item("d-*-inline-flex"),
                make_listgroup_item("d-print-{display}"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
