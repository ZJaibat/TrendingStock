from selenium import webdriver
import pandas as pd
import time

Tickers = []
Names = []
Prices = []
Change = []
mktcap = []



# Defines the website and gives file path to ChromeDriver.
website = 'https://finance.yahoo.com/trending-tickers'
PATH  = '/Users/zakariah/Documents/Code/chromedriver'
driver = webdriver.Chrome(PATH)
driver.get(website)



# Locating the table storing it in variable called stocks.
tickers = driver.find_elements_by_xpath('//tbody/tr/td[1]/a')
name = driver.find_elements_by_xpath('//table/tbody/tr/td[2]')
prices = driver.find_elements_by_xpath('//tbody/tr/td[3]')
change = driver.find_elements_by_xpath('//table/tbody/tr/td[6]')
mkt_cap = driver.find_elements_by_xpath('//table/tbody/tr/td[8]')


#converts all the inforamtion to a text string to be displayed
Stock_result = []

for i in range(len(prices)):
    temporary_data={'Ticker': tickers[i].text,
                   'Name': name[i].text,
                   'Price': prices[i].text,
                   'Change': change[i].text,
                   'mktcap': mkt_cap[i].text}
    Stock_result.append(temporary_data)


#Trending_Stock=[]
#Trending_Stock.append(tempdata)



# adds the cleaned data to a CSV and exports it.
df_data = pd.DataFrame(Stock_result)
df_data.to_csv('Stocks.csv', index=False)



print("Todays top 5 trending stocks are: \n")
print(df_data.head(5))
print("\n NOTE: A more extensive list is located in the same folder as this program. :)")


# tells the program to wait before closing.
time.sleep(15)

# closes and quits the program.
driver.close()
driver.quit()
