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
allAddresses = soup.find_all("address")
allIcons = soup.find_all("div",{"class":"icons"})

prices = []
suburbs = []
streets = []
bedrooms = []
bathrooms = []
garages = []


for address in allAddresses:
    suburb = address.find_all("span")[0].text
    street = address.find_all("span")[1].text
    suburbs.append(suburb)
    streets.append(street)


for item in allDetails:
    price = item.find("span",{"class":"pricetext"}).text.replace("\n","").replace(" ","")
    prices.append(price)
    
for item in allIcons:
    bedroom = item.find_all("span")[0].text
    bathroom = item.find_all("span")[1].text
    garage = item.find_all("span")[2].text
    bedrooms.append(bedroom)
    bathrooms.append(bathroom)
    garages.append(garage)
    