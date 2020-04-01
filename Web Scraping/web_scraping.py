from bs4 import BeautifulSoup
import requests

# Scrape the Webpage to search for each Title,
# Summary and the Youtube link
# and save in a CSV file

source=requests.get('https://coreyms.com').text
soup=BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    try:

        headline=article.h2.a.text
        print(headline)

        para=article.find('div',class_='entry-content').p.text
        print(para)

        vid_src=soup.find('iframe',class_='youtube-player')['src']
        src_id=vid_src.split("/")[4]
        src_id=src_id.split('?')[0]
        link=f'https://www.youtube.com/watch?v={src_id}'
    except Exception as e:
        link=None
    print(link)
    print()
