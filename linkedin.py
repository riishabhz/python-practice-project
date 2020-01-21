from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import csv
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time 
import re
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

option = Options()

option.add_argument("user-data-dir=C:\\Users\\r.bhardwaj\\AppData\\Local\\Google\\Chrome\\User Data\\") #Extract this path from "chrome://version/"
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

#driver = webdriver.Chrome(executable_path = exec_path_driver, options = ch_options) #Chrome_Options is deprecated. So we use options instead.
#C:\Users\r.bhardwaj\AppData\Local\Google\Chrome\User Data
driver=webdriver.Chrome(chrome_options=option,executable_path=r"chromedriver.exe")


driver.get('https://www.linkedin.com/search/results/people/?keywords=Python')

page_num = 1
counter=0
while counter<50:
	page_num += 1

	for t in range(0,10):
		try:
			request=driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[{}]/div/div/div[3]/div".format(str(t))).click()
			counter+=1
			try:
				r1=driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]/span").click()
				time.sleep(2)
			except:
				pass	
		except:
			print('fail')
			pass
	driver.get("https://www.linkedin.com/search/results/people/?keywords=Python&page={}".format(page_num))
print(counter)
 

# sigin=driver.find_element_by_class_name("main__sign-in-link").click()
# time.sleep(1)
#/html/body/div/main/form/section/div[2]/input[1]

# username=driver.find_element_by_xpath('/html/body/div/main/div/form/div[1]/input').send_keys("rishabhbhardwaj24@gmail.com")
# password=driver.find_element_by_xpath('/html/body/div/main/div/form/div[2]/input').send_keys("rishabh24")
# login=driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button').send_keys(Keys.ENTER)
# time.sleep(1)

# try:
# 	check_manage_account=driver.find_element_by_xpath('/html/body/div/div[1]/section/div[2]/div/article/footer/div/div/span/button').send_keys(keys.ENTER)
# 	time.sleep(1)
# except:
# 	pass	


#https://www.creditmantri.com/diesel-price-in-gurgaon/
#https://www.creditmantri.com/petrol-price-in-gurgaon/

# driver.get('https://www.linkedin.com/search/results/people/?keywords=python')

# try:
# 	button=driver.find_element_by_xpath('/html/body/div[5]/div[4]/div[3]/div/div[2]/div/div[2]/div/div/div/div/ul/li[{}]/div/div/div[3]/div/button'.format(str(t))).click()
# 	time.sleep(3)
# except:
# 	pass	




