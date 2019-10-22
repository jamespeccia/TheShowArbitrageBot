"""
    File name: actions.py
    Author: James Peccia
    Date created: 5/2/2019
    Date last modified: 5/2/2019
    Python Version: 3.7
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initializes webdriver with desired arguments
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\james\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('--disable-extensions')
driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

# Loads the community market
driver.get('https://mlb19.theshownation.com/community_market')


# Sets a buy order for 'name' at price 'amount'
def set_buy_order(name, amount):
    player_lookup(name)
    driver.find_element_by_xpath("(//input[@name='price'])[2]").send_keys(str(amount) + Keys.RETURN)


# Sets a sell order for 'name' at price 'amount'
def set_sell_order(name, amount):
    player_lookup(name)
    driver.find_element_by_xpath("(//input[@name='price'])[4]").send_keys(str(amount) + Keys.RETURN)


# Flips 'name' at buy price 'buy' + 'insurance' and sell price 'sell' - 'insurance'
def flip(name, buy, sell, insurance):
    set_buy_order(name, sell + insurance)
    time.sleep(1)
    set_sell_order(name, buy - insurance)


# Navigates to the page of the player 'name' that will be flipped
def player_lookup(name):
    driver.get('https://mlb19.theshownation.com/community_market')
    driver.find_element_by_name('name').send_keys(name + Keys.RETURN)
    driver.find_element_by_link_text(name).click()
