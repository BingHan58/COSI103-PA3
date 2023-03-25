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
        
      
    
    
    '''Don't forget to add other features from 4-10'''
     
    def runQuery(self, query, tuple):
        con = sqlite3.connect(os.getenv('HOME'), 'tracker.db')
        cur = con.cursor() 
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
        