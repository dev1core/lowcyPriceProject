import urllib.request

import datetime
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

#Open File
from matplotlib import dates

file_path = 'C:/Users/Documents/GitProjects/lowcyPriceProject/lowcy_price.txt'
readFile = open(file_path, 'r').read()
priceMin = -1.0
priceMax = -1.0
price = 0.0
dateTimeList = []

priceTime = readFile.split("\n")

for p in priceTime:
    pSplited = p.split(";")
    price = float(pSplited[0])
    if priceMin == -1.0:
        priceMin = price
    elif priceMax == -1.0:
        priceMax = price
    else:
        if price > priceMax:
            priceMax = price
        if price < priceMin:
            priceMin = price

    hours, minutes, seconds = pSplited[1].split(":")
    currDate = datetime.time(int(hours), int(minutes), int(seconds))

    dateTimeList.append(dates.date2num(currDate))

#   Range of scales between freezing to boiling water
dateList = dates.date2num(dateTimeList)  # X axis presented date
price = [priceMin, priceMax]  # Y axis presented price

plt.title('Present Lowcy Gier Price / Date')
plt.xlabel('date time')
plt.ylabel('PLN')

plt.xlim(priceMin, priceMax)  # try commenting this out...
plt.grid(True)

plt.plot(dateList, price)
plt.show()