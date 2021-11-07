# robiNotion

This project is to get stock prices from robinhood account and note them in notion database.

# Steps to Project

1. Get dictionary with token as key and stock price as value from robinhood.py
2. Login to notion using token and link to database
3. Write stock information in the database

# Issues I Ran

1. HTTPError - Invalid input
    1. Cause - Notion API has changed and large limit gets 404 error
    2. Solution - Change limit from 10,000 to 100 in client.py and store.py
        https://stackoverflow.com/a/66546826/17346473
              
2. get_collection_view method leads to HTTPError - Invalid input
    1. Cause - Some error in source code or Notion API
    2. Solution - Need to use venv with merger of pr #352
        1. https://github.com/jamalex/notion-py/pull/352

# ToDO

- Figure out table view and update specific cell
- Work with pages and gmail notes
- ......

# Inspired from:
 - https://github.com/jamalex/notion-py
 - https://github.com/jmfernandes/robin_stocks
