from bs4 import BeautifulSoup
import requests
import csv
import time
import string

def scrape_data(url,count):
    session = requests.session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
    source = session.get(url)
    soup = BeautifulSoup(source.content,'lxml')
    all_data = soup.find('div',class_='sectFrst bgc1 pr')

    try:
        name = all_data.find('h1',class_='bo').text
    except Exception as identifier:
        name = 'not provided'
    
    try:
        price=all_data.find('span',class_='prc-tip').text
    except Exception as identifier:
        price = 'not provided'

    try:
        brochure= all_data.find('span',class_='lh26 pdinb pdgR20').a['href']
    except Exception as identifier:
        brochure = 'not provided'
    
    try:
        phoneNo=all_data.find('span',class_='bo duet').text
    except Exception as identifier:
        phoneNo = 'not provided'
    
    
    seller_details = all_data.find('div',class_='rdsp')

    try:
        seller_name = seller_details.find('a',class_='pcmN bo').text
    except Exception as identifier:
        seller_name = 'not provided'
    
    try:
        seller_address = seller_details.find_all('span',class_='color1 dcell verT fs13').span.text + seller_details.find_all('span',class_='color1 dcell verT fs13').text
    except Exception as identifier:
        seller_address = 'not provided'
    

    print(count,name,price,brochure,phoneNo,seller_name,seller_address)

page_num = 1
count = 1


while True:

    if page_num>100:
        break
    
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
    url = 'https://dir.indiamart.com/search.mp?ss=polycom&cq=mumbai&&pg={0}&frsc=15'.format(page_num)

    source = session.get(url)
    soup = BeautifulSoup(source.content,'lxml')

    all_data = soup.find('ul',class_='wlm')

    # csv_file = open('indiamart.csv','w')
    # writer = csv.writer(csv_file)
    
    for each_data in all_data.find_all('div',class_='l-cl b-w'):
        try:
            url = each_data.find('div',class_='rht pnt').a['href']
            # print(url)
            count = count + 1
            scrape_data(url,count)

        except Exception as identifier:
            pass

    page_num = page_num + 1
    # print(page_num)
    print('\n')


