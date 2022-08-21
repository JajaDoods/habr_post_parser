

class Article:

    def __init__(self, soup):
        self.meta_container = soup.find(class_='tm-article-snippet__meta')
        self.hubs_container = soup.find(class_='tm-article-snippet__hubs')
        self.counts_container = soup.find(class_='tm-data-icons') 

    def author_info(self) -> None:
        '''
        Extract author information: username and link to account
        '''
        user_info_block = self.meta_container.find('a', class_='tm-user-info__username')

        self.username = user_info_block.text.strip()
        self.user_link = 'https://habr.com' + user_info_block['href']
        
