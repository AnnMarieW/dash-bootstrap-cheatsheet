"""
This is the card and content of the code snippets and preview content for

Utility:Text
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item

text_start_code = """

text-start can be used for responsive cases with the help of
text-{sm|md|lg|xl|xxl}-start 
example "text-sm-start
```
html.P("Start aligned text on all viewport sizes", className="text-start")
html.P("Start aligned text on all viewport sized small or wider", className="text-sm-start")
html.P("Start aligned text on all viewport sized medium or wider", className="text-md-start")
html.P("Start aligned text on all viewport sized large or wider", className="text-lg-start")
html.P("Start aligned text on all viewport sized extra large or wider", className="text-xl-start")
html.P("Start aligned text on all viewport sized extra extra large", className="text-xxl-start")
```"""

text_start_preview = html.Div(
    [
        html.P("Start aligned text on all viewport sizes", className="text-start"),
        html.P(
            "Start aligned text on all viewport sized small or wider",
            className="text-sm-start",
        ),
        html.P(
            "Start aligned text on all viewport sized medium or wider",
            className="text-md-start",
        ),
        html.P(
            "Start aligned text on all viewport sized large or wider",
            className="text-lg-start",
        ),
        html.P(
            "Start aligned text on all viewport sized extra large or wider",
            className="text-xl-start",
        ),
        html.P(
            "Start aligned text on all viewport sized extra extra large",
            className="text-xxl-start",
        ),
    ]
)


text_center_code = """

text-center can be used for responsive cases with the help of
text-{sm|md|lg|xl|xxl}-center
example "text-sm-center
```
html.P("Center aligned text on all viewport sizes", className="text-center")
html.P("Center aligned text on all viewport sized small or wider", className="text-sm-center")
html.P("Center aligned text on all viewport sized medium or wider", className="text-md-center")
html.P("Center aligned text on all viewport sized large or wider", className="text-lg-center")
html.P("Center aligned text on all viewport sized extra large or wider", className="text-xl-center")
html.P("Center aligned text on all viewport sized extra extra large", className="text-xxl-center")
```"""

text_center_preview = html.Div(
    [
        html.P("Center aligned text on all viewport sizes", className="text-center"),
        html.P(
            "Center aligned text on all viewport sized small or wider",
            className="text-sm-center",
        ),
        html.P(
            "Center aligned text on all viewport sized medium or wider",
            className="text-md-center",
        ),
        html.P(
            "Center aligned text on all viewport sized large or wider",
            className="text-lg-center",
        ),
        html.P(
            "Center aligned text on all viewport sized extra large or wider",
            className="text-xl-center",
        ),
        html.P(
            "Center aligned text on all viewport sized extra extra large",
            className="text-xxl-center",
        ),
    ]
)


text_end_code = """

text-end can be used for responsive cases with the help of
text-{sm|md|lg|xl|xxl}-end 
example "text-sm-end
```
html.P("End aligned text on all viewport sizes", className="text-end")
html.P("End aligned text on all viewport sized small or wider", className="text-sm-end")
html.P("End aligned text on all viewport sized medium or wider", className="text-md-end")
html.P("End aligned text on all viewport sized large or wider", className="text-lg-end")
html.P("End aligned text on all viewport sized extra large or wider", className="text-xl-end")
html.P("End aligned text on all viewport sized extra extra large", className="text-xxl-end")
```"""

text_end_preview = html.Div(
    [
        html.P("End aligned text on all viewport sizes", className="text-end"),
        html.P(
            "End aligned text on all viewport sized small or wider",
            className="text-sm-end",
        ),
        html.P(
            "End aligned text on all viewport sized medium or wider",
            className="text-md-end",
        ),
        html.P(
            "End aligned text on all viewport sized large or wider",
            className="text-lg-end",
        ),
        html.P(
            "End aligned text on all viewport sized extra large or wider",
            className="text-xl-end",
        ),
        html.P(
            "End aligned text on all viewport sized extra extra large",
            className="text-xxl-end",
        ),
    ]
)

text_wrap_code = """
```
dbc.Badge("This text should wrap", className="text-wrap", style={"width":75})
```"""

text_wrap_preview = dbc.Container(
    dbc.Badge("This text should wrap", className="text-wrap", style={"width": 75})
)


text_nowrap_code = """
```
dbc.Badge("This text does not wrap", className="text-nowrap", style={"width":50})
```"""

text_nowrap_preview = dbc.Container(
    dbc.Badge("This text does not wrap", className="text-nowrap", style={"width": 50})
)

text_break_code = """
```
html.P(className="text-break", children="mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
```"""

text_break_preview = dbc.Container(
    html.P(
        className="text-break",
        children="mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
    )
)

text_option_code = """
```
html.P("Lowercased text", className="text-lowercase")
html.P("Uppercased text", className="text-uppercase")
html.P("CapiTaliZed text", className="text-capitalize")
```"""

text_option_preview = dbc.Container(
    [
        html.P("Lowercased text", className="text-lowercase"),
        html.P("Uppercased text", className="text-uppercase"),
        html.P("CapiTaliZed text", className="text-capitalize"),
    ]
)

fs_size_code = """
```
html.P("fs-1", className="fs-1 text")
html.P("fs-2", className="fs-2 text")
html.P("fs-3", className="fs-3 text")
html.P("fs-4", className="fs-4 text")
html.P("fs-5", className="fs-5 text")
html.P("fs-6", className="fs-6 text")
```"""

fs_size_preview = dbc.Container(
    [
        html.P("fs-1", className="fs-1 text"),
        html.P("fs-2", className="fs-2 text"),
        html.P("fs-3", className="fs-3 text"),
        html.P("fs-4", className="fs-4 text"),
        html.P("fs-5", className="fs-5 text"),
        html.P("fs-6", className="fs-6 text"),
    ]
)

fw_weight_code = """
```
html.P("Bold text", className="fw-bold")
html.P("Bolder weight text (relative to the parent element)", className="fw-bolder")
html.P("Normal weight text")
html.P("Light weight text", className="fw-light")
html.P("Lighter weight text (relative to the parent container)", className="fw-lighter")
```"""

fw_weight_preview = html.Div(
    [
        html.P("Bold text", className="fw-bold"),
        html.P(
            "Bolder weight text (relative to the parent element)", className="fw-bolder"
        ),
        html.P("Normal weight text"),
        html.P("Light weight text", className="fw-light"),
        html.P(
            "Lighter weight text (relative to the parent container)",
            className="fw-lighter",
        ),
    ]
)

fst_style_code = """
```
html.P("Italic text", className="fst-italic")
html.P("Text with normal font style", className="fst-normal")
```"""

fst_style_preview = html.Div(
    [
        html.P("Italic text", className="fst-italic"),
        html.P("Text with normal font style", className="fst-normal"),
    ]
)


lh_style_code = """
```
lorem_text = "Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Donec sed odio dui. Cras mattis pannenkoek purus sit amet fermentum. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Cras mattis consectetur purus sit amet fermentum."
html.P(lorem_text, className="lh-1")
html.P(lorem_text, className="lh-sm")
html.P(lorem_text, className="lh-base")
html.P(lorem_text, className="lh-lg")
```"""

lorem_text = "Vivamus sagittis lacus vel augue laoreet rutrum faucibus dolor auctor. Donec sed odio dui. Cras mattis pannenkoek purus sit amet fermentum. Praesent commodo cursus magna, vel scelerisque nisl consectetur et. Nullam id dolor id nibh ultricies vehicula ut id elit. Cras mattis consectetur purus sit amet fermentum."
lh_style_preview = html.Div(
    [
        html.P(lorem_text, className="lh-1"),
        html.P(lorem_text, className="lh-sm"),
        html.P(lorem_text, className="lh-base"),
        html.P(lorem_text, className="lh-lg"),
    ]
)

font_monospace_code = """
```
html.P("This is in monospace", className="font-monospace")
```"""
font_monospace_preview = html.P("This is in monospace", className="font-monospace")


text_reset_code = """
```
html.P(
    [
        "Muted text with a ", 
        html.A("reset link", href="#", className="text-reset")
    ],
    className="text-muted"
)
```"""
text_reset_preview = html.P(
    ["Muted text with a ", html.A("reset link", href="#", className="text-reset")],
    className="text-muted",
)

text_decoration_code = """
```
html.P("This text has a line underneath it", className="text-decoration-underline")
html.P("This text has a line going through it", className="text-decoration-line-through")
html.A("This link has text decoration removed",  href="#",className="text-decoration-none")
```"""

text_decoration_preview = html.Div(
    [
        html.P(
            "This text has a line underneath it", className="text-decoration-underline"
        ),
        html.P(
            "This text has a line going through it",
            className="text-decoration-line-through",
        ),
        html.A(
            "This link has text decoration removed",
            href="#",
            className="text-decoration-none",
        ),
    ]
)


# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
utility_text = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Text"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/text/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "text-*-start",
                    "align text - start with breakpoings {xs|sm|md|lg|xl|xxl}",
                ),
                make_listgroup_item(
                    "text-*-center",
                    "align text - center with breakpoings {xs|sm|md|lg|xl|xxl}",
                ),
                make_listgroup_item(
                    "text-*-end",
                    "align text - end with breakpoings {xs|sm|md|lg|xl|xxl}",
                ),
                make_listgroup_item("text-wrap", "text wraps in parent"),
                make_listgroup_item("text-nowrap", "text may overflow parent"),
                make_listgroup_item(
                    "text-break", "long words will break to stay in parent"
                ),
                make_listgroup_item(
                    "text-{option}",
                    "Transform text with text-{lowercase|uppercase|capitalize",
                ),
                make_listgroup_item(
                    "fs-{size}", "font size {1|2|3|4|5|6} corresponds to heading sizes"
                ),
                make_listgroup_item(
                    "fw-{weight}", "font wight {bold|bolder|normal|light|lighter"
                ),
                make_listgroup_item("fst-{style}", "font style {italic|normal}"),
                make_listgroup_item("lh-{style}", "line height {1|sm|base|lg"),
                make_listgroup_item("font-monospace", "font monospace"),
                make_listgroup_item(
                    "text-reset", "reset text or link color so color is from parent"
                ),
                make_listgroup_item(
                    "text-decoration-{option}",
                    "text-decoration{underline|line-through|none",
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card-tall",
)
