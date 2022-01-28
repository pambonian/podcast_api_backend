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

# pull embedded yt-video's source as html
vid_src = item.find('iframe', class_='youtube-player')
# print(vid_src)

# pull value of the source attribute from the tag
vid_src = item.find('iframe', class_='youtube-player')['src']

# parse the string to grab the value of the video (splits on all forward slash)
vid_id = vid_src.split('/')
# print(vid_id)

# specify index of split for everything after the fourth index of the / split
vid_id = vid_src.split('/')[4]
# print(vid_id)

# grab the video id from the split info returned
vid_id = vid_id.split('?')[0]

# create a new youtube link using the id you got from the parsing
yt_link = f'https://youtube.com/watch@v={vid_id}'
# print(yt_link)

#  LOOPING OVER EVERYTHING WITH WHAT YOU LEARNED ABOVE

# pull all titles
for item in soup.find_all('item'):
    headline = item.title.text
    # print(headline)