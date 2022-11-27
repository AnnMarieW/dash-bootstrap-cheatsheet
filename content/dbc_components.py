"""
This is the card for the Dash Boostrap Components links
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_link, dbc_url, dbc_home_url

dbc_card1_urls = {
    "GitHub dbc Source Code": "https://github.com/facultyai/dash-bootstrap-components",
    "Quickstart": f"{dbc_home_url}docs/quickstart/",
    "Themes" : f"{dbc_home_url}docs/themes/",
    "Theme Explorer": "https://hellodash.pythonanywhere.com/",
    "Icons": f"{dbc_home_url}docs/icons/",
    "Accordion": f"{dbc_url}accordion",
    "Alert": f"{dbc_url}alert/",
    "Badge": f"{dbc_url}badge",
    "Breadcrumb": f"{dbc_url}breadcrumb",
    "Button": f"{dbc_url}button",
    "ButtonGroup": f"{dbc_url}buttongroup",
}


dbc_card2_urls = {
    "Card": f"{dbc_url}card",
    "Carousel": f"{dbc_url}carousel",
    "Collapse": f"{dbc_url}collapse",
    "DropdownMenu": f"{dbc_url}dropdownmenu",
    "Fade": f"{dbc_url}fade",
    "Form": f"{dbc_url}form",
    "Input": f"{dbc_url}input",
    "InputGroup": f"{dbc_url}inputgroup",
    "Jumbotron": f"{dbc_url}jumbotron",
    "Layout": f"{dbc_url}layout",
    "ListGroup": f"{dbc_url}listgroup",

}


dbc_card3_urls = {
    "Modal": f"{dbc_url}modal",
    "Nav": f"{dbc_url}nav",
    "Navbar": f"{dbc_url}navbar",
    "Offcanvas": f"{dbc_url}offcanvas",
    "Pagination": f"{dbc_url}pagination",
    "Popover": f"{dbc_url}popover",
    "Progress": f"{dbc_url}progress",
    "Spinner": f"{dbc_url}spinner",
    "Table": f"{dbc_url}table",
    "Tabs": f"{dbc_url}tabs",
    "Toast": f"{dbc_url}toast",
    "Tooltip": f"{dbc_url}tooltip",
}



dbc_components1 = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Dash Bootstrap Components"),
                html.Div("Card: Start-B"),
                make_link(dbc_home_url),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [dbc.ListGroupItem(html.H5("Links to the docs:"), className="border-0"),]
            + [make_listgroup_link(title, url) for title, url in dbc_card1_urls.items()],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card-tall",
)


dbc_components2 = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Dash Bootstrap Components"),
                html.Div("Card: C-L"),
                make_link(dbc_home_url),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [dbc.ListGroupItem(html.H5("Links to the docs:"), className="border-0"),]
            + [make_listgroup_link(title, url) for title, url in dbc_card2_urls.items()],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card-tall",
)


dbc_components3 = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Dash Bootstrap Components"),
                html.Div("Card: M-Z"),
                make_link(dbc_home_url),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [dbc.ListGroupItem(html.H5("Links to the docs:"), className="border-0"),]
            + [make_listgroup_link(title, url) for title, url in dbc_card3_urls.items()],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card-tall",
)

