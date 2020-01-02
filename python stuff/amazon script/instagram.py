from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time 
import re

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

driver=webdriver.Chrome(chrome_options=option,executable_path=r"chromedriver.exe")

url = 'https://www.instagram.com/p/B5hTYCZAZfd/'
driver.get(url)


for i in range(0,50):
	load_more_comment = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li/div/button/span').click()
	time.sleep(2);

#load_more_comment.click()    


with open("instagramcomments.csv","w",encoding="utf8") as f1:
    #f1.write("title,mrp,sellprice,discount,averageratings,rating_summary,style\n")
    f1.write("id,comment\n")

# approximately 12 comments per page

#print("final click count: " + str(click_count) + "; should yield roughly " + str(click_count*12) + " comments")


for t in range(0,100):

	#caption=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
	#caption=caption.text
	#print(caption)

	try:
		instagramidxpath=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/h3/a'.format(str(t)))
		href=instagramidxpath.get_attribute('href')
		print(href)
	except:
		pass

	try:
		comment=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[{}]/div/li/div/div[1]/div[2]/span'.format(str(t)))
		comment=comment.text
		print(comment)
	except:
		pass	
	print('\n')

	#with open('instagramcomments.csv','a', encoding="utf8") as csv_file:
    #        data = str(href)+ ',' + str(comment) +'\n'
    #        csv_file.write(data)		



