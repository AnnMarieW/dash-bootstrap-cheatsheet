# App Maintenance Notes

##App Structure
Main entry point:  Run app.py

- app.py: Main app.  Has the main layout and callbacks
- utilites.py: Has reusable components to make the layout
- content folder: Has a file for the content of each card
- index_examples:  ties the list item name in the card with the content


##Adding Content

**The name of the example on the card must be unique. It's used
as an id in the callbacks**


in `content` directory each file is one card
  - card definition - add the header link and name of example 
  - code snippet as a text string
  - code snippet for the preview

In the `index_examples.py`:
  - import the card frm the content folder
  - add content to dict:
     - key is name of example in the card
     - value is a list [code_snippet_text, code_snippet_preview]

In `app.py`
 - import the card
 - add the card to the layout