'''
transaction.py is an Object-Relational Mapping (ORM) module that interacts with the tracker.db database.

The ORM will map SQL rows with the schema
(id, date, description, amount, category_id)
to Python Dictionaries as follows:
{id:1, date:'2022-03-28', description:'Grocery shopping', amount: 100.00, category_id:1}


In place of SQL queries, we will have method calls.

This app will store the data in a SQLite database named tracker.db

The class Transaction provides various methods for accessing and manipulating data, including adding and modifying categories, adding and deleting transactions, and summarizing transactions by date, month, year, or category.

In addition, the ORM includes a method runQuery() that connects to the database, executes a query with parameters, fetches the rows, and closes the connection. The method catches and ignores any errors that may occur during the database interaction.
'''

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

        
     # features created by Yingshan Hu
     def show_categories(self):
        return self.runQuery("SELECT * FROM categories", ())
    
     def add_category(self, name):
        self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
        
     def modify_category(self, old_name, new_name):
        self.runQuery("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))  
        
      
    
    
    
    
    
    
    
        
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
