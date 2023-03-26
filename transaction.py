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

DB_FILE_PATH = 'tracker.db'

# features created by Tianling Hou
def toDict(t):
    keys = ['id', 'date', 'description', 'amount', 'category_id', 'category_name']
    values = list(t) + [None] * (len(keys) - len(t))
    if values[4] is not None:
        values[5] = self.runQuery("SELECT name FROM categories WHERE id = ?", (values[4],))[0][0]
    return {k: v for k, v in zip(keys, values)}

class Transaction:
    # features created by Tianling Hou
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE NOT NULL)''', ())

        self.runQuery('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories(id))''', ())
        
        # Initialize categories list
        self.categories = self.runQuery("SELECT * FROM categories", ())

    # features created by Yingshan Hu, modified by Tianling
    # def show_categories(self):
    #   return self.runQuery("SELECT * FROM categories", ())
    def show_categories(self):
        rows = self.runQuery("SELECT id, name FROM categories", ())
        if len(rows) == 0:
            return []
        else:
            return rows

    # features created by Yingshan Hu, modified by Tianling
    # def add_category(self, name):
    #    self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
    def add_category(self, name):
        if name == '':
            return False
        try:
            self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
            return True
        except sqlite3.IntegrityError:
            return False

    # features created by Yingshan Hu
    #def modify_category(self, old_name, new_name):
       #self.runQuery("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))
    def modify_category(self, old_name, new_name):
        if old_name == '' or new_name == '':
            return
        category_id = self.runQuery("SELECT id FROM categories WHERE name = ?", (old_name,))
        if not category_id:
            return
        self.runQuery("UPDATE categories SET name = ? WHERE id = ?", (new_name, category_id[0][0]))

    # features created by Bing Han, modified by Tianling
    # def show_transactions(self):
    #     return self.runQuery("SELECT * FROM transactions", ())
    def show_transactions(self):
        rows = self.runQuery("SELECT * FROM transactions", ())
        if len(rows) == 0:
            print("No transactions found.")
            return []
        else:
            return rows
        
    # features created by Bing Han, modified by Tianling
    def add_transaction(self, date, description, amount, category_id):
        self.runQuery("INSERT INTO transactions (date, description, amount, category_id) VALUES (?, ?, ?, ?)",
                      (date, description, amount, category_id))

    # features created by Bing Han
    def delete_transaction(self, transaction_id):
        self.runQuery("DELETE FROM transactions WHERE id = ?", (transaction_id,))

    # feature created by Feifan He
    def summarize_transactions_by_date(self):
        return self.runQuery("SELECT date, SUM(amount) FROM transactions GROUP BY date", ())

    # feature created by Feifan He
    def summarize_transactions_by_month(self):
        return self.runQuery("SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM transactions GROUP BY month",
                             ())

    # feature created by Feifan He
    def summarize_transactions_by_year(self):
        return self.runQuery("SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year", ())

    # feature created by Tianling Hou
    def summarize_transactions_by_category(self):
        # Get all categories from the database
        categories = self.runQuery("SELECT * FROM categories", ())

        # Initialize list of summary strings
        summaries = []

        # Iterate through each category and retrieve its transactions
        for category in categories:
            category_id = category[0]
            category_name = category[1]
            transactions = self.runQuery("SELECT * FROM transactions WHERE category_id = ?", (category_id,))

            # Calculate total amount spent for this category
            total_amount = sum([transaction['amount'] for transaction in transactions])

            # Add summary string to list
            summary = f"Category: {category_name}\nTotal amount spent: {total_amount}\nNumber of transactions: {len(transactions)}\n"
            summaries.append(summary)
            return summaries


    # features created by Yingshan Hu
    # def runQuery(self, query, params):
    #     try:
    #         conn = sqlite3.connect(DB_FILE_PATH)
    #         cur = conn.cursor()
    #         cur.execute(query, params)
    #         conn.commit()
    #         rows = cur.fetchall()
    #         conn.close()
    #         return rows
    #     except sqlite3.Error as e:
    #         pass

    # feature modified by Tianling Hou
    def runQuery(self, query, tuple, fetch_names=False):
        con = sqlite3.connect(DB_FILE_PATH)
        cur = con.cursor() 
        cur.execute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        if fetch_names:
            return [toDict(t, self.runQuery) for t in tuples]
        else:
            return tuples
