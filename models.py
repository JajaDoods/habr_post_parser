from typing import Dict


class Article:

    def __init__(self, soup):
        self.soup = soup
        self.meta_container = soup.find(class_='tm-article-snippet__meta')
        self.hubs_container = soup.find(class_='tm-article-snippet__hubs')
        self.counts_container = soup.find(class_='tm-data-icons') 

        self.root_link = 'https://habr.com'

    def __author_info(self) -> None:
        '''
        Extract author information: username and link to account
        '''
        user_info_block = self.meta_container.find('a', class_='tm-user-info__username')

        self.author_name = user_info_block.text.strip()
        self.author_link = self.root_link + user_info_block['href']
        
    def __article_info(self) -> None:
       header_container = self.soup.find('a', class_='tm-article-snippet__title-link')

       self.article_link = self.root_link + header_container['href']
       self.article_title = header_container.span.text.strip()

    def extract_info(self) -> Dict[str, str]:
        self.__author_info()
        self.__article_info()

        return {
            'author_name': self.author_name,
            'author_link': self.author_link,
            'article_title': self.article_title,
            'article_link': self.article_link
        }
