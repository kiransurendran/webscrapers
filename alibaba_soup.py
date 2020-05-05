import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=raspberry+pi+3').text
soup = BeautifulSoup(page,'lxml')

csv_file = open('alibabanew.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Price','Min-order','URL'])


products = soup.find('div',class_='organic-list app-organic-search__list')
for product in products.find_all('div',class_='organic-list-offer-outter J-offer-wrapper'):
    title = product.find('p',class_='organic-gallery-title__content').text
    price = product.find('p',class_='gallery-offer-price').text
    min_order = product.find('p',class_='gallery-offer-minorder').text
    try:
        prod_link = product.find('a',class_='organic-gallery-title one-line')['href']
    except Exception as identifier:
        prod_link = None
    
    csv_writer.writerow([title,price,min_order,prod_link])

csv_file.close()

# print(prod_link)
# print(price)
# print(title)
# print(soup)
