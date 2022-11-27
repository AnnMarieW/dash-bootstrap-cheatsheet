"""
This is the card and content of the code snippets and preview content for

Utility:Display
"""


from dash import html
import dash_bootstrap_components as dbc

from utilities import make_link, make_listgroup_item


m_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}    
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("m-0", className="m-0 bg-light border"),
        html.Div("m-1", className="m-1 bg-light border"),
        html.Div("m-2", className="m-2 bg-light border"),
        html.Div("m-3", className="m-3 bg-light border"),
        html.Div("m-4", className="m-4 bg-light border"),
        html.Div("m-5", className="m-5 bg-light border"),
        html.Div("m-auto", className="m-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


m_preview = html.Div(
    [
        html.Div("m-0", className="m-0 bg-light border"),
        html.Div("m-1", className="m-1 bg-light border"),
        html.Div("m-2", className="m-2 bg-light border"),
        html.Div("m-3", className="m-3 bg-light border"),
        html.Div("m-4", className="m-4 bg-light border"),
        html.Div("m-5", className="m-5 bg-light border"),
        html.Div("m-auto", className="m-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


mt_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("mt-0", className="mt-0 bg-light border"),
        html.Div("mt-1", className="mt-1 bg-light border"),
        html.Div("mt-2", className="mt-2 bg-light border"),
        html.Div("mt-3", className="mt-3 bg-light border"),
        html.Div("mt-4", className="mt-4 bg-light border"),
        html.Div("mt-5", className="mt-5 bg-light border"),
        html.Div("mt-auto", className="mt-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


mt_preview = html.Div(
    [
        html.Div("mt-0", className="mt-0 bg-light border"),
        html.Div("mt-1", className="mt-1 bg-light border"),
        html.Div("mt-2", className="mt-2 bg-light border"),
        html.Div("mt-3", className="mt-3 bg-light border"),
        html.Div("mt-4", className="mt-4 bg-light border"),
        html.Div("mt-5", className="mt-5 bg-light border"),
        html.Div("mt-auto", className="mt-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


me_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("me-0", className="me-0 bg-light border"),
        html.Div("me-1", className="me-1 bg-light border"),
        html.Div("me-2", className="me-2 bg-light border"),
        html.Div("me-3", className="me-3 bg-light border"),
        html.Div("me-4", className="me-4 bg-light border"),
        html.Div("me-5", className="me-5 bg-light border"),
        html.Div("me-auto", className="me-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


me_preview = html.Div(
    [
        html.Div("me-0", className="me-0 bg-light border"),
        html.Div("me-1", className="me-1 bg-light border"),
        html.Div("me-2", className="me-2 bg-light border"),
        html.Div("me-3", className="me-3 bg-light border"),
        html.Div("me-4", className="me-4 bg-light border"),
        html.Div("me-5", className="me-5 bg-light border"),
        html.Div("me-auto", className="me-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


mb_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("mb-0", className="mb-0 bg-light border"),
        html.Div("mb-1", className="mb-1 bg-light border"),
        html.Div("mb-2", className="mb-2 bg-light border"),
        html.Div("mb-3", className="mb-3 bg-light border"),
        html.Div("mb-4", className="mb-4 bg-light border"),
        html.Div("mb-5", className="mb-5 bg-light border"),
        html.Div("mb-auto", className="mb-auto bg-light border"),
    ]
)    
```"""


mb_preview = html.Div(
    [
        html.Div("mb-0", className="mb-0 bg-light border"),
        html.Div("mb-1", className="mb-1 bg-light border"),
        html.Div("mb-2", className="mb-2 bg-light border"),
        html.Div("mb-3", className="mb-3 bg-light border"),
        html.Div("mb-4", className="mb-4 bg-light border"),
        html.Div("mb-5", className="mb-5 bg-light border"),
        html.Div("mb-auto", className="mb-auto bg-light border"),
    ]
)


ms_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("ms-0", className="ms-0 bg-light border"),
        html.Div("ms-1", className="ms-1 bg-light border"),
        html.Div("ms-2", className="ms-2 bg-light border"),
        html.Div("ms-3", className="ms-3 bg-light border"),
        html.Div("ms-4", className="ms-4 bg-light border"),
        html.Div("ms-5", className="ms-5 bg-light border"),
        html.Div("ms-auto", className="ms-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


ms_preview = html.Div(
    [
        html.Div("ms-0", className="ms-0 bg-light border"),
        html.Div("ms-1", className="ms-1 bg-light border"),
        html.Div("ms-2", className="ms-2 bg-light border"),
        html.Div("ms-3", className="ms-3 bg-light border"),
        html.Div("ms-4", className="ms-4 bg-light border"),
        html.Div("ms-5", className="ms-5 bg-light border"),
        html.Div("ms-auto", className="ms-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


mx_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("mx-0", className="mx-0 bg-light border"),
        html.Div("mx-1", className="mx-1 bg-light border"),
        html.Div("mx-2", className="mx-2 bg-light border"),
        html.Div("mx-3", className="mx-3 bg-light border"),
        html.Div("mx-4", className="mx-4 bg-light border"),
        html.Div("mx-5", className="mx-5 bg-light border"),
        html.Div("mx-auto", className="mx-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


mx_preview = html.Div(
    [
        html.Div("mx-0", className="mx-0 bg-light border"),
        html.Div("mx-1", className="mx-1 bg-light border"),
        html.Div("mx-2", className="mx-2 bg-light border"),
        html.Div("mx-3", className="mx-3 bg-light border"),
        html.Div("mx-4", className="mx-4 bg-light border"),
        html.Div("mx-5", className="mx-5 bg-light border"),
        html.Div("mx-auto", className="mx-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


my_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
m-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "m-sm-2"
```
html.Div(
    [
        html.Div("my-0", className="my-0 bg-light border"),
        html.Div("my-1", className="my-1 bg-light border"),
        html.Div("my-2", className="my-2 bg-light border"),
        html.Div("my-3", className="my-3 bg-light border"),
        html.Div("my-4", className="my-4 bg-light border"),
        html.Div("my-5", className="my-5 bg-light border"),
        html.Div("my-auto", className="my-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


my_preview = html.Div(
    [
        html.Div("my-0", className="my-0 bg-light border"),
        html.Div("my-1", className="my-1 bg-light border"),
        html.Div("my-2", className="my-2 bg-light border"),
        html.Div("my-3", className="my-3 bg-light border"),
        html.Div("my-4", className="my-4 bg-light border"),
        html.Div("my-5", className="my-5 bg-light border"),
        html.Div("my-auto", className="my-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


p_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
p-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "p-sm-2"
```
html.Div(
    [
        html.Div("p-0", className="p-0 bg-light border"),
        html.Div("p-1", className="p-1 bg-light border"),
        html.Div("p-2", className="p-2 bg-light border"),
        html.Div("p-3", className="p-3 bg-light border"),
        html.Div("p-4", className="p-4 bg-light border"),
        html.Div("p-5", className="p-5 bg-light border"),
        html.Div("p-auto", className="p-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


p_preview = html.Div(
    [
        html.Div("p-0", className="p-0 bg-light border"),
        html.Div("p-1", className="p-1 bg-light border"),
        html.Div("p-2", className="p-2 bg-light border"),
        html.Div("p-3", className="p-3 bg-light border"),
        html.Div("p-4", className="p-4 bg-light border"),
        html.Div("p-5", className="p-5 bg-light border"),
        html.Div("p-auto", className="p-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


pt_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
pt-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "pt-sm-2"
```
html.Div(
    [
        html.Div("p-0", className="pt-0 bg-light border"),
        html.Div("pt-1", className="pt-1 bg-light border"),
        html.Div("pt-2", className="pt-2 bg-light border"),
        html.Div("pt-3", className="pt-3 bg-light border"),
        html.Div("pt-4", className="pt-4 bg-light border"),
        html.Div("pt-5", className="pt-5 bg-light border"),
        html.Div("pt-auto", className="pt-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


pt_preview = html.Div(
    [
        html.Div("pt-0", className="pt-0 bg-light border"),
        html.Div("pt-1", className="pt-1 bg-light border"),
        html.Div("pt-2", className="pt-2 bg-light border"),
        html.Div("pt-3", className="pt-3 bg-light border"),
        html.Div("pt-4", className="pt-4 bg-light border"),
        html.Div("pt-5", className="pt-5 bg-light border"),
        html.Div("pt-auto", className="pt-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


pe_code = """

Make responsive layouts with breakpoints at device or viewport sizes:
pe-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "pe-sm-2"
```
html.Div(
    [
        html.Div("pe-0", className="pe-0 bg-light border"),
        html.Div("pe-1", className="pe-1 bg-light border"),
        html.Div("pe-2", className="pe-2 bg-light border"),
        html.Div("pe-3", className="pe-3 bg-light border"),
        html.Div("pe-4", className="pe-4 bg-light border"),
        html.Div("pe-5", className="pe-5 bg-light border"),
        html.Div("pe-auto", className="pe-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


pe_preview = html.Div(
    [
        html.Div("pe-0", className="pe-0 bg-light border"),
        html.Div("pe-1", className="pe-1 bg-light border"),
        html.Div("pe-2", className="pe-2 bg-light border"),
        html.Div("pe-3", className="pe-3 bg-light border"),
        html.Div("pe-4", className="pe-4 bg-light border"),
        html.Div("pe-5", className="pe-5 bg-light border"),
        html.Div("pe-auto", className="pe-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


pb_code = """

Make responsive layouts with breakpoints at device or viewport sizes:
pb-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "pb-sm-2"
```
html.Div(
    [
        html.Div("pb-0", className="pb-0 bg-light border"),
        html.Div("pb-1", className="pb-1 bg-light border"),
        html.Div("pb-2", className="pb-2 bg-light border"),
        html.Div("pb-3", className="pb-3 bg-light border"),
        html.Div("pb-4", className="pb-4 bg-light border"),
        html.Div("pb-5", className="pb-5 bg-light border"),
        html.Div("pb-auto", className="pb-auto bg-light border"),
    ], 
)    
```"""


pb_preview = html.Div(
    [
        html.Div("pb-0", className="pb-0 bg-light border"),
        html.Div("pb-1", className="pb-1 bg-light border"),
        html.Div("pb-2", className="pb-2 bg-light border"),
        html.Div("pb-3", className="pb-3 bg-light border"),
        html.Div("pb-4", className="pb-4 bg-light border"),
        html.Div("pb-5", className="pb-5 bg-light border"),
        html.Div("pb-auto", className="pb-auto bg-light border"),
    ]
)


ps_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
ps-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "ps-sm-2"
```
html.Div(
    [
        html.Div("ps-0", className="ps-0 bg-light border"),
        html.Div("ps-1", className="ps-1 bg-light border"),
        html.Div("ps-2", className="ps-2 bg-light border"),
        html.Div("ps-3", className="ps-3 bg-light border"),
        html.Div("ps-4", className="ps-4 bg-light border"),
        html.Div("ps-5", className="ps-5 bg-light border"),
        html.Div("ps-auto", className="ps-auto bg-light border"),
    ],className="d-flex flex-wrap align-items-start"
)    
```"""


ps_preview = html.Div(
    [
        html.Div("ps-0", className="ps-0 bg-light border"),
        html.Div("ps-1", className="ps-1 bg-light border"),
        html.Div("ps-2", className="ps-2 bg-light border"),
        html.Div("ps-3", className="ps-3 bg-light border"),
        html.Div("ps-4", className="ps-4 bg-light border"),
        html.Div("ps-5", className="ps-5 bg-light border"),
        html.Div("ps-auto", className="ps-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


px_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
px-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "px-sm-2"
```

html.Div(
    [
        html.Div("px-0", className="px-0 bg-light border"),
        html.Div("px-1", className="px-1 bg-light border"),
        html.Div("px-2", className="px-2 bg-light border"),
        html.Div("px-3", className="px-3 bg-light border"),
        html.Div("px-4", className="px-4 bg-light border"),
        html.Div("px-5", className="px-5 bg-light border"),
        html.Div("px-auto", className="px-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


px_preview = html.Div(
    [
        html.Div("px-0", className="px-0 bg-light border"),
        html.Div("px-1", className="px-1 bg-light border"),
        html.Div("px-2", className="px-2 bg-light border"),
        html.Div("px-3", className="px-3 bg-light border"),
        html.Div("px-4", className="px-4 bg-light border"),
        html.Div("px-5", className="px-5 bg-light border"),
        html.Div("px-auto", className="px-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


py_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
py-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}  
for example: "py-sm-2"
```
html.Div(
    [
        html.Div("py-0", className="py-0 bg-light border"),
        html.Div("py-1", className="py-1 bg-light border"),
        html.Div("py-2", className="py-2 bg-light border"),
        html.Div("py-3", className="py-3 bg-light border"),
        html.Div("py-4", className="py-4 bg-light border"),
        html.Div("py-5", className="py-5 bg-light border"),
        html.Div("py-auto", className="py-auto bg-light border"),
    ], className="d-flex flex-wrap align-items-start"
)    
```"""


py_preview = html.Div(
    [
        html.Div("py-0", className="py-0 bg-light border"),
        html.Div("py-1", className="py-1 bg-light border"),
        html.Div("py-2", className="py-2 bg-light border"),
        html.Div("py-3", className="py-3 bg-light border"),
        html.Div("py-4", className="py-4 bg-light border"),
        html.Div("py-5", className="py-5 bg-light border"),
        html.Div("py-auto", className="py-auto bg-light border"),
    ],
    className="d-flex flex-wrap align-items-start",
)


gap_code = """

Make responsive layouts with breakpoints at device or viewport sizes:  
gap-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5}     
for example: "gap-sm-0"
```
html.Div(
    [
        html.Div("Grid item 1", className="p-2 bg-light border"),
        html.Div("Grid item 2", className="p-2 bg-light border"),
        html.Div("Grid item 3", className="p-2 bg-light border"),
        
    ], className="d-grid gap-3"
)    
```"""


gap_preview = html.Div(
    [
        html.Div("Grid item 1", className="p-2 bg-light border"),
        html.Div("Grid item 2", className="p-2 bg-light border"),
        html.Div("Grid item 3", className="p-2 bg-light border"),
    ],
    className="d-grid gap-3",
)


# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
utility_spacing_margin = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Spacing margin"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/spacing/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item(
                    "m-*-{option}",
                    "margin all sides with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "mt-*-{option}",
                    "margin on top with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "me-*-{option}",
                    "margin at end with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "mb-*-{option}",
                    "margin bottom with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "ms-*-{option}",
                    "margin at start with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "mx-*-{option}",
                    "margin horizontal with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "my-*-{option}",
                    "margin vertical with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),

                make_listgroup_item(
                    "gap-*-{size}",
                    "gap all sides with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5}",
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)

utility_spacing_padding = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Spacing padding"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/spacing/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [

                make_listgroup_item(
                    "p-*-{option}",
                    "padding all sides with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "pt-*-{option}",
                    "padding on top with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "pe-*-{option}",
                    "padding at end with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "pb-*-{option}",
                    "padding on bottom with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "ps-*-{option}",
                    "padding at start with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "px-*-{option}",
                    "padding horizontal with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "py-*-{option}",
                    "padding vertical with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}",
                ),
                make_listgroup_item(
                    "gap-*-{sz}",
                    "gap all sides with breakpoints and size: m-{xs|sm|md|lg|xl|xxl}-{0|1|2|3|4|5}",
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)

