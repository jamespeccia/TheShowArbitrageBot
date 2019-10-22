"""
    File name: bot.py
    Author: James Peccia
    Date created: 5/2/2019
    Date last modified: 5/2/2019
    Python Version: 3.7
"""

import json
import requests
import actions

page = 0
# Checks players on each page and flips them if flipping conditions are met
while True:
    # Increments page and gets the data of the players on that page
    page = page + 1
    response = requests.get(
        'https://mlb19.theshownation.com/apis/listings.json?type=MLB_Card&page={}'.format(str(page)))
    response_text = response.text

    # If condition is met, then the bot has iterated through all pages and restarts from page 1
    if response_text.__contains__('"listings":[]'):
        page = 0
        continue
    players = json.loads(response_text.split('listings":')[1][:-1])

    # Checks players on current page and flips them if flipping conditions are met
    for player in players:
        name = player.get('name')
        sell = player.get('best_buy_price')
        buy = player.get('best_sell_price')
        profit = int(buy * .9 - sell)
        if profit > 100 and buy < 500 and sell > 50:
            actions.flip(name, buy, sell, 10)
            break
