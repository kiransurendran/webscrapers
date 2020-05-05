from bs4 import BeautifulSoup
import requests
import csv  
# import json 

source = requests.get('https://coreyms.com').text
soup = BeautifulSoup(source,'lxml')

 
csv_file = open('data.csv','w')
# json_file =  open('data.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video-link'])

# article = soup.find('article')
for article in soup.find_all('article'):
    headline = article.h2.a.text
    description = article.find('div',class_='entry-content').p.text
    try:
        # pass
        yt_link = article.find('iframe',class_='youtube-player')['src'].split('/')[4].split('?')[0]
        youtube_link = 'www.youtube.com/watch?v={0}'.format(yt_link)
    except Exception as identifier:
        youtube_link = None
    
    # print(headline)
    # print(description)
    # print(youtube_link)
    print()
    csv_writer.writerow([headline,description,youtube_link])

csv_file.close()   



