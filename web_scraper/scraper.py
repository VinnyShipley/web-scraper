from cgitb import text
import requests
from bs4 import BeautifulSoup

# Gives the readout of all the paragraphs
def get_citations_needed_report(url):
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
  for i in para_list:
    print(i)







# Gives the count of the citation needed 
def get_citation_needed_count(url):
  page = requests.get(str(url))


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
  return print(len(para_list))
