from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import smtplib
import requests
import time
import random
import sys

gta_cities = ['toronto, ON', 'mississauga, ON', 'hamilton, ON', 'kitchener, ON', 'waterloo, ON', 'barrie, ON', 'ajax'
, 'cambridge, ON', 'peterborough, ON', 'gatineau, ON', 'burlington, ON', 'montreal, ON', 'niagara, ON', 'ottawa, ON', 'guelph',
'quinte, ON', 'london, ON']
searchbar = random.choice(gta_cities)

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()

class realEstateBot:
    def __init__(self, search, username, password):
        self.search = search
        self.username = username
        self.password = password
        self.bot = webdriver.Chrome()
    
    def closeBrowser(self):
        self.bot.close()

    def login(self):
        bot = self.bot
        bot.get('https://www.point2homes.com/')
        time.sleep(2)
        bot.find_element_by_id('login').click()
        time.sleep(4)
        username = bot.find_element_by_id('Username')
        password = bot.find_element_by_id('Password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(5)
        search = bot.find_element_by_id('listing-location')
        search.clear()
        search.send_keys(self.search)
        time.sleep(5)
        search.send_keys(Keys.RETURN)
        time.sleep(5)

    def get_info(self):
        bot = self.bot
        for i in range(1):
            bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            for j in range(10):
                bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                houses = bot.find_elements_by_class_name('button-flat-color')
                locations = [elem.get_attribute('href') for elem in houses]
                bot.find_element_by_class_name('pager-next').click()
                for location in locations:
                    try:
                        URL = location
                        headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"}
                        page = requests.get(URL, headers=headers)
                        soup = BeautifulSoup(page.content, 'html.parser')
                        address = soup.find(id='ratehub').get_text()
                        print(address[50:-4]) 
                    except Exception as e:
                        continue




point2homes = realEstateBot(searchbar, 'email', 'password')
print(searchbar)
point2homes.login()
point2homes.get_info()