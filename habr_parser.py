import sys
import time
import json

import requests
from bs4 import BeautifulSoup

from rich.prompt import Prompt
from rich.console import Console

from models import Article

def main():
    console = Console()

    # query = Prompt.ask('Enter query: ')
    # pages = int(Prompt.ask('Pages: ', default='10'))
    query = 'postgresql'
    pages = 1
    saving_file = f'{query}.json'
    articles = []

    for page in range(1, pages+1):
        response = requests.get(f'https://habr.com/ru/search/page{page}/?q={query}&target_type=posts&order=relevance')
        if response.status_code != 200:
            break

        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        for article in soup.find_all('article'):
            art_info = Article(article).get_info()
            articles.append(art_info)
        
        time.sleep(.1)

    if not articles:
        print('Something go wrong')
        sys.exit(1)

    with open(saving_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(articles, jsonfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
