# This site was adapted for Dash from:
"""
This is the card for the About links
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_link, dbc_url, dbc_home_url


about = dbc.Card(
    [
        dbc.CardHeader([html.H3("About"),],),
        dbc.ListGroup(
            [
                dbc.ListGroupItem(
                    [
                        make_listgroup_link(
                            "GitHub Source Code",
                            "https://github.com/AnnMarieW/dash-bootstrap-cheatsheet",
                        )
                    ]
                ),
                dbc.ListGroupItem(
                    make_listgroup_link(
                        "See also: Dash Bootstrap Theme Explorer",
                        "https://hellodash.pythonanywhere.com/theme_explorer",
                    )
                ),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
