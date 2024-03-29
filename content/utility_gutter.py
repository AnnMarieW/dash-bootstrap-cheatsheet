"""
This is the card and content of the code snippets and preview content for

Utility:Grid
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


def make_row(example_class_name):
    return dbc.Row(
        [
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
        ],
        className=example_class_name + " my-2 border border-danger",
    )


gx_size_code = """

Gutters are the padding between  columns.

Note: To help show the spacing:     
- The `Container` has `className="bg-secondary"`   
- Each `Row` also has `className=" my-2 border border-danger"`   
- The `Col` content has `className="bg-light"`
 
```
def make_row(example_class_name):
    return dbc.Row(
        [
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
        ],
        className=example_class_name + " my-2 border border-danger",
    )
    
gx_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("gx-0"),
        make_row("gx-1"),
        make_row("gx-2"),
        make_row("gx-3"),
        make_row("gx-4"),
        make_row("gx-5"),
    ],
    fluid=True,
    className="bg-secondary",
)
```"""

gx_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("gx-0"),
        make_row("gx-1"),
        make_row("gx-2"),
        make_row("gx-3"),
        make_row("gx-4"),
        make_row("gx-5"),
    ],
    fluid=True,
    className="bg-secondary",
)

gy_size_code = """

Gutters are the padding between  columns.
Note: To help show the spacing:     
- The `Container` has `className="bg-secondary"`   
- Each `Row` also has `className=" my-2 border border-danger"`   
- The `Col` content has `className="bg-light"`
 
```
def make_row(example_class_name):
    return dbc.Row(
        [
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
        ],
        className=example_class_name + " my-2 border border-danger",
    )

gy_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("gy-0"),
        make_row("gy-1"),
        make_row("gy-2"),
        make_row("gy-3"),
        make_row("gy-4"),
        make_row("gy-5"),
    ],
    fluid=True,
    className="bg-secondary",
)
```"""

gy_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("gy-0"),
        make_row("gy-1"),
        make_row("gy-2"),
        make_row("gy-3"),
        make_row("gy-4"),
        make_row("gy-5"),
    ],
    fluid=True,
    className="bg-secondary",
)

g_size_code = """

Gutters are the padding between  columns.
Note: To help show the spacing:     
- The `Container` has `className="bg-secondary"`   
- Each `Row` also has `className=" my-2 border border-danger"`   
- The `Col` content has `className="bg-light"`
 
```

def make_row(example_class_name):
    return dbc.Row(
        [
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
            dbc.Col(html.Div(example_class_name, className="bg-light")),
        ],
        className=example_class_name + " my-2 border border-danger",
    )

g_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("g-0"),
        make_row("g-1"),
        make_row("g-2"),
        make_row("g-3"),
        make_row("g-4"),
        make_row("g-5"),
    ],
    fluid=True,
    className="bg-secondary",
)
```"""

g_size_preview = dbc.Container(
    [
        make_row("default"),
        make_row("g-0"),
        make_row("g-1"),
        make_row("g-2"),
        make_row("g-3"),
        make_row("g-4"),
        make_row("g-5"),
    ],
    fluid=True,
    className="bg-secondary",
)

gx_dev_size_code = """

Gutters are the padding between  columns.
Make responsive layouts by setting different gutters at breakpoints for device or viewport sizes:     
gx-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 
```
gx_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="gx-2 gx-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)
```"""

gx_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="gx-2 gx-xl-5 m-2 border border-danger",
        ),
    ],
    fluid=True,
)


gy_dev_size_code = """

Gutters are the padding between  columns.
Make responsive layouts by setting different gutters at breakpoints for device or viewport sizes:  
gy-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 
```
gy_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="gy-2 gy-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)
```"""

gy_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="gy-2 gy-xl-5 m-2 border border-danger",
        ),
    ],
    fluid=True,
)


g_dev_size_code = """

Gutters are the padding between  columns.
Make responsive layouts by setting different gutters at breakpoints for device or viewport sizes:  
g-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 
```
g_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="g-2 g-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)
```"""

g_dev_size_preview = dbc.Container(
    [
        html.H5("Change the screen size to see how the gutters change"),
        dbc.Row(
            [
                dbc.Col(html.Div("col1", className="border bg-light")),
                dbc.Col(html.Div("col2", className=" border bg-light")),
            ],
            className="g-2 g-xl-5 m-2 border border-danger",
        ),
    ],
    fluid=True,
)


# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
utility_gutter = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Gutter"),
                make_link("https://getbootstrap.com/docs/5.1/layout/gutters/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("gx-{size}", "Gutter horizontal"),
                make_listgroup_item("gx-*-{size}", "Gutter horizontal w breakpoints"),
                make_listgroup_item("gy-{size}", "Gutter vertical"),
                make_listgroup_item("gy-*-{size}", "Gutter vertical w breakpoints"),
                make_listgroup_item("g-{size}", "Gutter horizontal & vertical"),
                make_listgroup_item(
                    "g-*-{size}", "Gutter horizontal & vertical w breakpoints"
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
