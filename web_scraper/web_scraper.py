from cgitb import text
import requests
from bs4 import BeautifulSoup

# Declaring and pulling url content in raw
url = 'https://en.wikipedia.org/wiki/Money'
page = requests.get(url)


# Parsing with beautiful soup
soup = BeautifulSoup(page.content, 'html.parser')

# finds all the paragraphs in article
body_div = soup.find_all('p')


# empty list to populate with citation needed paragraphs
para_list = []

# filters out non citation needed paragraphs
for paragraph in body_div:
  if 'citation needed' in paragraph.text:
    para_list.append(paragraph.text)


def get_citations_needed_count():
  return print(len(para_list))

def get_citation_needed_report():
  for i in para_list:
    print(i)
