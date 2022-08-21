import time

import requests
from bs4 import BeautifulSoup

from rich.prompt import Prompt
from rich.console import Console

from models import Article

def main():
    console = Console()

    # query = Prompt.ask('Enter query: ')
    # pages = int(Prompt.ask('Pages: ', default='10'))
    query = 'python'
    pages = 1
    aritcles = []

    for page in range(1, pages+1):
        response = requests.get(f'https://habr.com/ru/search/page{page}/?q={query}&target_type=posts&order=relevance')
        if response.status_code != 200:
            print('Something go wrong.')
            break

        html = response.text
        soup = BeautifulSoup(html, 'lxml')

        articles_soup = soup.find_all('article')
        for article in articles_soup:
            art_info = Article(article).extract_info()
            articles.append(art_info)

        
        time.sleep(.1)

if __name__ == '__main__':
    main()
