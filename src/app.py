from crudder import Crudder
from cardparse import CardParse
import config as cfg

def main():
    file = input("combo list file name: ")
    parser = CardParse(file)
    parser.parse()

    crud = Crudder(
        hostname=cfg.hostname,
        username=cfg.username,
        password=cfg.password,
        database=cfg.database
    )
    crud.connect()
    crud.insert_cards(parser.cards)
    crud.insert_combos(parser.combos)


if __name__ == '__main__':
    main()
