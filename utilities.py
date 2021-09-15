"""

"""
from dash import html, dcc
import dash_bootstrap_components as dbc

dbc_home_url = "https://dbc-v1.herokuapp.com/"
dbc_url = "https://dbc-v1.herokuapp.com/docs/components/"


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
                                ]
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
                                ]
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


def make_listgroup_item(idx):
    return html.Div(
        [
            dbc.ListGroupItem(
                idx,
                id={"type": "list-item", "index": idx},
                n_clicks=0,
                className="border-0",
            ),
            make_offcanvas(idx),
        ],
        style={"minWidth": 200},
    )


def make_listgroup_link(title, url):
    return dbc.ListGroupItem(title, href=url, target="_blank", className="border-0")


def make_link(url):
    """
    Makes the link with box arrow icon
    """
    return html.Span(
        [
            html.A(
                className="bi bi-box-arrow-up-right h4",
                href=url,
                target="blank",
                title="Official Documentation",
            )
        ]
    )


def make_fullscreen_btn(idx):
    return dbc.Button(
        "fullscreen",
        id={"type": "button", "index": idx,},
        outline=True,
        color="secondary",
        style={"position": "absolute", "top": 15, "right": 50},
    )
