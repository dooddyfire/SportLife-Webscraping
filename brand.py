from bs4 import BeautifulSoup 
import requests 
import pandas as pd 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pyperclip

import time

#url = 'https://www.mottoauction.com/Auction/Code/X1FBK019'

brand_name = input('Enter your brand name : ')
url = "https://www.sportforlife.co.th/brand/{}?order=recommend&limit=100".format(brand_name)


res = requests.get(url)

soup = BeautifulSoup(res.content,'html.parser')

prod_link_lis = [ c['href'] for c in soup.find_all('a',{'class':'product-item-link'})]

title_lis = []
img_lis = []
price_lis = []
desc_lis = []

for i in prod_link_lis: 
    resx = requests.get(i)
    soupx = BeautifulSoup(resx.content,'html.parser')

    try:
        title = soupx.find('title').text
        print(title)
    except: 
        title = " "
        print(title)

    title_lis.append(title)

    try:
        main_img = [ e['data-thumb']for e in soupx.find('div',{'class':'six'}).find('div',{'class':'goods__images'}).find_all('a') ]
        print(main_img)
    except: 
        main_img = " "
        print(main_img)    

    input_img = "\n".join(main_img)
    img_lis.append(input_img)  

    try:
        price = soupx.find('div',{'class':'_price'}).text 
        print(price)
    except: 
        price = " "
        print(price)       

    price_lis.append(price)

    try:
        desc = soupx.find('div',{'data-tab':'detail'}).text 
        print(desc)
    
    except: 
        desc = " "
        print(desc)
    
    desc_lis.append(desc)

df = pd.DataFrame()
df['Product Name'] = title_lis 
df['Product Link'] = prod_link_lis
df['Image'] = img_lis 
df['Price'] = price_lis 
df['Description'] = desc_lis 

df.to_excel('{}.xlsx'.format(brand_name))