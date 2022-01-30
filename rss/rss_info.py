from bs4 import BeautifulSoup
import requests
from flask import Flask, request, jsonify
import json

source = requests.get('https://feeds.simplecast.com/T8TzwY_T').text
soup = BeautifulSoup(source, 'lxml')

item_results = []

for item in soup.findAll('item'):

    site_title = item.find('title').text
    itunes_episode = item.find('itunes:episode').text
    itunes_title = item.find('itunes:title').text
    itunes_author = item.find('itunes:author').text
    itunes_duration = item.find('itunes:duration').text
    itunes_explicit = item.find('itunes:explicit').text
    itunes_summary = item.find('itunes:summary').text
    cover_art = item.find('itunes:image')['url']
    audio_link = item.find('enclosure')['url']
    pub_date = item.find('pubDate')

    item_results.append({
        
        'site_title': site_title, 
        'itunes_episode': itunes_episode, 
        'itunes_title': itunes_title, 
        'itunes_author': itunes_author, 
        'itunes_duration': itunes_duration, 
        'itunes_explicit': itunes_explicit, 
        'itunes_summary': itunes_summary, 
        'cover_art': cover_art, 
        'audio_link':audio_link,
        'pub_date':pub_date,
    })

try:

   None

except Exception as e:

    site_title = None
    itunes_episode = None
    itunes_title = None
    itunes_author = None
    itunes_duration = None
    itunes_explicit = None
    cover_art = None
    media = None
    pub_date = None

##################


# def return_data(results, string_format):
#     # Create our empty list
#     return_list = []

#     return return_list


# for i in range(len(item_results)):
#     print(item_results[i])    
    # [
    #     'site_title',
    #     'itunes_episode',
    #     'itunes_title',
    #     'itunes_author',
    #     'itunes_duration',
    #     'itunes_explicit',
    #     'itunes_summary',
    #     'cover_art',
    #     'media',
    # ]


for i in range(100):
    # print(type(item_results[i]))
    # print(item_results[i]['itunes_title'])
    # print(item_results[i]['itunes_summary'])
    # print(item_results[i]['pub_date'])
    # print(item_results[i]['itunes_author'])
    print(item_results[i]['cover_art'])
