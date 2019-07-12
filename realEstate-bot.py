from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class realEstateBot:
    def __init__(self, search):
        self.search = search
        #self.password = password
        self.bot = webdriver.Chrome()

    def closeBrowser(self):
        self.bot.close()

    def search_nav(self):
        bot = self.bot
        bot.get('https://www.zillow.com/')
        time.sleep(2)
        search = bot.find_element_by_class_name("react-autosuggest__input")
        search.clear()
        search.send_keys(self.search)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        for_sale = bot.find_element_by_class_name("ListingButtons__Button-sc-8yz792-1")
        for_sale.click()


zillow = realEstateBot('mississauga')
zillow.search_nav()