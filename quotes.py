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
except:
    print('Wiki for not found...')
