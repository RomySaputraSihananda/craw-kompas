from lib import Kompas
from lib.helpers import Site
from json import dumps


kompas: Kompas = Kompas()

with open('data/bola.json', 'w') as file:
    file.write(dumps(kompas.execute(site=Site.Global, page=1, date='2020-10-11')))