"""
This is the card and content of the code snippets and preview content for

Typography
"""

from dash import html
import dash_bootstrap_components as dbc
from utilities import make_link, make_listgroup_item


h1h6_code = """
Note - See also dcc.Markdown() to format text
```
h1h6_html_preview = html.Div(
    [
        html.H1("Heading 1"),
        html.H2("Heading 2"),
        html.H3("Heading 3"),
        html.H4("Heading 4"),
        html.H5("Heading 5"),
        html.H6("Heading 6"),
    ]
)

h1h6_class_preview = html.Div(
    [
        html.Div("Heading 1", className="h1"),
        html.Div("Heading 2", className="h2"),
        html.Div("Heading 3", className="h3"),
        html.Div("Heading 4", className="h4"),
        html.Div("Heading 5", className="h5"),
        html.Div("Heading 6", className="h6"),
    ]
)
```"""

h1h6_html_preview = html.Div(
    [
        html.H1("Heading 1"),
        html.H2("Heading 2"),
        html.H3("Heading 3"),
        html.H4("Heading 4"),
        html.H5("Heading 5"),
        html.H6("Heading 6"),
    ]
)
h1h6_class_preview = html.Div(
    [
        html.Div("Heading 1", className="h1"),
        html.Div("Heading 2", className="h2"),
        html.Div("Heading 3", className="h3"),
        html.Div("Heading 4", className="h4"),
        html.Div("Heading 5", className="h5"),
        html.Div("Heading 6", className="h6"),
    ]
)
h1h6_preview = html.Div(
    [
        h1h6_html_preview,
        html.Div(
            "Or apply heading styles to other components with  className:",
            className="my-4",
        ),
        h1h6_class_preview,
    ]
)

# ------ Display --------------------------------------------------------------


display_code = """
Note - See also dcc.Markdown() to format text
```

display_preview = html.Div(
    [
        html.Div("Display 1", className="display-1"),
        html.Div("Display 2", className="display-2"),
        html.Div("Display 3", className="display-3"),
        html.Div("Display 4", className="display-4"),
        html.Div("Display 5", className="display-5"),
        html.Div("Display 6", className="display-6"),
    ]
)
```"""
display_preview = html.Div(
    [
        html.Div("Display 1", className="display-1"),
        html.Div("Display 2", className="display-2"),
        html.Div("Display 3", className="display-3"),
        html.Div("Display 4", className="display-4"),
        html.Div("Display 5", className="display-5"),
        html.Div("Display 6", className="display-6"),
    ]
)


# ---- lead ----------------------------------------------------------------

lead_code = """
Note - See also dcc.Markdown() to format text
```

lead_preview = html.Div(
    [
        html.P("This is a lead paragraph. It stands out from regular paragraphs.", className="lead"),
        html.P("This is a regular paragraph."),
        
    ]
)
```"""

lead_preview = html.Div(
    [
        html.P(
            "This is a lead paragraph. It stands out from regular paragraphs.",
            className="lead",
        ),
        html.P("This is a regular paragraph."),
    ]
)

# ---- mark  ----------------------------------------------------------------

mark_code = """
Note - See also dcc.Markdown() to format text
```

mark_preview = html.Div(
    [
        html.P(["You can use html.Mark to ", html.Mark("highlight"), " text"]),

    ]
)
```"""

mark_preview = html.Div(
    [html.P(["You can use html.Mark to ", html.Mark("highlight"), " text"]),]
)

# ---- small ----------------------------------------------------------------

small_code = """
Note - See also dcc.Markdown() to format text
```

small_preview = html.Div(
    [
        html.Small("This line of text is meant to be treated as fine print"),
        html.P("This is a regular print."),

    ]
)

```"""

small_preview = html.Div(
    [
        html.Small("This line of text is meant to be treated as fine print"),
        html.P("This is a regular print."),
    ]
)


# ---- abbr & initialism ----------------------------------------------------------------

abbr_code = """
Note - See also dcc.Markdown() to format text
```

abbr_preview = html.Div(
    [
        html.P(html.Abbr("attr", title="attribute")),
        html.P(
            html.Abbr("HTML", title="HyperText Markup Language"), className="initialism"
        ),
        html.P(
            [
                html.Abbr("HTML", title="HyperText Markup Language"),
                "without initialism class",
            ]
        ),
    ]
)


```"""

abbr_preview = html.Div(
    [
        html.P(html.Abbr("attr", title="attribute")),
        html.P(
            html.Abbr("HTML", title="HyperText Markup Language"), className="initialism"
        ),
        html.P(
            [
                html.Abbr("HTML", title="HyperText Markup Language"),
                "without initialism class",
            ]
        ),
    ]
)


# ---- blockquote  ----------------------------------------------------------------

blockquote_code = """
Note - See also dcc.Markdown() to format text
```
blockquote_preview = html.Div(
    [
        html.Blockquote(
            html.P(
                "There are only two industries that refer to their customers as ‘users’."
            ),
            className="blockquote",
        ),
        html.Footer("Edward Tufte ", className="blockquote-footer"),
    ],
)

```"""

blockquote_preview = html.Div(
    [
        html.Blockquote(
            html.P(
                "There are only two industries that refer to their customers as ‘users’."
            ),
            className="blockquote",
        ),
        html.Footer("Edward Tufte ", className="blockquote-footer"),
    ],
)


# ---- cite  ----------------------------------------------------------------

cite_code = """
Note - See also dcc.Markdown() to format text
```
cite_preview = html.Div(
    [
        html.Blockquote(html.P("Where is the ‘any’ key?"), className="blockquote",),
        html.Footer(
            ["Homer Simpson ", html.Cite("The Simpsons", title="The Simpsons TV show")],
            className="blockquote-footer",
        ),
    ],
)

```"""

cite_preview = html.Div(
    [
        html.Blockquote(html.P("Where is the ‘any’ key?"), className="blockquote",),
        html.Footer(
            ["Homer Simpson ", html.Cite("The Simpsons", title="The Simpsons TV show")],
            className="blockquote-footer",
        ),
    ],
)




# --------------------------------------------------------------------
# Cheatsheet Card  - Header name, item name and hover info
# --------------------------------------------------------------------
typography = dbc.Card(
    [
        dbc.CardHeader(
            [
                html.H3("Typography"),
                make_link("https://getbootstrap.com/docs/5.1/content/typography/"),
            ],
            className="hstack gap-4",
        ),
        dbc.ListGroup(
            [
                make_listgroup_item("h1-h6", "headings"),
                make_listgroup_item(
                    "display-{size}", "larger more opinionated heading style"
                ),
                make_listgroup_item("lead", "make paragraphs stand out"),
                make_listgroup_item("mark", "highlight text"),
                make_listgroup_item(
                    "small", "small print, like copyright and legal text"
                ),
                make_listgroup_item("abbr", "abbreviations"),
                make_listgroup_item(
                    "initialism", "slightly smaller font - use with html.Abbr"
                ),
                make_listgroup_item(
                    "blockquote", "for quoting content from another source"
                ),
                make_listgroup_item("blockquote-footer", "blockquote small print"),
                make_listgroup_item("cite", "name of source work"),
            ],
            flush=True,
            className="border-0",
        ),
    ],
    className="class-card",
)
