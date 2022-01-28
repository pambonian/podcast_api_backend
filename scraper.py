from bs4 import BeautifulSoup
import requests


source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')



# for item in soup.findAll('item'):
for item in soup.findAll('item'):


    site_title = item.find('title').text
    itunes_episode = item.find('itunes:episode').text
    itunes_title = item.find('itunes:title').text
    itunes_author = item.find('itunes:author').text
    itunes_duration = item.find('itunes:duration').text
    itunes_explicit = item.find('itunes:explicit').text
    itunes_summary = item.find('itunes:summary').text
    cover_art = item.find('itunes:image')
    media = item.find('enclosure')['url']

    item_results = [
        site_title, itunes_episode, itunes_title, itunes_author, itunes_duration, itunes_explicit, itunes_summary, cover_art, media
    ]

    print(item_results)

try:

    print()

except Exception as e:
        
    site_title = None
    itunes_episode = None
    itunes_title = None
    itunes_author = None
    itunes_duration = None
    itunes_explicit = None
    cover_art = None
    media = None
