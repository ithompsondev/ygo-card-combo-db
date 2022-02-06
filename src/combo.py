from crudder import Crudder as crud

class Combo:

    def __init__(self,db):
        self.db = db


    def frequent(self):
        results = db.get_starter_frequency()
        for result in results:
            starter = result[0]
            frequency = result[1]
            print(f'{starter} appears as a combo starter in {frequency} combo(s)')


    def build_chain(self,name):
        # Figure out how to build a tree of combos
        pass
                
