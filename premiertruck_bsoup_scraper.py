from bs4 import BeautifulSoup
import requests
import string
import csv

def scrape_data(truck_url):
    session1 = requests.Session()
    session1.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
    url = 'https://'+truck_url
    # print(url)
    page = session1.get(url)
    
    soup = BeautifulSoup(page.content,'lxml')
    all_data = soup.find('section',id='content')
    seller_details = all_data.find('div',class_='col-sm-12 col-md-7')
    image_details = all_data.find('div',class_='swiper-wrapper')
    # print(all_data)

    # data_scraped
    truck_name = all_data.find('div',class_='title').h1.text
    price = all_data.find('h3',itemprop='priceCurrency').text
    location = all_data.find('div',id='vdp-location-bubble').a.span.text
    seller_name = seller_details.find('h3').text
    seller_address = seller_details.find('p').text
    # print(seller_address)
    image_url = image_details.find('a')['href'].split('//')[1]
    print(truck_name,price,location,seller_name,seller_address,image_url)
    writer.writerow([truck_name,price,location,seller_name,seller_address,image_url])
   
page = 1

for page in range(100):
    session = requests.Session()
    session.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"})
    url = 'https://www.premiertruck.com/inventory.aspx?_vstatus=3,4,5&_new=true&_vehicletype=truck&_page{0}'.format(page)
    source = session.get(url)
    # print(source.content)
    soup = BeautifulSoup(source.content,'lxml')

    csv_file = open('truck_data.csv','w')
    writer = csv.writer(csv_file)
    writer.writerow(['TRUCK NAME','PRICE','LOCATION','SELLER NAME','ADDRESS','PHOTOS'])
    for each_truck in soup.find_all('div',class_='ml-0 ml-lg-5 pt-4 pb-2 border-bottom'):

        truck_url = each_truck.find('h2',class_='color m-0 ebiz-vdp-title').a['href'].split('//')[1]
        # print(truck_url)
        scrape_data(truck_url)
    page = page + 1