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
        self.bot = webdriver.Chrome()
    
    def closeBrowser(self):
        self.bot.close()

    def city_search(self):
        bot = self.bot
        bot.get('https://www.point2homes.com/')
        time.sleep(10)
        search = bot.find_element_by_id('listing-location')
        search.clear()
        search.send_keys(self.search)
        time.sleep(5)
        search.send_keys(Keys.RETURN)
        time.sleep(5)


    def get_prices(self):
        bot = self.bot
        for i in range(1,5):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            houses = bot.find_elements_by_class_name('button-flat-color')
            locations = [elem.get_attribute('href') for elem in houses]
            for location in locations:
                bot.get(location)
                time.sleep(5)
                try:
                    house_price = bot.find_element_by_css_selector('div.price')
                    print(house_price)
                    #converted_price = round(int(house_price))
                    #if(converted_price >= 500000):
                        #Aprint('high price')
                    #else:
                    #    print('low prices')
                except Exception as e:
                    time.sleep(5)


            

gta_cities = ['toronto', 'mississauga', 'hamilton', 'kitchener', 'waterloo', 'barrie', 'ajax'
, 'cambridge', 'peterborough', 'gatineau', 'burlington', 'montreal', 'niagara', 'ottawa', 'guelph',
'quinte', 'trois-rivieres', 'london', 'sherbrooke']

searchbar = random.choice(gta_cities)
point2homes = realEstateBot(searchbar)
print(searchbar)
point2homes.city_search()
point2homes.get_prices()