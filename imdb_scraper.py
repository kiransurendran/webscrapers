from bs4 import BeautifulSoup
import requests
import csv

page = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250').text
# print(page.content)
soup = BeautifulSoup(page,'lxml')
# print(soup)
csv_file = open('movies.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name','Year','Rating','URL'])

movie = soup.find('tbody',class_='lister-list')
count = 1
for tr in movie.find_all('tr'):

    name = tr.find('td',class_='titleColumn').a.text
    year = tr.find('span',class_='secondaryInfo').text
    rating = tr.find('td',class_='ratingColumn imdbRating').text
    link = tr.find('td',class_='titleColumn').a['href']
    mv_link = 'imdb.com{0}'.format(link)
    count = count + 1
    print(count,name,year,rating,mv_link)
    csv_writer.writerow([name,year,rating,mv_link])  

csv_file.close()
