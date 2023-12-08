from lib import Kompas
from lib.helpers import Site
from json import dumps

if(__name__ == '__main__'):
    kompas: Kompas = Kompas()

    with open(f'data/{Site.Global.name}.json', 'w') as file:
        file.write(dumps(kompas.execute(site=Site.Global, page=1, date='2020-10-11')))