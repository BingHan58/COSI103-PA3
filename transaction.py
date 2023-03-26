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
import re

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
        return rows

    # features created by Yingshan Hu, modified by Tianling
    # def add_category(self, name):
    #    self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
    def add_category(self, name):
        if name == '':
            return "Need to provide category name"
        try:
            self.runQuery("INSERT INTO categories(name) VALUES(?)", (name,))
            return f"{name} category added successfully."
        except sqlite3.IntegrityError:
            return f"{name} category already exists."

    # features created by Yingshan Hu
    def modify_category(self, old_name, new_name):
       self.runQuery("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))

    # features created by Bing Han, modified by Tianling
    # def show_transactions(self):
    #     return self.runQuery("SELECT * FROM transactions", ())
    def show_transactions(self):
        rows = self.runQuery("SELECT * FROM transactions", ())
        if len(rows) == 0:
            return "No transactions found.", []
        else:
            return rows
        
    # features created by Bing Han, modified by Tianling
    def add_transaction(self, date, description, amount, category_id):
        if not re.match(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])", date):
            raise ValueError("Invalid date format. Date should be in the format YYYY-MM-DD.")
        if not isinstance(description, str):
            raise TypeError("Description should be a string.")
        if not isinstance(amount, int):
            raise TypeError("Amount should be an integer.")
        if not isinstance(category_id, int):
            raise TypeError("Category ID should be an integer.")
        return self.runQuery("INSERT INTO transactions (date, description, amount, category_id) VALUES (?, ?, ?, ?)",
                            (date, description, amount, category_id))
        # return self.runQuery("INSERT INTO transactions (date, description, amount, category_id) VALUES (?, ?, ?, ?)",
        #               (date, description, amount, category_id))

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
            total_amount = sum([transaction[2] for transaction in transactions])
            # Add summary string to list
            summary = f"Category: {category_name}\nTotal amount spent: {str(total_amount)}\nNumber of transactions: {len(transactions)}\n"
            summaries.append(summary)
        return summaries

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