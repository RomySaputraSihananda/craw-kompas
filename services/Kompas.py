from requests import Session;

class Kompas: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__request.headers.update({
            'accept : testooo'
        });

    def execute(self, url) -> str:
        self.__request.get(url);


if(__name__ == '__main__'):
    kompas: Kompas = Kompas();
    print(kompas.execute('https://httpbin.org/headers'));