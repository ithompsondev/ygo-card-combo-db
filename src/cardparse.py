import re

# Delimiter-directed translation for external card processing DSL

class CardParse:

    TYPE_MATCH = 1
    NAME_MATCH = 2
    COST_MATCH = 3
    EFFECT_MATCH = 4
    STARTER_MATCH = NAME_MATCH
    ENDER_MATCH = 5

    def __init__(self,file_name):
        self.file_name = file_name
        self.cards = []
        self.combos = []
        self.regex = r"(\w+[\w+\s]+)\s\[(\w+[\w+\s]*)\]\s>>\s(\w+[\w+\s]*)\s>>\s(\w+[\w+\s]*)\s\[(\w+[\w+\s]*)\]"
        
        
    def parse(self):
        file = self.open_file()
        for line in file:
            match = re.search(self.regex,line)
            self.process_new_card_matches(match)
            self.process_new_combo_matches(match)
        self.close_file(file)
        
    
    def process_new_card_matches(self,match):
        new_card = {
            "name": match.group(self.NAME_MATCH).lower(),
            "type": match.group(self.TYPE_MATCH).lower()
        }
        
        self.cards.append(new_card)
    
    
    def process_new_combo_matches(self,match):
        new_combo = {
            "starter": match.group(self.STARTER_MATCH).lower(),
            "cost": match.group(self.COST_MATCH).lower(),
            "effect": match.group(self.EFFECT_MATCH).lower(),
            "ender": match.group(self.ENDER_MATCH).lower()
        }

        self.combos.append(new_combo)

    
    def open_file(self):
        return open(self.file_name,'r')
        
    
    def close_file(self,file):
        file.close()

def main():
    parser = CardParse('test.txt')
    parser.parse()
    print(parser.cards)
    print(parser.combos)

if __name__ == '__main__':
    main()

        
    
