import requests
from bs4 import BeautifulSoup

wiki = input('Input wikipedia target (ex. Dog) Put \'_\' between spaces: ')
r = requests.get('https://en.wikipedia.org/wiki/' + wiki)
soup = BeautifulSoup(r.text, 'html.parser')
try:
    title = soup.find('title')
    lastDate = soup.find("li", {"id": "footer-info-lastmod"})
    counter = 0
    print("\n", title.text)
    references = soup.find(
        "ol", {"class": "references"})
    for i in references.find_all('li'):
        counter += 1
    print("Total of ", counter, " references used")
    print(lastDate.text, "\n")
except:
    print('Wiki for ', wiki, ' not found...')
