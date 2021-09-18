"""
This is the card and content of the code snippets and preview content for

Utility:Misc
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


user_select_code = """
```
html.P("This paragraph will be entirely selected when clicked by the user", className="user-select-all")
html.P("This paragraph has default select behaviour")
html.P("This paragraph will not be selectable when clicked by the user", className="user-select-none")
```"""

user_select_preview = html.Div(
    [
        html.P(
            "This paragraph will be entirely selected when clicked by the user",
            className="user-select-all",
        ),
        html.P("This paragraph has default select behaviour"),
        html.P(
            "This paragraph will not be selectable when clicked by the user",
            className="user-select-none",
        ),
    ]
)

pointer_code = """
```
html.P([html.A("This link ", href="#", className="pe-none"), "can not be clicked"])
    
html.P(
    [
        html.A("This link ", href="#", className="pe-auto"),
        "can be clicked (default behavior)",
    ]
)
html.P(
    [
        html.A("This link ", href="#"),
        "can not be clicked because the",
        html.Code(" pointer-events "),
        "property is inherited from it's parent. However, ",
        html.A("This link ", href="#", className="pe-auto"),
        "has a",
        html.Code(" pe-auto "),
        "class and can be clicked",
    ],
    className="pe-none",
)


```"""

pointer_preview = html.Div(
    [
        html.P(
            [html.A("This link ", href="#", className="pe-none"), "can not be clicked"]
        ),
        html.P(
            [
                html.A("This link ", href="#", className="pe-auto"),
                "can be clicked (default behavior)",
            ]
        ),
        html.P(
            [
                html.A("This link ", href="#"),
                "can not be clicked because the",
                html.Code(" pointer-events "),
                "property is inherited from it's parent. However, ",
                html.A("This link ", href="#", className="pe-auto"),
                "has a",
                html.Code(" pe-auto "),
                "class and can be clicked",
            ],
            className="pe-none",
        ),
    ]
)

shadow_code = """
```
html.Div("No shadow", className="shadow-none p-3 mb-5 bg-light rounded")
html.Div("Small shadow", className="shadow-sm p-3 mb-5 bg-white rounded")
html.Div("Regular shadow", className="shadow p-3 mb-5 bg-white rounded")
html.Div("Larger shadow", className="shadow-lg p-3 mb-5 bg-white rounded")

```"""

shadow_preview = html.Div(
    [
        html.Div("No shadow", className="shadow-none p-3 mb-5 bg-light rounded"),
        html.Div("Small shadow", className="shadow-sm p-3 mb-5 bg-white rounded"),
        html.Div("Regular shadow", className="shadow p-3 mb-5 bg-white rounded"),
        html.Div("Larger shadow", className="shadow-lg p-3 mb-5 bg-white rounded"),
    ]
)

overflow_code = """

overflow-{auto|hidden|visible|scroll}
```
html.Div(
    [
        html.Div(
            'This is an example of using "overflow-auto" on an element with set width and height dimensions. By design, this content will vertically scroll.',
            className="overflow-auto p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-hidden" on an element with set width and height dimensions. ',
            className="overflow-hidden p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-visible" on an element with set width and height dimensions. ',
            className="overflow-visible p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-scroll" on an element with set width and height dimensions. ',
            className="overflow-scroll p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
    ],
    className="d-sm-flex d-md-block d-xxl-flex"
)
```"""

overflow_preview = html.Div(
    [
        html.Div(
            'This is an example of using "overflow-auto" on an element with set width and height dimensions. By design, this content will vertically scroll.',
            className="overflow-auto p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-hidden" on an element with set width and height dimensions. ',
            className="overflow-hidden p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-visible" on an element with set width and height dimensions. ',
            className="overflow-visible p-3 mb-3 me-sm-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
        html.Div(
            'This is an example of using "overflow-scroll" on an element with set width and height dimensions. ',
            className="overflow-scroll p-3 bg-light",
            style={"maxWidth": 260, "maxHeight": 100},
        ),
    ],
    className="d-sm-flex d-md-block d-xxl-flex",
)


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

visible_code = """
```
html.Div("...", className="visible")
html.Div("...", className="invisible")
```"""

visible_preview = html.Div(
    [html.Div("...", className="visible"), html.Div("...", className="invisible")]
)

utility_misc = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Misc"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/interactions/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "user-select-{option}", "how content is selected {all|auto|none}"
                ),
                make_listgroup_item(
                    "pe-{option} (pointer)", "whether links can be clicked"
                ),
                make_listgroup_item(
                    "overflow-{option}",
                    "how content overflows an element {auto|hidden|visible|scroll}",
                ),
                make_listgroup_item(
                    "shadow-{option}", "box shadows {none|sm|lg}"
                ),
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
                make_listgroup_item("visible/invisible"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
