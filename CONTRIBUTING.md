# App Maintenance Notes

## App Structure
Main entry point:  `app.py`

- `app.py`: Main app.  Has the main layout and callbacks
- `utilities.py`: Has reusable components and app data used in other parts of the app
- `content` folder: Each file is a cheatsheet card.
- `index_examples.py`:  Ties the list item name in the card with the content displayed in the offcanvas 
code stippets and preview.  This is used in the pattern matching callback in `app.py` to show the content 
when the card item is clicked on


##Adding Content

### Cards with code snippets

**The name of the example on the card must be unique. It's used
as an `id` in the callbacks**


In the `content` directory each file is one cheatsheet card:
  - card definition: Has header name and link, list item name and list item hover info
  - `snippet_name_code` is a code text string for each item - shows in the "Code Snippet" panel of the Offcanvas
  - `snippen_name_preivew` is the code snippet for each item (actual code) for the "Preview" panel of the Offcanvas

In the `index_examples.py`:
  - import the card from the `content` folder
  - add to `examples` dict:
     - key is name of example in the card
     - value is a list [snippet_name_code, snippet_name_preview]

In `app.py`
 - import the card
 - add the card to the layout

### Cards with links only

See an example in `about.py` or `dbc_components.py`