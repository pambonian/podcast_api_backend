from bs4 import BeautifulSoup
import requests


source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

# for article in soup.find_all('div', class_='article'):
#     headline = article.h2.a.text
#     print(headline)

# # pull a title
# item = soup.find('item')
# headline = item.title.text
# # print(headline)

# pull all titles
# for item in soup.find_all('item'):
    
    # try:
item = soup.find('item')

headline = item.title.text

description = soup.find('itunes:summary').text

datepub = item.pubDate

sitelink = item.link.text

author = soup.find('itunes:author').text

image_link = item.itunes

item_results = [headline, description, datepub, sitelink, author, image_link]

print(item_results)


# print(sitelink)
    # except Exception as e:
    #     headline = None
    #     description = None
    #     datepub = None
    #     author = None
    #     sitelink = None

# # pull embedded yt-video's source as html
# vid_src = item.find('iframe', class_='youtube-player')
# # print(vid_src)

# # pull value of the source attribute from the tag
# vid_src = item.find('iframe', class_='youtube-player')['src']

# # parse the string to grab the value of the video (splits on all forward slash)
# vid_id = vid_src.split('/')
# # print(vid_id)

# # specify index of split for everything after the fourth index of the / split
# vid_id = vid_src.split('/')[4]
# # print(vid_id)

# # grab the video id from the split info returned
# vid_id = vid_id.split('?')[0]

# # create a new youtube link using the id you got from the parsing
# yt_link = f'https://youtube.com/watch@v={vid_id}'
# print(yt_link)

#  LOOPING OVER EVERYTHING WITH WHAT YOU LEARNED ABOVE

# # pull all titles
# for item in soup.find_all('item'):
#     headline = item.title.text
    # print(headline)

# try/accept for any missing loop items

# for article in soup.find_all('article'):
#     headline = article.h2.a.text
#     # print(headline)

#     summary = article.find('div', class_='entry-content').p.text
#     # print(summary)

#     try:
#         vid_src = article.find('iframe', class_='youtube-player')['src']

#         vid_id = vid_src.split('/')[4]
#         vid_id = vid_id.split('?')[0]

#         yt_link = f'https://youtube.com/watch?v={vid_id}'
#     except Exception as e:
#         yt_link = None

    # print(yt_link)


# # TUT CODE
# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('http://coreyms.com').text

# soup = BeautifulSoup(source, 'lxml')
# # open csv file:
# csv_file = open('cms_scrape.csv', 'w')
# # set up csv file:
# csv_writer = csv.writer(csv_file)
# write headers for csv file:
# csv_writer.writerow(['headline', 'summary', 'video_link'])
# find all articles:
# for article in soup.find_all('article'):
#     headline = article.h2.a.text
    # print(headline)
# find the text in p tags for divs with class entry content:
    # summary = article.find('div', class_='entry-content').p.text
    # print(summary)
# ignore issues when looping when missing elements are detected using try/except:
    # try:
    #     vid_src = article.find('iframe', class_='youtube-player')['src']

    #     vid_id = vid_src.split('/')[4]
    #     vid_id = vid_id.split('?')[0]

    #     yt_link = f'https://youtube.com/watch?v={vid_id}'
    # except Exception as e:
    #     yt_link = None

    # print(yt_link)

    # print()
# write to csv:
    # csv_writer.writerow([headline, summary, yt_link])
# close csv:
# csv_file.close()