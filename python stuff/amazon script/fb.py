from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
driver.get('https://mobile.facebook.com/BenettonIndia/photos/a.301209163637128/770217696736270')
