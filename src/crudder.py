import mysql.connector

class Crudder:
    
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
            if not self.card_exists(card):
                self.cursor.execute(sql,vals)
        self.db.commit()


    def insert_combos(self,combos):
        sql = 'insert into combo (starter,cost,effect,ender) values (%s,%s,%s,%s)'
        for combo in combos:
            vals = (combo['starter'],combo['cost'],combo['effect'],combo['ender'])
            if not self.combo_exists(combo):
                self.cursor.execute(sql,vals)
        self.db.commit()


    def card_exists(self,card):
        sql = 'select name from card where name=%s'
        val = (card['name'],)
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
