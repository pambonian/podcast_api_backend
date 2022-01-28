from bs4 import BeautifulSoup
import requests

source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')

for item in soup.findAll('item'):
    try:
        site_title = item.title.text
        itunes_episode = item.find('itunes:episode')
        itunes_title = item.find('itunes:title')
        itunes_author = item.find('itunes:author')
        itunes_duration = item.find('itunes:duration')
        itunes_explicit = item.find('itunes:explicit')
        itunes_summary = item.find('itunes:summary')
        cover_art = item.find('itunes:image')
        media = item.find('enclosure')
    except Exception as e:
        site_title = None
        itunes_episode = None
        itunes_title = None
        itunes_author = None
        itunes_duration = None
        itunes_explicit = None
        itunes_summary = None
        cover_art = None
        media = None

item_results = item



print(item_results([
    site_title, 
    itunes_episode,
    itunes_title, 
    itunes_author, 
    itunes_duration, 
    itunes_summary,
    cover_art, 
]))




# 
# print(image_link)






# item = soup.find('item')
# print(item)




# for content in soup.find_all('article'):

#     headline = article.h2.a.text
#     print(headline)

#     summary = article.find('div', class_='entry-content').p.text
#     print(summary)

#     try:
#         video_src = article.find('iframe', class_='youtube-player')['src']
#         vid_id = video_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]
#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None   
    
#     print(yt_link)
#     print()

    

