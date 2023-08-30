# cashcog-ui-automation

## Prerequisite:
    - internet should be present (selenium driver won't work)
    - libraries from requirements.txt installed
    - chrome / edge / firefox browsers present

## commands:
    - `pytest tests/ --html=reports/report.html`

## folder structure:
    - page_objects
        one browser page corresponds to one file
        holds all selectors and methods to interact with that page 
    - tests
        each file holds test cases based on objective (use of asserts & pytest decorators)
