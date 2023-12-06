from requests import Session, Response;
from pyquery import PyQuery;
from ..helpers import Parser, Datetime, Hasher;

from json import dumps;
import re;

class Kompas: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();
        self.__datetime: Datetime = Datetime();
        self.__hasher: Hasher = Hasher();
    
        self.__result: dict = {}
        self.__result['title']: str = None;
        self.__result['url']: str = None;
        self.__result['date_now']: str = None;
        self.__result['prev_page']: str = None;
        self.__result['next_page']: str = None;
        self.__result['data']: list[dict] = [];
    
    def __get_urls(self, container: PyQuery) -> list[str]:
        urls = [];

        for div in container('.article__list.clearfix'):
            urls.append(self.__parser.execute(div, '.article__list__title h3 a').attr('href'));

        return urls;

    def __get_data_page(self, url: str):
        res: Response = self.__request.get(url);

        parser: PyQuery = self.__parser.execute(res.text, 'body');
        title = parser('.read__title').text();

        article = parser('div[class="col-bs9-7"] div[class="clearfix"]').remove('strong').remove('i').remove('iframe').text().lstrip('- ').replace('\u201c', '').replace('\u201d', '').replace('\n', '');

        return { 
            'id': self.__hasher.execute(title),
            'title':  title,
            'url': url,
            'url_thumbnail': parser('.photo__wrap img').attr('src'),
            'create_at': self.__datetime.execute(re.search(r'/(\d{4}/\d{2}/\d{2}/\d+)/', url).group(1).replace("/", "")),
            'autor': parser('.credit-title-name h6:first-child').text().rstrip(","),
            'editor': parser('.credit-title-name h6:last-child').text(),
            'desc': article[:100] + '....',
            'article': article,
            'tags': [self.__parser.execute(li, 'a').text() for li in parser('.tag__article__item .tag__article__link')]
            };

    def execute(self, site: str, page: int, date: str = None) -> str:
        url: str = f'https://indeks.kompas.com/?site={site}&date={date if date else self.__datetime.now().split("T")[0]}&page={page}';
        res: Response = self.__request.get(url);

        parser: PyQuery = self.__parser.execute(res.text, 'html');

        if(res.status_code != 200): raise TypeError(f"Error! status code {res.status_code} : {res.reason}");

        self.__result['title']: str = parser('title').text();
        self.__result['url']: str = url;
        self.__result['date_now']: str = self.__datetime.now();

        urls: list[str] = self.__get_urls(parser('.latest--indeks.mt2.clearfix'));

        for url in urls:
            data: dict = self.__get_data_page(url);

            self.__result['data'].append(data);

            # break;

        return self.__result;


if(__name__ == '__main__'):
    kompas: Kompas = Kompas();
    with open('data/data_test.json', 'w') as file:
        file.write(dumps(kompas.execute('news', 1)))
    # print(dumps(kompas.execute('news', 1)));