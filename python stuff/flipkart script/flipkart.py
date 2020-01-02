from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
import os
import time
import csv
import lxml
import io
import re

url_list = []

base_url = 'https://www.flipkart.com'

init_url = 'https://www.flipkart.com/search?q=united%20colors%20of%20benetton'
rqst = requests.get(init_url)
soup = BeautifulSoup(rqst.text, 'lxml')
#pages = soup.find("")
with io.open("file1.csv","w",encoding="utf8") as f1:
    #f1.write("title,mrp,sellprice,discount,averageratings,rating_summary,style\n")
    f1.write("title,mrp,sellprice,discount,average,rating_summary,style,url\n")
div_data = soup.find("div",{"class":"_2zg3yZ"})
span_list = soup.select('div._2zg3yZ span')
total_pages = int(span_list[0].text.split(' ')[3])

for i in range(1,52):
    print('Crawling Page {}'.format(i))
    search_url = 'https://www.flipkart.com/search?q=united%20colors%20of%20benetton&page={}'.format(i)
    search_rqst = requests.get(search_url)
    #print(search_rqst.url)
    #print(search_rqst.status_code)
    soup = BeautifulSoup(search_rqst.text, 'lxml')
    links = soup.find_all("a", {"class":"_2mylT6"})
    for link in links:
        found = link.get('href')
        final_url = base_url + found 
        url_list.append(final_url)
    #time.sleep(1)

print(len(url_list))

for url in url_list:
    #url="https://www.flipkart.com/united-colors-benetton-boys-casual-shirt/p/itmehvu7b4ah3cgn?pid=SHTEHVU7BREDMDZD&lid=LSTSHTEHVU7BREDMDZDTEE1G9&marketplace=FLIPKART&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_0_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_0_5_na_na_na&fm=SEARCH&iid=40b30858-47d6-4ebe-b07c-7b6dc8316c4c.SHTEHVU7BREDMDZD.SEARCH&ppt=sp&ppn=sp&ssid=ky0ugextq80000001568712424503&qH=3241e26373eddaea"
    print(url + '\n')
    content = requests.get(url)
    #page_html=uClient.read()
    #uClient.close()
    soup = BeautifulSoup(content.text, 'lxml')

    #Brand=soup.find("a",{"class":"_1KHd47"})
    #Brand = Brand.text
    #print(Brand)

    title=soup.find("span",{"class":"_35KyD6"})
    if title==None:
        title='none'
        print(title)
    else:
        title=title.text.replace(',', '')
        print(title)

    mrp=soup.find("div",{"class":"_3auQ3N _1POkHg"})
    if mrp==None:
        mrp = 'Same as sellprice'
        print(mrp)
    else:
        mrp=mrp.text[1:].replace(',', '')
        print(mrp)

    sellprice=soup.find("div",{"class":"_1vC4OE _3qQ9m1"})
    if sellprice==None:
        if sellprice==None:
            sellprice=mrp
            print(sellprice)
    else:
        sellprice=sellprice.text[1:].replace(',', '')
        print(sellprice)

    discount=soup.find("div",{"class":"VGWI6T _1iCvwn _9Z7kX3"})
    if discount==None:
        discount=soup.find("div",{"class":"VGWI6T _1iCvwn"})
        if discount==None:
            discount = '0%'
            print(discount)
        else:
            discount=discount.text
            print(discount)

    else:
        discount=discount.text
        print(discount)

    averageratings=soup.find("div",{"class":"hGSR34 bqXGTW"})
    if averageratings==None:
        averageratings=soup.find("div",{"class":"hGSR34"})
        if averageratings==None:
            averageratings='none'
            print(averageratings)
        else:
            averageratings=averageratings.text
            print(averageratings)    
        #averageratings=averageratings.text
        #print(averageratings)   
        #print("none type detected")
    else:
        averageratings=averageratings.text.replace(',','')
        print(averageratings)
        

    rating_summary=soup.find("span",{"class":"_38sUEc"})
    if rating_summary==None:
        rating_summary='none'
        print(rating_summary)
    else:    
        rating_summary=rating_summary.text.replace(',', '')
        print(rating_summary)


    style=soup.find_all("div",["col col-9-12 _1BMpvA"])
    #print(style)
    for item in style:
        item = item.text.strip()
        if item.isalpha() == True:
            pass
        elif item.isdigit() == True:
            pass
        else:
            if item.isalnum() == True:
                Style = item
                print(Style)
    #if style==None:
     #   style=soup.find("li",["_3YhLQA"])
      #  style=style.text
       # print(style+ '\n')

        #i_need_element = soup.select ('a[class*="shared-components"]')
        #print("none type detected")
    #else:
     #   style=style.text
      #  print(style+ '\n')

    
    #data=title + "," +mrp+ "," + sellprice +"," + discount +"," + averageratings +"," + rating_summary + "," + style + "\n"
    #with io.open("file1.csv","a",encoding="utf8") as f1:
     #   f1.write(data)
      #  f1.close()
    
    with open('file1.csv', 'a', encoding="utf8") as csv_file:
        data = str(title) + ',' + str(mrp) + ',' + str(sellprice) + ','+ str(discount) +',' + str(averageratings) +',' + str(rating_summary) + ',' + str(Style) + ','+ url + '\n'
        csv_file.write(data)
    #time.sleep(1)
#print(len(containers))
#print(containers)
#print(soup.prettify(containers)[0])
#container=containers[0]
#print(container)


#Brand=container.find("div",{"class":"_2B_pmu"})
#print(title.text)

#Brand=container.find("a",{"class":"_2mylT6"}).string

#print(Brand)
#print(Brand)