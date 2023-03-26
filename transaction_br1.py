import sqlite3
import os

def toDict(t):
    ''' t is a tuple (id, date, description, amount, category_id)'''
    print('t =', t)
    transaction = {'id': t[0], 'date': t[1], 'description': t[2], 'amount': t[3], 'category_id': t[4]}
    return transaction

class Transaction:
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            description TEXT NOT NULL,
                            amount REAL NOT NULL,
                            category_id INTEGER,
                            FOREIGN KEY (category_id) REFERENCES categories (id))''', ())
        
     # features created by Yingshan Hu
    def show_categories(self):
        return self.runQuery("SELECT * FROM categories", ())

    # features created by Yingshan Hu
    def add_category(self, name):
        self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
    
    # features created by Yingshan Hu
    def modify_category(self, old_name, new_name):
        self.runQuery("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))  
        
    # features created by Bing Han
    def show_transactions(self):
        return self.runQuery("SELECT * FROM transactions", ())

    # features created by Bing Han
    def add_transaction(self, amount, category_id, date, description):
        self.runQuery("INSERT INTO transactions (amount, category_id, date, description) VALUES (?, ?, ?, ?)",
            (amount, category_id, date, description))

    # features created by Bing Han
    def delete_transaction(self, transaction_id):
        self.runQuery("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    
    # features created by Tianling Hou
    '''Don't forget to add other features from 4-10'''
    def summarize_transactions_by_category(self):
        """Summarize transactions by category"""
        summary_query = """
            SELECT category_id, SUM(amount)
            FROM transactions
            GROUP BY category_id
        """
        return self.runQuery(summary_query, ())
     
    def runQuery(self, query, tuple):
        con = sqlite3.connect(os.path.join(os.getenv('HOME'), 'tracker.db'))
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
