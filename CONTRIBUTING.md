# App Maintenance Notes

##App Structure
Main entry point:  `app.py`

- app.py: Main app.  Has the main layout and callbacks
- utilites.py: Has reusable components to make the layout
- content folder: Has a file for the content of each card
- index_examples:  ties the list item name in the card with the content


##Adding Content - cards with code snippets

**The name of the example on the card must be unique. It's used
as an id in the callbacks**


in `content` directory each file is one card
  - card definition - add the header link and name of example - shown on main page
  - code snippet as a text string - shows in Offcanvas
  - code snippet (actual code) for the preview - shown in Offcanvas

In the `index_examples.py`:
  - import the card from the `content` folder
  - add to dict:
     - key is name of example in the card
     - value is a list [code_snippet_text, code_snippet_preview]

In `app.py`
 - import the card
 - add the card to the layout