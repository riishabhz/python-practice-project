#https://www.myntra.com/united-colors-of-benetton-tshirts-men?p=11


from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import csv

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 2 
})

driver=webdriver.Chrome(chrome_options=option,executable_path=r"chromedriver.exe")

#desktopSearchResults > div.search-searchProductsContainer.row-base > section > ul > li:nth-child(4) > a > div.product-productMetaInfo > h3
#title=driver.find_elements_by_('product-price')
#print(title)
#exit()

#driver.get('https://www.myntra.com/united-colors-of-benetton')
driver.get('https://www.myntra.com/united-colors-of-benetton')
with open("file1.csv","w",encoding="utf8") as f1:
    #f1.write("title,mrp,sellprice,discount,averageratings,rating_summary,style\n")
    f1.write("title,price,mrp,discount,code,url\n")

total_pages = driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/div[2]/ul/li[1]')
total_pages = total_pages.text
total_pages = total_pages.split(' ')
total_pages = total_pages[-1]
total_pages = int(total_pages)

for page in range(1, total_pages):
	print('Page Number : {}'.format(str(page)))
	driver.get("https://www.myntra.com/united-colors-of-benetton?p={}".format(str(page)))
	#driver.get("https://www.myntra.com/united-colors-of-benetton?p={}".format(str(page)))
	for t in range(1,51):
		title=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a/div[2]/h4[1]/a'.format(str(t)))
		title = title.text
		try:
			price=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a/div[2]/div/span[1]/span[1]'.format(str(t)))
			price = price.text
		except:
			price=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a/div[2]/div'.format(str(t)))
			price = price.text
		try:
			mrp=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a/div[2]/div/span[1]/span[2]'.format(str(t)))
			mrp = mrp.text	
		except:
			mrp = 'Same as Selling Price'
		try:
			discount=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a/div[2]/div/span[2]'.format(str(t)))
			discount = discount.text
		except:
			discount = 'No Discount'
		value=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[{}]/a'.format(str(t)))
		href = value.get_attribute('href')
		
		code=href
		code=href.split('/')
		code = code[-2]
		print(title)
		print(price)
		print(mrp)
		print(discount)
		print(code)	
		print(href)

		with open('file1.csv', 'a', encoding="utf8") as csv_file:
			data = str(title) + ',' + str(price) + ',' + str(mrp) + ','+ str(discount) +',' + str(code) +',' + str(href) + '\n'
			csv_file.write(data)


		
driver.close()
#//*[@id="desktopSearchResults"]/div[2]/section/ul/li[3]/a/div[2]/h4[1]/a
# //*[@id="desktopSearchResults"]/div[2]/section/ul/li[2]/a/div[2]/h4[1]
#print(len(title))
#//*[@id="desktopSearchResults"]/div[2]/section/ul/li[3]/a/div[2]/div/span[1]/span[1]#
#//*[@id="desktopSearchResults"]/div[2]/section/ul/li[2]/a/div[2]/div  
#link=driver.find_element_by_xpath('//*[@id="desktopSearchResults"]/div[2]/section/ul/li[1]/a/@href')
#print(link.text)
#links=driver.find_element_by_link_text('')