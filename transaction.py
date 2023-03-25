import sqlite3
import os

class Transaction:
    def __init__(self):
        self.db_file = os.path.join(os.getenv('HOME'), 'tracker.db')
        self.create_tables()

    def create_tables(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE NOT NULL)''', ())

        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions (
                            id INTEGER PRIMARY KEY,
                            date TEXT NOT NULL,
                            description TEXT NOT NULL,
                            amount REAL NOT NULL,
                            category_id INTEGER,
                            FOREIGN KEY (category_id) REFERENCES categories (id))''', ())
        
        
     def runQuery(self, query, params):
        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
            rows = cur.fetchall()
            conn.close()
            return rows
        except sqlite3.Error as e:
            pass
