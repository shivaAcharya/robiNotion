# Inspired from https://github.com/jamalex/notion-py
import robinhood

from notion.client import NotionClient

my_Stocks = robinhood.get_stockInfo()

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2 = "Your Token from webbrowser cookies")

# Replace this URL with the URL of the page you want to edit

robinHood = client.get_collection_view("Your notion link to database")


for key, value in my_Stocks.items():
    new_row = robinHood.collection.add_row()
    new_row.ticker_symbol = key
    new_row.no_of_shares = round(float(value['quantity']), 2)
    new_row.average_cost = round(float(value['average_buy_price']), 2)
    new_row.current_price = round(float(value['price']), 2)

