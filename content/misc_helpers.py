"""
This is the card and content of the code snippets and preview content for

Misc & Helpers
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


visible_code = """
```
html.Div("...", className="visible")
html.Div("...", className="invisible")
```"""

visible_preview = html.Div(
    [html.Div("...", className="visible"), html.Div("...", className="invisible")]
)

fixed_bottom_code = """
```
html.Div("fixed bottom", className="fixed-bottom bg-primary text-white")
```"""

fixed_bottom_preview = html.Div(
    [
        "See bottom of the screen",
        html.Div("fixed bottom", className="fixed-bottom bg-primary text-white"),
    ]
)


fixed_top_code = """
```
html.Div("fixed top", className="fixed-top bg-primary text-white")
```"""

fixed_top_preview = html.Div(
    [
        "Look at top of screen",
        html.Div("fixed top", className="fixed-top bg-primary text-white"),
    ]
)


sticky_top_code = """
Position an element at the top of the viewport, but only after you scroll past it.
Not supported in all browsers
Make responsive layouts by setting different gutters at breakpoints for device or viewport sizes:     
sticky-{sm|md|lg|xl|xxl}-top

```
html.Div("sticky top", className="sticky-top bg-primary text-white")
```"""

sticky_top_preview = html.Div(
    "sticky top", className="sticky-top bg-primary text-white"
)


img_fluid_code = """
```
html.Img(src=..., className="img-fluid"
```"""

img = "https://user-images.githubusercontent.com/72614349/133930947-1c95d44e-a6a5-44fd-a66d-258baddb44a4.png"

img_fluid_preview = html.Div(
    [
        "Change the screen size to see that the image scales in parent container",
        html.Img(src=img, className="img-fluid"),
    ]
)

img_thumbnail_code = """
```
html.Div(html.Img(src=..., className="img-thumbnail"
```"""
img_thumbnail_preview = html.Img(src=img, className="img-thumbnail img-fluid")


# ----------------------------------------------------------

misc_helpers = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Misc & Helpers"),
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
                make_listgroup_item("shadow-{option}", "box shadows {none|sm|lg}"),
                make_listgroup_item("visible/invisible"),
                make_listgroup_item("fixed-top", "element fixed to top of viewport",),
                make_listgroup_item(
                    "fixed-bottom", "element fixed to bottom of viewport",
                ),
                make_listgroup_item(
                    "sticky-*-top",
                    "fixed to top of viewport but only after scrolling past it",
                ),
                make_listgroup_item("img-fluid", "scale image with screen size"),
                make_listgroup_item("img-thumbnail", "Add frame to image"),
                #  make_listgroup_item("ratio", "set aspect ratio")
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
