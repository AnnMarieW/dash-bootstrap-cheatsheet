# This site was adapted for Dash from:
"""
This is the card for the About links
"""

from dash import html, dcc
import dash_bootstrap_components as dbc



book_img = "https://user-images.githubusercontent.com/72614349/185497519-733bdfc3-5731-4419-9a68-44c1cad04a78.png"
nostarch = "https://nostarch.com/book-dash"
github = "fa-brands fa-github"
youtube = "fa-brands fa-youtube"
info = "fa-solid fa-circle-info"
cart = "fa-solid fa-cart-shopping"
plotly = "https://plotly.com/python/"
dash_url = "https://dash.plotly.com/"
forum = "https://community.plotly.com/"
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"
book_github = "https://github.com/DashBookProject/Plotly-Dash"
amw = "https://github.com/AnnMarieW"
adam = "https://www.youtube.com/c/CharmingData/featured"
chris = "https://finxter.com/"
dbt_github = "https://github.com/AnnMarieW/dash-bootstrap-templates"
dbc_docs_url = "https://dash-bootstrap-components.opensource.faculty.ai/"
bootstrap_docs_url = "https://getbootstrap.com/docs/5.1/"



welcome_md = dcc.Markdown(
    f"""
### Welcome to Dash Bootstrap Cheatsheet 🤗

This cheatsheet is based on the official Bootstrap documentation.  You can find more information about each category by 
 clicking on the book icon in the category headings.   
 
If you're new to Dash or Bootstrap, see:
- The  [Plotly Dash]({plotly}) tutorial
- The [Dash Boostrap Components]({dbc_docs_url}) documentation
- The [Bootstrap]({bootstrap_docs_url}) documentation
- Videos by [Charming Data]({adam})
- For even more examples, don't miss the [Dash Bootstrap Utilities Tutorial](https://hellodash.pythonanywhere.com/adding-themes/bootstrap-utility-classes)
on the [Dash Bootstrap Theme Explorer](https://hellodash.pythonanywhere.com/) site.

Still have questions?  Try asking on the [Dash Community Forum](https://community.plotly.com/)
""",)


def make_link(text, icon, link):
    return html.Span(html.A([html.I(className=icon + " ps-1 pe-2"), text], href=link))


button = dbc.Button(
    [html.I(className=cart + " pe-2"),"Order"], color="primary", href=nostarch, size="sm", className="mt-2 ms-1"
)

cover_img = html.A(
    dbc.CardImg(
        src=book_img,
        className="img-fluid rounded-start",
    ),
    href=nostarch,

)

text = dcc.Markdown(
    "From basic components to advanced layouts, learn how to display data in effective, usable, and elegant ways.",
    className="ps-2",
)


authors = html.P(
    [
        "By ",
        make_link("Adam Schroeder ", youtube, adam),
        make_link("Christian Mayer", info, chris),
        make_link("Ann Marie Ward", github, amw),
    ],
    className="card-text p-2",
)


about_me1 = f"""
__This site is maintained by Ann Marie Ward__  
co-author of ["The Book of Dash"]({nostarch})  

"""
about_me = dcc.Markdown(about_me1,
    className="mt-5 text-center small",
    style={"maxWidth": "32rem"},
)


book_card = dbc.Card(
    [
        dbc.Row(
            [
                dbc.Col(cover_img, width=3, className="p-1"),
                dbc.Col(
                    [text, button],
                    width=9,
                ),
            ],
            className="g-0 d-flex align-items-center",
        ),
        dbc.Row(dbc.Col(authors)),
    ],
    className="mt-4 mb-5 small shadow p-2",
    style={"maxWidth": "32rem"},
)

about = dbc.Card(
    [
        dbc.CardHeader([html.H3("About")]),
        dbc.CardBody(welcome_md)
    ],
    className="shadow m-5",
)

book = html.Div(
    [
        html.Hr(),
        dbc.Row(dbc.Col([about_me, book_card], width="auto"), justify="center")

    ]
)