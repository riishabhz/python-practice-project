from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time 
import re
from selenium.common.exceptions import NoSuchElementException

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

driver=webdriver.Chrome(chrome_options=option,executable_path=r"chromedriver.exe")

#https://www.creditmantri.com/diesel-price-in-gurgaon/
#https://www.creditmantri.com/petrol-price-in-gurgaon/

driver.get('https://www.creditmantri.com/diesel-price-in-gurgaon/')
with open("petrolprices.csv","w",encoding="utf8") as f1:
    f1.write("date,price\n")


t=0
while True:
	t+=1
	try:
		date=driver.find_element_by_xpath('//*[@id="trigger-offers"]/div[1]/div[1]/div[1]/div[3]/ul/li[{}]/div/div/div[1]'.format(str(t)))
		date=date.text
		print(date)
													#//*[@id="trigger-offers"]/div[1]/div[1]/div[1]/div[3]/ul/li[1]/div/div/div[2]
		price=driver.find_element_by_xpath('//*[@id="trigger-offers"]/div[1]/div[1]/div[1]/div[3]/ul/li[{}]/div/div/div[2]'.format(str(t)))
		price=price.text
		print(price)
		#data=date + ',' + price + '\n'
		#csv_file.write(data)
	except:
		break


	try:
		button=driver.find_element_by_xpath('//*[@id="trigger-offers"]/div[1]/div[1]/div[2]/a')
		button.click()
	except:
		pass
	with open('petrolprices.csv', 'a', encoding="utf8") as csv_file:
            #data = str(titles)+ ',' + str(price) + ',' + str(mrp) + ',' + str(code)+ ',' + str(href)+'\n'
            data=str(date) + ',' + str(price) + '\n'
            csv_file.write(data)
			
			#csv_file.write(data)	

