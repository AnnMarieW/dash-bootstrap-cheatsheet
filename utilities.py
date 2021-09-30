"""

"""
from dash import html, dcc
import dash_bootstrap_components as dbc

dbc_home_url = "https://dbc-v1.herokuapp.com/"
dbc_url = "https://dbc-v1.herokuapp.com/docs/components/"

# These items are highlighted with the "highlight new" button
new_items = [
    "vstack",
    "hstack",
    "vr (vertical rule)",
    "gx-{size}",
    "gx-*-{size}",
    "gy-{size}",
    "gy-*-{size}",
    "g-{size}",
    "g-*-{size}",
    "justify-content-*-{option}",
    # "order-*-{order-name}",
    "gap-*-{size}",
    "{direction}-{position}",
    "translate-middle-{direction}",
    "text-*-start",
    "text-*-center",
    "text-*-end",
    "fs-{size}",
    "fst-{style}",
    "lh-{style}",
    "text-decoration-{option}",
    "opacity-{value}",
    "bg-opacity-{value}",
    "text-opacity-{value}",
    "pe-{option} (pointer)",
    "overflow-{option}",
    "Migration Guide",
    "Icons",
    "Accordion",
    "Breadcrumb",
    "Offcanvas",
    "Pagination",
    "display-{size}"
]


def make_offcanvas(idx):
    return dbc.Offcanvas(
        [
            dbc.Container(
                [
                    make_fullscreen_btn(idx),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Code Snippet"),
                                            dcc.Markdown(
                                                id={"type": "code", "index": idx,},
                                                className="p-2",
                                                style={"minHeight": 250},
                                            ),
                                            dcc.Clipboard(
                                                target_id={
                                                    "type": "code",
                                                    "index": idx,
                                                },
                                                title="copy snippet",
                                                className="position-absolute top-0 end-0 fs-3",
                                            ),
                                        ],
                                        className="position-relative",
                                    ),
                                ],
                                width=12, lg=6
                            ),
                            dbc.Col(
                                [
                                    dbc.Card(
                                        [
                                            dbc.CardHeader("Preview"),
                                            dbc.CardBody(
                                                id={"type": "preview", "index": idx,},
                                                # className="p-2",
                                                style={"minHeight": 250},
                                            ),
                                        ]
                                    )
                                ], width=12, lg=6
                            ),
                        ]
                    ),
                ],
                fluid=True,
            ),
        ],
        id={"type": "off-canvas", "index": idx},
        title=idx,
        is_open=False,
        placement="top",
        scrollable=True,
        style={"position": "absolute", "height": 400},
    )


def make_listgroup_item(idx, tooltip=None):
    listgroup_item = dbc.ListGroupItem(
        idx,
        id={"type": "list-item", "index": idx},
        n_clicks=0,
        className="border-0 text-nowrap",
    )
    add_tooltip = dbc.Tooltip(
        tooltip,
        id={"type": "tooltip", "index": idx},
        target={"type": "list-item", "index": idx},
        # placement="auto-end",
    )
    if tooltip:
        return html.Div([listgroup_item, add_tooltip, make_offcanvas(idx)])
    return html.Div([listgroup_item, make_offcanvas(idx)])


def make_listgroup_link(title, url):
    return dbc.ListGroupItem(
        title,
        id={"type": "list-item", "index": title},
        href=url,
        target="_blank",
        className="border-0",
    )


def make_link(url):
    """
    Makes the link with box arrow icon
    """
    return html.Span(
        [
            html.A(
                className="bi bi-box-arrow-up-right h4",
                href=url,
                target="_blank",
                title="Official Documentation",
            )
        ]
    )


def make_fullscreen_btn(idx):
    return dbc.Button(
        "fullscreen",
        id={"type": "button", "index": idx,},
       # outline=True,
        color="primary",
        style={"position": "absolute", "top": 15, "right": 50},
    )
