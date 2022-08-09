from cgitb import text
import requests
from bs4 import BeautifulSoup

# Declaring and pulling url content in raw
url = 'https://en.wikipedia.org/wiki/Money'
page = requests.get(url)


# Parsing with beautiful soup
soup = BeautifulSoup(page.content, 'html.parser')


body_div = soup.find_all('p')

para_list = []

for paragraph in body_div:
  if 'citation needed' in paragraph.text:
    para_list.append(paragraph.text)

for i in para_list:
  print(i)


