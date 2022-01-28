from bs4 import BeautifulSoup
import requests

with open('deleteme.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

match = soup.find('div', class_='footer')
print(match)