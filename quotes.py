import requests
from bs4 import BeautifulSoup
import json

author = input(
    'Input famous person for their quote(s)! (ex. Albert Einstein): ')
r = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(r.text, 'html.parser')
try:
    results = soup.find_all(
        "small", text=author)
    if not results:
        print("\n", "Wasn't able to find quotes for ",
              author, " in my database! :( ")
    else:
        print("\n")
        for r in results:
            parent = r.find_parent('span')
            quote = parent.find_previous_sibling('span').text
            print(quote)
        print("\n")
    # print(subscribers)
    # parent = results.find_parent('span')
    # print(parent.find_previous_sibling('span').text)
    # counter = 0
    # print(title.text)
    # references = soup.find(
    #     "ol", {"class": "references"})
    # for i in references.find_all('li'):
    #     counter += 1
    # print("Total of ", counter, " references used")
except:
    print('Wiki for not found...')
