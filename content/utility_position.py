"""
This is the card and content of the code snippets and preview content for

Utility:Position
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


float_code = """
```
float can be used for responsive cases with the help of 
float-{sm|md|lg|xl|xxl}-{start|end|none}
For example float-sm-start

html.Div("Float start on all viewport sizes", className="float-start")
html.Br()
html.Div("Float end on all viewport sizes", className="float-end")
html.Br()
html.Div("Don't float on all viewport sizes", className="float-none")

```"""

float_preview = html.Div(
    [
        html.Div("Float start on all viewport sizes", className="float-start"),
        html.Br(),
        html.Div("Float end on all viewport sizes", className="float-end"),
        html.Br(),
        html.Div("Don't float on all viewport sizes", className="float-none"),
    ]
)


position_code = """
```
These positioning classes are not responsive.

html.Div("position-static", className="position-static")
html.Div("position-relative", className="position-relative")
html.Div("position-absolute", className="position-absolute")
html.Div("position-fixed", className="position-fixed")
html.Div("position-sticky", className="position-sticky")
```"""

position_preview = html.Div(
    [
        html.Div("position-static", className="position-static"),
        html.Div("position-relative", className="position-relative"),
        html.Div("position-absolute", className="position-absolute"),
        html.Div("position-fixed", className="position-fixed"),
        html.Div("position-sticky", className="position-sticky"),
    ]
)


direction_position_code = """
```
html.Div(
    [
        html.Div(className="position-absolute top-0 start-0"),
        html.Div(className="position-absolute top-0 end-0"),
        html.Div(className="position-absolute top-50 start-50"),
        html.Div(className="position-absolute bottom-50 end-50"),
        html.Div(className="position-absolute bottom-0 start-0"),
        html.Div(className="position-absolute bottom-0 end-0"),
    ],
    className="position-relative"
)
```"""

direction_position_preview = html.Div(
    [
        html.Div(className="position-absolute top-0 start-0 sm-square"),
        html.Div(className="position-absolute top-0 end-0 sm-square"),
        html.Div(className="position-absolute top-50 start-50 sm-square"),
        html.Div(className="position-absolute bottom-50 end-50 sm-square"),
        html.Div(className="position-absolute bottom-0 start-0 sm-square"),
        html.Div(className="position-absolute bottom-0 end-0 sm-square"),
    ],
    className="position-relative border", style={"height":175}
)


translate_middle_code = """
```
html.Div(
    [
        html.Div(className="position-absolute top-0 start-0 translate-middle"),
        html.Div(className="position-absolute top-0 start-50 translate-middle"),
        html.Div(className="position-absolute top-0 start-100 translate-middle"),
        html.Div(className="position-absolute top-50 start-0 translate-middle"),
        html.Div(className="position-absolute top-50 start-50 translate-middle"),
        html.Div(className="position-absolute top-50 start-100 translate-middle"),
        html.Div(className="position-absolute top-100 start-0 translate-middle"),
        html.Div(className="position-absolute top-100 start-50 translate-middle"),
        html.Div(className="position-absolute top-100 start-100 translate-middle"),
    ],
    className="position-relative"
)
```"""

translate_middle_preview = html.Div(
    [
        html.Div(className="position-absolute top-0 start-0 translate-middle sm-square"),
        html.Div(className="position-absolute top-0 start-50 translate-middle sm-square"),
        html.Div(className="position-absolute top-0 start-100 translate-middle sm-square"),
        html.Div(className="position-absolute top-50 start-0 translate-middle sm-square"),
        html.Div(className="position-absolute top-50 start-50 translate-middle sm-square"),
        html.Div(className="position-absolute top-50 start-100 translate-middle sm-square"),
        html.Div(className="position-absolute top-100 start-0 translate-middle sm-square"),
        html.Div(className="position-absolute top-100 start-50 translate-middle sm-square"),
        html.Div(className="position-absolute top-100 start-100 translate-middle sm-square"),
    ],
    className="position-relative border", style={"height":175}
)


translate_middle_direction_code = """
```
html.Div(
    [
        html.Div(className="position-absolute top-0 start-0"),
        html.Div(className="position-absolute top-0 start-50 translate-middle-x"),
        html.Div(className="position-absolute top-0 end-0"),
        html.Div(className="position-absolute top-50 start-0 translate-middle-y"),
        html.Div(className="position-absolute top-50 start-50 translate-middle"),
        html.Div(className="position-absolute top-50 end-0 translate-middle-y"),
        html.Div(className="position-absolute bottom-0 start-0"),
        html.Div(className="position-absolute bottom-0 start-50 translate-middle-x"),
        html.Div(className="position-absolute bottom-0 end-0"),
    ],
    className="position-relative"
)
```"""

translate_middle_direction_preview = html.Div(
    [
        html.Div(className="position-absolute top-0 start-0 sm-square"),
        html.Div(className="position-absolute top-0 start-50 translate-middle-x sm-square"),
        html.Div(className="position-absolute top-0 end-0 sm-square"),
        html.Div(className="position-absolute top-50 start-0 translate-middle-y sm-square"),
        html.Div(className="position-absolute top-50 start-50 translate-middle sm-square"),
        html.Div(className="position-absolute top-50 end-0 translate-middle-y sm-square"),
        html.Div(className="position-absolute bottom-0 start-0 sm-square"),
        html.Div(className="position-absolute bottom-0 start-50 translate-middle-x sm-square"),
        html.Div(className="position-absolute bottom-0 end-0  sm-square"),
    ],
    className="position-relative border", style={"height":175}
)


align_code = """
```
html.Span("baseline", className="align-baseline")
html.Span("top", className="align-top")
html.Span("middle", className="align-middle")
html.Span("bottom", className="align-bottom")
html.Span("text-top", className="align-text-top")
html.Span("text-bottom", className="align-text-bottom")

```"""

align_preview = html.Div(
    [
        html.Span("baseline", className="align-baseline"),
        html.Span("top", className="align-top"),
        html.Span("middle", className="align-middle"),
        html.Span("bottom", className="align-bottom"),
        html.Span("text-top", className="align-text-top"),
        html.Span("text-bottom", className="align-text-bottom")
    ]
)


utility_position = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Position"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/position/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("float-*-{option}"),
                make_listgroup_item("position-{option}"),
                make_listgroup_item("{direction}-{position}"),
                make_listgroup_item("translate-middle"),
                make_listgroup_item("translate-middle-{direction}"),
                make_listgroup_item("align-{option}"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)


