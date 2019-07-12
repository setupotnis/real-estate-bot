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
        bot.get('https://www.point2homes.com/CA')
        time.sleep(10)
        search = bot.find_element_by_id("listing-location")
        search.clear()
        search.send_keys(self.search)
        time.sleep(5)
        search.send_keys(Keys.RETURN)
        time.sleep(6)
        price_value = []
        for i in range(1,7):
            try:
                bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(4)

                proper_prices = bot.find_elements_by_tag_name('span')
                

gta_cities = ['toronto', 'mississauga', 'hamilton', 'Kitchener', 'Waterloo', 'Barrie', 'Ajax'
    , 'cambridge', 'peterborough', 'gatineau', 'burlington', 'montreal', 'niagara', 'ottawa', 'guelph',
    'quinte', 'trois-rivieres', 'london', 'sherbrooke']

search_cities = random.choice(gta_cities)
Point2Homes = realEstateBot(search_cities)
print(search_cities)
Point2Homes.search_nav()



