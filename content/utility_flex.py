"""
This is the card and content of the code snippets and preview content for

Utility:Flex
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


flex_row_code = """
```
Display flex can be used for responsive cases as well with the help of 
flex-{sm|md|lg|xl|xxl}-row
example:  "flex-sm-row"

html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),

    ],
    className="d-flex flex-row border bg-light"
)
```"""

flex_row_preview = html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-row border bg-light",
)


flex_row_reverse_code = """
```
Display flex can be used for responsive cases as well with the help of 
flex-{sm|md|lg|xl|xxl}-row-reverse
example:  "flex-sm-row-reverse"

html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),

    ],
    className="d-flex flex-row-reverse border bg-light"
)
```"""

flex_row_reverse_preview = html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-row-reverse border bg-light",
)


flex_column_code = """
```
Display flex can be used for responsive cases as well with the help of 
flex-{sm|md|lg|xl|xxl}-column
example:  "flex-sm-column"

html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),

    ],
    className="d-flex flex-column border bg-light"
)
```"""

flex_column_preview = html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-column border bg-light",
)

flex_column_reverse_code = """
```
Display flex can be used for responsive cases as well with the help of 
flex-{sm|md|lg|xl|xxl}-column-reverse
example:  "flex-sm-column-reverse"

html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),

    ],
    className="d-flex flex-column-reverse border bg-light"
)
```"""

flex_column_reverse_preview = html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-column-reverse border bg-light",
)


justify_content_code = """
```
justify-content can be used for responsive cases as well with the help of 
justify-content-{sm|md|lg|xl|xxl}-{start|end|center|between|around|evenly}
example:  "justify-content-sm-start"

flex_items = [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary")
]

justify_content_preview = html.Div(
    [
        html.Div(flex_items, className="d-flex justify-content-start bg-light border mb-2"),
        html.Div(flex_items, className="d-flex justify-content-end bg-light border mb-2"),
        html.Div(flex_items, className="d-flex justify-content-center bg-light border mb-2"),
        html.Div(flex_items, className="d-flex justify-content-between bg-light border mb-2"),
        html.Div(flex_items, className="d-flex justify-content-around bg-light border mb-2"),
        html.Div(flex_items, className="d-flex justify-content-evenly bg-light border mb-2"),
    ]
)
```"""

flex_items = [
    html.Div("Flex item 1", className="p-2 bg-secondary"),
    html.Div("Flex item 2", className="p-2 bg-secondary"),
    html.Div("Flex item 3", className="p-2 bg-secondary"),
]

justify_content_preview = html.Div(
    [
        html.Div(
            flex_items, className="d-flex justify-content-start bg-light border mb-2"
        ),
        html.Div(
            flex_items, className="d-flex justify-content-end bg-light border mb-2"
        ),
        html.Div(
            flex_items, className="d-flex justify-content-center bg-light border mb-2"
        ),
        html.Div(
            flex_items, className="d-flex justify-content-between bg-light border mb-2"
        ),
        html.Div(
            flex_items, className="d-flex justify-content-around bg-light border mb-2"
        ),
        html.Div(
            flex_items, className="d-flex justify-content-evenly bg-light border mb-2"
        ),
    ]
)


align_items_code = """
```
align-items can be used for responsive cases as well with the help of 
align-items-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}
example:  "align-items-sm-start"

flex_items = [
    html.Div("Flex item 1", className="p-2 bg-secondary"),
    html.Div("Flex item 2", className="p-2 bg-secondary"),
    html.Div("Flex item 3", className="p-2 bg-secondary"),
]

align_items_preview = html.Div(
    [
        html.Div(flex_items, className="d-flex align-items-start bg-light border mb-2", style={"height": 100}),
        html.Div(flex_items, className="d-flex align-items-end bg-light border mb-2", style={"height": 100}),
        html.Div(flex_items, className="d-flex align-items-center bg-light border mb-2", style={"height": 100}),
        html.Div(flex_items, className="d-flex align-items-baseline bg-light border mb-2", style={"height": 100}),
        html.Div(flex_items, className="d-flex align-items-stretch bg-light border mb-2", style={"height": 100}),
    ]
)

```"""

align_items_preview = html.Div(
    [
        html.Div(
            flex_items,
            className="d-flex align-items-start bg-light border mb-2",
            style={"height": 100},
        ),
        html.Div(
            flex_items,
            className="d-flex align-items-end bg-light border mb-2",
            style={"height": 100},
        ),
        html.Div(
            flex_items,
            className="d-flex align-items-center bg-light border mb-2",
            style={"height": 100},
        ),
        html.Div(
            flex_items,
            className="d-flex align-items-baseline bg-light border mb-2",
            style={"height": 100},
        ),
        html.Div(
            flex_items,
            className="d-flex align-items-stretch bg-light border mb-2",
            style={"height": 100},
        ),
    ]
)

align_self_code = """
```
align-self can be used for responsive cases as well with the help of
align-self-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}

def make_flex_align_items(className):
    return html.Div(
        [
            html.Div("Flex item", className="p-2 bg-secondary"),
            html.Div("Aligned Flex item", className=className + " p2 bg-secondary"),
            html.Div("Flex item", className="p-2 bg-secondary"),
        ],
        className="d-flex bg-light border mb-2",
        style={"height":100}
    )


align_self_preview = html.Div(
    [
        make_flex_align_items("align-self-start"),
        make_flex_align_items("align-self-end"),
        make_flex_align_items("align-self-center"),
        make_flex_align_items("align-self-baseline"),
        make_flex_align_items("align-self-stretch"),
    ]
)

```"""


def make_flex_align_items(className):
    return html.Div(
        [
            html.Div("Flex item", className="p-2 bg-secondary border"),
            html.Div("Aligned Flex item", className=className + " p2 bg-secondary border"),
            html.Div("Flex item", className="p-2 bg-secondary border"),
        ],
        className="d-flex bg-light border mb-2",
        style={"height": 100},
    )


align_self_preview = html.Div(
    [
        make_flex_align_items("align-self-start"),
        make_flex_align_items("align-self-end"),
        make_flex_align_items("align-self-center"),
        make_flex_align_items("align-self-baseline"),
        make_flex_align_items("align-self-stretch"),
    ]
)

flex_fill_code = """
```
flex-fill can be used for responsive cases as well with the help of
flex-{sm|md|lg|xl|xxl}-fill

flex_fill_preview = html.Div(
    [
        html.Div("Flex item with a lot of content", className="flex-fill p-2 bg-secondary"),
        html.Div("Flex item", className="flex-fill p-2 bg-secondary"),
        html.Div("Flex item", className="flex-fill p-2 bg-secondary"),
    ],
    className="d-flex bg-light border",
)


```"""

flex_fill_preview = html.Div(
    [
        html.Div(
            "Flex item with a lot of content", className="flex-fill p-2 bg-secondary"
        ),
        html.Div("Flex item", className="flex-fill p-2 bg-secondary"),
        html.Div("Flex item", className="flex-fill p-2 bg-secondary"),
    ],
    className="d-flex bg-light border",
)
flex_grow_code = """
```
flex-grow can be used for responsive cases as well with the help of
flex-{sm|md|lg|xl|xxl}-grow-{0|1}

flex_grow_preview = html.Div(
    [
        html.Div("Flex item 1", className="flex-grow-1 p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex bg-light border",
)
```"""

flex_grow_preview = html.Div(
    [
        html.Div("Flex item 1", className="flex-grow-1 p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
    ],
    className="d-flex bg-light border",
)

flex_shrink_code = """
```
flex-shrink can be used for responsive cases as well with the help of
flex-{sm|md|lg|xl|xxl}-shrink-{0|1}

flex_shrink_preview = html.Div(
    [
        html.Div("Flex item 1", className="w-100 p-2 bg-secondary"),
        html.Div("Flex item 2", className="flex-shrink-1 p-2 bg-secondary"),        
    ],
    className="d-flex bg-light border",
)
```"""

flex_shrink_preview = html.Div(
    [
        html.Div("Flex item 1", className="w-100 p-2 bg-secondary"),
        html.Div("Flex item 2", className="flex-shrink-1 p-2 bg-secondary"),
    ],
    className="d-flex bg-light border",
)

flex_nowrap_code = """
```
flex-nowrap can be used for responsive cases as well with the help of 
flex-{sm|md|lg|xl|xxl}-nowrap

html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
        html.Div("Flex item 5", className="p-2 bg-secondary"),
        html.Div("Flex item 5", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-nowrap bg-light border", style={"width": "8rem"}
)

```"""
flex_nowrap_preview = html.Div(
    [
        html.Div("Flex item 1", className="p-2 bg-secondary"),
        html.Div("Flex item 2", className="p-2 bg-secondary"),
        html.Div("Flex item 3", className="p-2 bg-secondary"),
        html.Div("Flex item 5", className="p-2 bg-secondary"),
        html.Div("Flex item 5", className="p-2 bg-secondary"),
    ],
    className="d-flex flex-nowrap bg-light border",
    style={"width": "8rem"},
)

flex_wrap_code = """
```
flex-wrap can be used for responsive cases as well with the help of
flex-{sm|md|lg|xl|xxl}-wrap
html.Div(
    [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
    className="d-flex flex-wrap border bg-light",
)
```"""

flex_wrap_preview = html.Div(
    [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
    className="d-flex flex-wrap border bg-light",
)


flex_wrap_reverse_code = """
```
flex-wrap-reverse can be used for responsive cases as well with the help of
flex-reverse-{sm|md|lg|xl|xxl}-wrap

html.Div(
    [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
    className="d-flex flex-wrap-reverse border bg-light",
)
```"""

flex_wrap_reverse_preview = html.Div(
    [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
    className="d-flex flex-wrap-reverse border bg-light",
)

order_number_code = """
```
order can be used for responsive cases as well with the help of
order-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5} 

order_number_preview = html.Div(
    [
        html.Div("flex item 1", className="order-3 p-2 bg-secondary" ),
        html.Div("flex item 2", className="order-2 p-2 bg-secondary" ), 
        html.Div("flex item 3", className="order-5 p-2 bg-secondary" )
    ],
    className="d-flex flex-nowrap border bg-light"
)
```"""
order_number_preview = html.Div(
    [
        html.Div("flex item 1", className="order-3 p-2 bg-secondary"),
        html.Div("flex item 2", className="order-2 p-2 bg-secondary"),
        html.Div("flex item 3", className="order-5 p-2 bg-secondary"),
    ],
    className="d-flex flex-nowrap border bg-light",
)

order_name_code = """
```
order can be used for responsive cases as well with the help of
order-{sm|md|lg|xl|xxl}-{first|last} 

html.Div(
    [
        html.Div("flex item 1", className="order-3 p-2 bg-secondary"),
        html.Div("flex item 2", className="order-last p-2 bg-secondary"),
        html.Div("flex item 3", className="order-first p-2 bg-secondary"),
        html.Div("flex item 4", className="order-1 p-2 bg-secondary")
    ],
    className="d-flex flex-nowrap border bg-light"
)
```"""
order_name_preview = html.Div(
    [
        html.Div("flex item 1", className="order-3 p-2 bg-secondary"),
        html.Div("flex item 2", className="order-last p-2 bg-secondary"),
        html.Div("flex item 3", className="order-first p-2 bg-secondary"),
        html.Div("flex item 4", className="order-1 p-2 bg-secondary"),
    ],
    className="d-flex flex-nowrap border bg-light",
)


align_content_code = """
```
align-content can be used for responsive cases as well with the help of
align-content-{sm|md|lg|xl|xxl}-{start|end|center|around|stretch} 

html.Div(
    [
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-start flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-end flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-center flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-around flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-stretch flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
    ]
)
```"""
align_content_preview= html.Div(
    [
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-start flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-end flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-center flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-around flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
        html.Div(
            [html.Div("Flex item", className="p-2 bg-secondary")] * 15,
            className="d-flex align-content-stretch flex-wrap border bg-light mb-2",
            style={"height": 200},
        ),
    ]
)

utility_flex = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Utility: Flex"),
                make_link("https://getbootstrap.com/docs/5.1/utilities/flex/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("flex-*-row"),
                make_listgroup_item("flex-*-row-reverse"),
                make_listgroup_item("flex-*-column"),
                make_listgroup_item("flex-*-column-reverse"),
                make_listgroup_item("justify-content-*-{option}"),
                make_listgroup_item("align-items-*-{option}"),
                make_listgroup_item("align-self-*-{option}"),
                make_listgroup_item("flex-*-fill"),
                make_listgroup_item("flex-grow-{option}"),
                make_listgroup_item("flex-shrink-{option}"),
                make_listgroup_item("flex-*-nowrap"),
                make_listgroup_item("flex-*-wrap"),
                make_listgroup_item("flex-*-wrap-reverse"),
                make_listgroup_item("order-*-{order-number}"),
                make_listgroup_item("order-*-{order-name}"),
                make_listgroup_item("align-content-*-{option}")
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
