import requests


url = 'https://en.wikipedia.org/wiki/Money'
page = requests.get(url)
print(page)