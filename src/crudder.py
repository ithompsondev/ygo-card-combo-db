import mysql.connector

class Crudder:

    # TODO: Change schema to represent different decks for each table
    def __init__(self,hostname,username,password,database):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.database = database
        self.db = None
        self.cursor = None
        
        
    def connect(self):
        self.db = mysql.connector.connect(
            host=self.hostname,
            user=self.username,
            password=self.password,
            database=self.database
        )

        self.cursor = self.db.cursor(buffered=True)


    def insert_cards(self,cards):
        sql = 'insert into card (name,type) values (%s,%s)'
        for card in cards:
            vals = (card['name'],card['type'])
            if not self.card_exists(card['name']):
                self.cursor.execute(sql,vals)
        self.db.commit()


    # if an ender card is not already contained in the card table
    # will throw foreign key constraint error otherwise
    def insert_card(self,card):
        sql = 'insert into card (name,type) values (%s,%s)'
        val = (card['name'],card['type'])
        if not self.card_exists(card['name']):
            self.cursor.execute(sql,val)
        self.db.commit()
        

    def insert_combos(self,combos):
        sql = 'insert into combo (starter,cost,effect,ender) values (%s,%s,%s,%s)'
        for combo in combos:
            vals = (combo['starter'],combo['cost'],combo['effect'],combo['ender'])
            # avoid foreign key constraint
            if not self.card_exists(combo['ender']):
                print('ender: ' + combo['ender'])
                print('type: ' + combo['ender_type'])
                self.insert_card({'name': combo['ender'], 'type': combo['ender_type']})
            if not self.combo_exists(combo):
                self.cursor.execute(sql,vals)
        self.db.commit()


    def card_exists(self,card_name):
        sql = 'select name from card where name=%s'
        val = (card_name,)
        self.cursor.execute(sql,val)
        result = self.cursor.fetchall()
        if len(result) == 0: return False
        else: return True


    def combo_exists(self,combo):
        sql = 'select starter,cost,effect,ender from combo where starter = %s and cost = %s and effect = %s and ender = %s'
        vals = (combo['starter'],combo['cost'],combo['effect'],combo['ender'])
        self.cursor.execute(sql,vals)
        result = self.cursor.fetchall()
        if len(result) == 0: return False
        else: return True


    def get_starter_frequency(self):
        sql = 'select starter,count(starter) as freq from combo group by starter order by freq desc'
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


    def get_combos(self,name):
        sql = 'select starter,cost,effect,ender from combo where starter=%s'
        val = (name,)
        self.cursor.execute(sql,val)
        result = self.cursor.fetchall()
        return result
