"""
This is the card for the Dash Boostrap Components links
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_link, dbc_url, dbc_home_url

urls = {
    "Dash Community Forum": "https://community.plotly.com/c/dash/python/25/l/latest",
    "Dash Tutorial": "https://dash.plotly.com/",
    "Dash Core Components": "https://dash.plotly.com/dash-core-components",
    "Dash HTML Components": "https://dash.plotly.com/dash-html-components",
    "DataTable": "https://dash.plotly.com/datatable",
    "Dash DAQ components": "https://dash.plotly.com/dash-daq",
    "Plotly Graphs": "https://plotly.com/python/",
    "Plotly Github": "https://github.com/plotly",
}


plotly_links = dbc.Card(
    [
        dbc.CardHeader(
            [html.H3("Plotly Dash"), make_link("https://dash.plotly.com/"),],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [dbc.ListGroupItem(html.H5("Links to the docs:"), className="border-0"),]
            + [make_listgroup_link(title, url) for title, url in urls.items()],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
