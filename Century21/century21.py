#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 23:02:59 2020

@author: tianlu
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.century21.com.au/properties-for-sale?page=1&searchtype=sale")
c = r.content
soup = BeautifulSoup(c,"html.parser")

allDetails = soup.find_all("div",{"class":"details"})
allCaptions = soup.find_all("address")

prices = []
addresses = []
rooms = []
suburbs = []


for caption in allCaptions:
    address = caption.text.replace("\n","")
    suburb = caption.find_all("span",{"class":"suburb oneline"})
    


for item in allDetails:
    price = item.find("span",{"class":"pricetext"}).text.replace("\n","").replace(" ","")
    prices.append(price)