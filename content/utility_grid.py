"""
This is the card and content of the code snippets and preview content for

Utility:Grid
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item, dbc_url


def make_row(className):
    return dbc.Row(
        [
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
        ],
        className=className + " my-2 border border-danger",
    )


gx_size_code = """
```
Note: To help show the spacing:     
    - The Container has className="bg-secondary"
    - Each Row also has className=" my-2 border border-danger"
    - The Col content has className="bg-light"
 

def make_row(className):
    return dbc.Row(
        [
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
        ],
        className=className + " my-2 border border-danger",
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
```
Note: To help show the spacing:     
    - The Container has className="bg-secondary"
    - Each Row also has className=" my-2 border border-danger"
    - The Col content has className="bg-light"


def make_row(className):
    return dbc.Row(
        [
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
        ],
        className=className + " my-2 border border-danger",
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
```
Note: To help show the spacing:     
    - The Container has className="bg-secondary"
    - Each Row also has className=" my-2 border border-danger"
    - The Col content has className="bg-light"


def make_row(className):
    return dbc.Row(
        [
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
            dbc.Col(html.Div(className, className="bg-light")),
        ],
        className=className + " my-2 border border-danger",
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
```
Gutters can be used for responsive cases with the help of 
gx-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 

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
            className="gx-2 gx-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)


gy_dev_size_code = """
```
Gutters can be used for responsive cases with the help of 
gy-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 

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
            className="gy-2 gy-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)


g_dev_size_code = """
```
Gutters can be used for responsive cases with the help of 
g-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 

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
            className="g-2 g-xl-5 m-2 border border-danger"
        ),
    ],
    fluid=True
)


utility_grid = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Grid"),
                make_link("https://getbootstrap.com/docs/5.1/layout/gutters/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                dcc.Markdown(
                    f"For Grid components see the *dash-bootstrap-components* [Layout section]({dbc_url}/layout/)",
                    className="p-2",
                ),
                make_listgroup_item("gx-{size}"),
                make_listgroup_item("gx-*-{size}"),
                make_listgroup_item("gy-{size}"),
                make_listgroup_item("gy-*-{size}"),
                make_listgroup_item("g-{size}"),
                make_listgroup_item("g-*-{size}"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
