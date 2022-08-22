import re
from typing import Dict


class Article:

    def __init__(self, soup):
        self.soup = soup
        self.meta_container = soup.find(class_='tm-article-snippet__meta')
        self.hubs_container = soup.find(class_='tm-article-snippet__hubs')
        self.counts_container = soup.find(class_='tm-data-icons') 

        self.root_link = 'https://habr.com'

    def __publicatoin_date_info(self) -> None:
        '''
        Extract publication date
        '''
        self.publication_datetime = self.meta_container.find('time')['title'].replace(',', '')


    def __author_info(self) -> None:
        '''
        Extract author information: username and link to account
        '''
        user_info_block = self.meta_container.find('a', class_='tm-user-info__username')

        self.author_name = user_info_block.text.strip()
        self.author_link = self.root_link + user_info_block['href']
        
    def __article_info(self) -> None:
        '''
        Extract article information: article title and link to the article
        '''
        header_container = self.soup.find('a', class_='tm-article-snippet__title-link')

        self.article_link = self.root_link + header_container['href']
        self.article_title = header_container.span.text.strip()

    def __views_info(self) -> None:
        '''
        Extract views of article
        '''
        self.num_views = self.counts_container.find('span', class_='tm-icon-counter__value').text.strip()

    def __voices_info(self) -> None:
        '''
        Extract information about voices on article 
        '''
        voices_container = self.counts_container.find(
            'span',
            class_='tm-votes-meter__value'
        )
        print(self.article_link)
        voices_increase = voices_container.text
        voice_plus, voice_minus, total_voices = (0,) * 3
        if voices_increase != '0' and voices_container['title']:
            total_voices, voice_plus, voice_minus = re.findall('(\d+\.\d+|\d+)', voices_container['title'])

        self.voices = {
            'voices_increase': voices_increase,
            'voice_plus': voice_plus,
            'voice_minus': voice_minus,
            'total_voices': total_voices
        }

    def __bookmarks_info(self) -> None:
        '''
        Extract informatino about number of article bookmarks
        '''
        self.num_bookmarks = self.counts_container.find('span', class_='bookmarks-button__counter').text.strip()

    def __comments_info(self) -> None:
        '''
        Extract informatino about number of comments
        '''
        self.num_comments = self.counts_container.find('span', class_='tm-article-comments-counter-link__value').text.strip()

    def get_info(self) -> Dict[str, str]:
        self.__publicatoin_date_info()
        self.__author_info()
        self.__article_info()
        self.__voices_info()
        self.__bookmarks_info()
        self.__comments_info()

        return {
            'publication_datetime': self.publication_datetime,
            'author_name': self.author_name,
            'author_link': self.author_link,
            'article_title': self.article_title,
            'article_link': self.article_link,
            'voices': self.voices,
            'num_bookmarks': self.num_bookmarks,
            'num_comments': self.num_comments
        }



