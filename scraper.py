from bs4 import BeautifulSoup
import requests


source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

# pull a title
item = soup.find('item')
headline = item.title.text
# print(headline)

# pull all titles
for item in soup.find_all('item'):
    headline = item.title.text
    # print(headline)

# pull embedded yt-video's source
vid_src = item.find('iframe', class_='youtube-player')['src']
# print(vid_src)