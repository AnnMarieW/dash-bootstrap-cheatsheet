

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_link, dbc_url, dbc_home_url


dbc_components = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Dash Bootstrap Components"),
                make_link(dbc_home_url),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                dbc.ListGroupItem(html.H5("Links to the docs:"), className="border-0"),
                dbc.ListGroupItem("Migration Guide", href=f"{dbc_home_url}/migration-guide/",
                                  target="_blank",className="border-0", ),

            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
