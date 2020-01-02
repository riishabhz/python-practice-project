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

url = 'https://www.instagram.com/p/B58g_LqAozY/'
driver.get(url)

with open("instagramcomments.csv","w",encoding="utf8") as f1:
    f1.write("id,comment\n")


t=0
with open("instagramcomments.csv", "a", encoding="utf8") as csv_file:
    while True:
        #time.sleep(0.5)
        t += 1
        print(t)
        try:
            instagramidxpath=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[{}]/div/li/div/div/div[2]/h3/a'.format(str(t)))
            href=instagramidxpath.get_attribute('href')
            print(href)
            comment=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/ul[{}]/div/li/div/div[1]/div[2]/span'.format(str(t)))
            comment=comment.text
            print(comment)
            data = href + ',' + comment + '\n' 
            csv_file.write(data)
            #time.sleep(0.2)
        except:
            break
        
        try:
            load_more_comment = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/li/div/button/span')
            load_more_comment.click()
            time.sleep(3)
        except:
            pass