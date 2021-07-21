import requests
import pandas as pd
from bs4 import BeautifulSoup

stockprices = []


def get_stock_prices(stockname):
    stockname = stockname.upper()
    URL = "https://finance.yahoo.com/quote/" + uniquestock + "/history"
    #currently defaults to exactly one year behind the current date, need to implement feature to dynamically find beginning of each company's price history so that max amount of data can be used for predictions
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    goodsoup = soup.prettify()
    endofdaystockprices = goodsoup.find_all('td', attrs = {'class':'ts5'})
    #might need ts0 and change row[0] to row[5]
    for i in endofdaystockprices:
        row = i.find_all('td')
        stockprices.append(row[0].text.strip())



# part of the program where it takes in the file input which contains all the specified stocks, and iterates through the process of getting stock prices for each one + calculating regression & predicting next day stock values
stocknames = open("differentstocks.txt", "r")
while stocknames:
    uniquestock = stocknames.readline()
    get_stock_prices(uniquestock)
    
    





