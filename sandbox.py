from bs4 import BeautifulSoup
import requests


# for item in soup.findAll('item'):

class Item:
    def __init__(self, site_title, episode_number, title, author,
        duration, explicit, summary, image, audio_link,
        ):

        source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
        soup = BeautifulSoup(source, 'lxml')

        for item in soup.findAll('item'):
    
            self.site_title = item.find('title').text
            self.episode_number = item.find('itunes:episode').text
            self.title = item.find('itunes:title').text
            self.author = item.find('itunes:author').text
            self.duration = item.find('itunes:duration').text
            self.explicit = item.find('itunes:explicit').text
            self.summary = item.find('itunes:summary').text
            self.image = item.find('itunes:image')
            self.audio_link = item.find('enclosure')['url']

    def populate(self):
        return '{} {} {} {} {} {} {} {}'

print(Item.populate)    

   
