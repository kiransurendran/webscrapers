from selenium import webdriver
from bs4 import BeautifulSoup
import csv
from time import sleep

csv_file = open('truck_data.csv','w')
writer = csv.writer(csv_file)
writer.writerow(['Name','Price','Location','Pictures','Seller','Details'])

def parse_truck_data(url):
    # pass
    driver = webdriver.Chrome('/home/kiran/virtual_workspace/web_drivers/chromedriver')
    driver.get(url)
    sleep(2)
    soup = BeautifulSoup(driver.page_source,'lxml')
    all_data = soup.find('div',class_='clearfix').section

    # data_scraped
    truck_name = all_data.find('div',class_='title').text
    price = all_data.find('h3',itemprop='priceCurrency').text
    location = all_data.find('div',id='vdp-location-bubble').a.span.text
    all_pictures = all_data.find('div',class_='swiper-container swiper-photos-thumbs swiper-container-horizontal')
    picture_link = []
    seller_address = []
    
    for picture in all_pictures.find_all('img'):
            picture_link.append(picture.find('img')['src'])
    
    seller_details = all_data.find('div',class_='col-sm-12 col-md-7').p

    for address in seller_details:
        seller_address.append(address.find('p').text)
    
    all_details = all_data.find('div',class_='row row-height nomargin')
    details = []

    for det in all_details.find_all('ul',class_='ml-5 subinfo'):
        details.append(det.find_all('li').text)

    writer.writerow([truck_name,price,location,picture_link,seller_address,details])




    # price = all_data.find('h3',itemprop='priceCurrency').text
    # price = all_data.find('h3',itemprop='priceCurrency').text
    # price = all_data.find('h3',itemprop='priceCurrency').text
    # price = all_data.find('h3',itemprop='priceCurrency').text



page_no = 1

for page_no in range(5):

    url = 'https://www.premiertruck.com/inventory.aspx?_vstatus=3,4,5&_new=true&_vehicletype=truck&_page={0}'.format(page_no)

    browser = webdriver.Chrome('/home/kiran/virtual_workspace/web_drivers/chromedriver')
    browser.get(url)
    sleep(2)


    soup = BeautifulSoup(browser.page_source,'lxml')
    all_trucks = soup.find('div',id='srp-vehicle-list')

    for truck in all_trucks.find_all('div',class_='srp-vehicle-block clearfix'):
        truck_url = truck.find('h2',class_='color m-0 ebiz-vdp-title').a['href'].split('//')[1]
        sleep(1)
        # browser.close()
        parse_truck_data(truck_url)
        # print(truck_url)
        # browser.find_element_by_xpath("//h2[@class='color m-0 ebiz-vdp-title']").click()

    # sleep(1)
    # browser.close()

    # for each_url in truck_url:
    #     parse(each_url)
csv_file.close()
# print(truck_url)



