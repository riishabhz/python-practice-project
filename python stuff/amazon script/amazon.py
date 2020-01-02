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



# you have to use remote, otherwise you'll have to code it yourself in python to 
# dynamically changing the system proxy preferences
#driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities)

#driver = webdriver.Chrome(desired_capabilities=capabilities)

total = []
p=[]

driver=webdriver.Chrome(chrome_options=option,executable_path=r"chromedriver.exe")

with open("amazonexcel.csv","w",encoding="utf8") as f1:
    #f1.write("title,mrp,sellprice,discount,averageratings,rating_summary,style\n")
    f1.write("title,price,mrp,code,url\n")

for num in range(1,295):
    print('Crawling Page {}\n'.format(str(num)))
#https://www.amazon.in/s?k=united+colors+of+benetton&i=apparel&page=100
    init_url = 'https://www.amazon.in/s?k=united+colors+of+benetton&i=fashion&page={}'.format(num)
    driver.get(init_url)

    for t in range(1,60):
    #time.sleep(5)
        #print(t)
        try:
                                  #19/11/2019              #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[19]/div/span/div/div/div[2]/div[3]/div/div/div[1]/h2/a/span
                                                #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[50]/div/span/div/div/div[2]/div[3]/div/div/div[1]/h2/a/span
                                                #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[8]/div/span/div/div/div[2]/div[3]/div/div/div[1]/h2/a/span
                                                #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[7]/div/span/div/div/div[2]/div[3]/div/div/div[1]/h2/a/span
            titles=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{}]/div/span/div/div/div[2]/div[3]/div/div[1]/h2/a/span'.format(str(t)))
            titles=titles.text
            print(titles)
            #titles=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[3]/div/div/div[1]/h2/a/span'.format(str(t)))
            #print(titles)
            #titles = titles.text
            #titles=titles.text
            
            #total.append(title)
           
        except:
             try:
                titles=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{}]/div/span/div/div/div[2]/div[3]/div/div/div/h2/a/span'.format(str(t)))
                titles=titles.text
                print(titles)
             except:
                titles='Sponsored'
                pass
            #titles=titles.text
            #print(titles.text)
            #titles='Sponsored'
            #pass
            #exit()  
        try:    
        	#price=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div[1]/div/div/span[3]/span[2]/span[2]'.format(str(t)))
            price=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[1]/span[2]/span[2]'.formay(str(t)))
            price=price.text
            price = re.findall('\d+', price)
            try:
                price = price[0]+price[1]
            except:
                price = price[0]
                print('Price : {}'.format(price))
            #p.append(price)
        except:
            try:
                #price=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div[1]/div/div/a/span/span[2]/span[2]'.format(str(t)))
                                                   #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[22]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[1]/span[2]/span[2]
                             #19/11/2019           #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[49]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[1]/span[2]/span[2] 
                price=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[1]/span[2]/span[2]'.format(str(t)))
                price=price.text
                price = re.findall('\d+', price)
                try:
                	price = price[0]+price[1]
                except:
                	price = price[0]
                print('Price : {}'.format(price))
                #p.append(price)
       	    except:
                price = 'Sponsored'
                pass
        
        try:
            #mrp=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div[1]/div/div/a/span[2]/span[2]'.format(str(t)))
                                              #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[55]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[2]/span[2]
            mrp=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[2]/span[2]'.format(str(t)))
            mrp=mrp.text
            mrp = re.findall('\d+', mrp)
            try:
            	mrp = mrp[0]+mrp[1]
            except:
            	mrp = mrp[0]
            print('Price : {}'.format(mrp))

        except:
            mrp='same as sellprice'
            pass

        try:
            #appareal#value=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[3]/div/div[1]/h2/a'.format(str(t)))
                                                #//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[55]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[2]/span[1]
            #v                                 //*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[55]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a/span[2]/span[2]
            value=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]/div[{}]/div/span/div/div/div[2]/div[4]/div/div/div[1]/div/div/a'.format(str(t)))
        #value=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[{}]/div/span/div/div/div[2]/div[3]/div/div[1]/h2/a'.
            href=value.get_attribute('href')
            print(href)
            code=href
            code=href.split('/')
            code=code[-2]
            print(code)
        except:
            href = 'Sponsored'
            code = 'Sponsored'
            pass
        print('\n')



        #print(titles)
        #print(price)
        #print(mrp)
        #print(code[-2])
        #print(href)

        
            #print('same as sellprice')         
        with open('amazonexcel.csv', 'a', encoding="utf8") as csv_file:
            data = str(titles)+ ',' + str(price) + ',' + str(mrp) + ',' + str(code)+ ',' + str(href)+'\n'
            csv_file.write(data)

with open('amazonexcel.csv', 'r') as inp, open('final.csv', 'w', newline='') as out:
    writer = csv.writer(out)
    for row in csv.reader(inp):
    	if row[1] != "Sponsored":
            writer.writerow(row)


#print(len(total))
#print(len(p))
#driver.exit()
#exit()
#mrp=driver.find_element_by_class_name("a-price-whole")
#print(mrp.text)

#title=driver.find_element_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[1]/div[10]/div/span/div/div/div[2]/div[4]/div/div[1]/div/div/span[3]/span[2]/span[2]')
#print(title.text)
