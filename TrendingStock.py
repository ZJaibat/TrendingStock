from distutils.util import change_root
from requests import RequestException
from selenium import webdriver
import pandas as pd
import time

# Defines the website and gives file path to ChromeDriver.
website = 'https://finance.yahoo.com/trending-tickers'
PATH  = '/Users/zakariah/Documents/Code/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get(website)

# Locating the table storing it in variable called stocks.
stocks = driver.find_elements_by_tag_name('tr')

# init vairabels "dirty" for the dirty data. Others for labeling purposes.
dirty = []
lprice = []
symbol = []
name = []
pchange = []
mkt_cap = []

# adds the data from website to a local list.
for stock in stocks:
    dirty.append(stock.text)

# cleans the data and adds it to the correct list.
for i in range(1, len(dirty)):
    dirty[i] = dirty[i].replace('\n', ' ').replace('"', "").split()
    for number in range(0, len(dirty[i])):
        if number == 0:
            symbol.append(dirty[i][number])
        if number == 1:
            name.append(dirty[i][number])
        if number == 4:
            lprice.append(dirty[i][number])
        if number == 5:
            pchange.append(dirty[i][number])
        if number == 8:
            mkt_cap.append(dirty[i][number])


# adds the cleaned data to a CSV and exports it.
df = pd.DataFrame({'TICKER' : symbol, 'NAME' : name, 'PRICE' : lprice, 'CHANGED' : pchange, 'MKTCAP': mkt_cap})
df.to_csv('Stocks.csv', index=False)

print("Todays top 5 trending stocks are: \n")
print(df.head(5))
print("\n NOTE: A more extensive list is located in the same folder as this program. :)")

# tells the program to wait before closing.
time.sleep(15)

# closes and quits the program.
driver.close()
driver.quit()
