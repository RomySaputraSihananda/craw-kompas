from argparse import ArgumentParser;

from lib import Kompas
from lib.helpers import Site
from json import dumps
import os 


if(__name__ == '__main__'):
    argp: ArgumentParser = ArgumentParser()
    argp.add_argument("--site", '-s', type=str, default='News')
    argp.add_argument("--date", '-d', type=str, default=None)
    argp.add_argument("--page", '-p', type=int, default=1)
    argp.add_argument("--output", '-o', type=str)
    args = argp.parse_args()

    kompas: Kompas = Kompas()

    output = f'data' if not args.output else args.output

    if(not os.path.exists(output)):
            os.makedirs(output)

    with open(f'{output}/{Site[args.site].name}.json', 'w') as file:
        file.write(dumps(kompas.execute(site=Site[args.site], page=args.page, date=args.date)))