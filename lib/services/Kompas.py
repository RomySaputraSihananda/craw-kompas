from requests import Session;
from ..helpers import Parser;

class Kompas: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();

    def __get_source_page(self, url: str) -> str:
        return self.__request.get(url).text;

    def execute(self, url: str) -> str:
        html = self.__get_source_page(url);
        return self.__parser.execute(html, 'title');




if(__name__ == '__main__'):
    kompas: Kompas = Kompas();
    print(kompas.execute('https://indeks.kompas.com/?site=news&date=2023-11-30&page=1'));