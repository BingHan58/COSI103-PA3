'''
transaction.py is an Object-Relational Mapping (ORM) module 
that interacts with the tracker.db database.
The ORM will map SQL rows with the schema
(id, date, description, amount, category_id)
to Python Dictionaries as follows:
{id:1, date:'2022-03-28', description:'Grocery shopping', amount: 100.00, category_id:1}
In place of SQL queries, we will have method calls.
This app will store the data in a SQLite database named tracker.db
The class Transaction provides various methods for accessing 
and manipulating data, including adding and modifying categories, adding and deleting transactions, 
and summarizing transactions by date, month, year, or category.
In addition, the ORM includes a method run_query() that connects to the database, 
executes a query with parameters, fetches the rows, and closes the connection. The method catches 
and ignores any errors that may occur during the database interaction.
'''

import sqlite3
import re

DB_FILE_PATH = 'tracker.db'

# features created by Tianling Hou
def to_dict(self, row):
    '''
    Convert a tuple representing a row in the transactions table to a dictionary.
    '''
    keys = ['id', 'date', 'description', 'amount', 'category_id', 'category_name']
    values = list(row) + [None] * (len(keys) - len(row))
    if values[4] is not None:
        values[5] = self.run_query("SELECT name FROM categories WHERE id = ?", (values[4],))[0][0]
    return dict(zip(keys, values))

class Transaction:
    """
    An ORM module that interacts with the tracker.db database.
    """
    # features created by Tianling Hou
    def __init__(self):
        self.run_query('''CREATE TABLE IF NOT EXISTS categories (
                            id INTEGER PRIMARY KEY,
                            name TEXT UNIQUE NOT NULL)''', ())

        self.run_query('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    description TEXT NOT NULL,
                    amount REAL NOT NULL,
                    date TEXT NOT NULL,
                    category_id INTEGER NOT NULL,
                    FOREIGN KEY (category_id) REFERENCES categories(id))''', ())

        # Initialize categories list
        self.categories = self.run_query("SELECT * FROM categories", ())

    # features created by Yingshan Hu, modified by Tianling
    def show_categories(self):
        """
        Return a list of dictionaries representing all categories in the categories table.
        """
        rows = self.run_query("SELECT id, name FROM categories", ())
        return rows

    # features created by Yingshan Hu, modified by Tianling
    def add_category(self, name):
        """
        Add a new category to the categories table.
        """
        if name == '':
            return "Need to provide category name"
        try:
            self.run_query("INSERT INTO categories(name) VALUES(?)", (name,))
            return f"{name} category added successfully."
        except sqlite3.IntegrityError:
            return f"{name} category already exists."

    # features created by Yingshan Hu
    def modify_category(self, old_name, new_name):
        """
        Modify the name of an existing category in the categories table.
        """
        self.run_query("UPDATE categories SET name = ? WHERE name = ?", (new_name, old_name))

    # features created by Bing Han, modified by Tianling
    def show_transactions(self):
        """
        Return a list of dictionaries representing all transactions in the transactions table.
        """
        rows = self.run_query("SELECT * FROM transactions", ())
        if len(rows) == 0:
            return "No transactions found.", []
        return rows

    # features created by Bing Han, modified by Tianling
    def add_transaction(self, date, description, amount, category_id):
        """
        Add a new transaction to the transactions table.
        """
        if not re.match(r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])", date):
            raise ValueError("Invalid date format. Date should be in the format YYYY-MM-DD.")
        if not isinstance(description, str):
            raise TypeError("Description should be a string.")
        if not isinstance(amount, int) and not isinstance(amount, float):
            raise TypeError("Amount should be a number.")
        if not isinstance(category_id, int):
            raise TypeError("Category ID should be an integer.")
        return self.run_query(
            "INSERT INTO transactions (date, description, amount, category_id) VALUES (?, ?, ?, ?)",
                            (date, description, amount, category_id))

    # features created by Bing Han
    def delete_transaction(self, transaction_id):
        """
        Delete a transaction from the transactions table.
        """
        self.run_query("DELETE FROM transactions WHERE id = ?", (transaction_id,))

    # feature created by Feifan He
    def summarize_transactions_by_date(self):
        """
        Summarize transactions by date.
        """
        return self.run_query("SELECT date, SUM(amount) FROM transactions GROUP BY date", ())

    # feature created by Feifan He
    def summarize_transactions_by_month(self):
        """
        Summarize transactions by month.
        """
        return self.run_query(
            "SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM transactions GROUP BY month",
                             ())

    # feature created by Feifan He
    def summarize_transactions_by_year(self):
        """
        Summarize transactions by year.
        """
        return self.run_query(
            "SELECT strftime('%Y', date) AS year, SUM(amount) FROM transactions GROUP BY year", ())

    # feature created by Tianling Hou
    # def summarize_transactions_by_category(self):
    #     """
    #     Summarize transactions by category.
    #     """
    #     # Get all categories from the database
    #     categories = self.run_query("SELECT * FROM categories", ())
    #     # Initialize list of summary strings
    #     summaries = []
    #     # Iterate through each category and retrieve its transactions
    #     for category in categories:
    #         category_id = category[0]
    #         category_name = category[1]
    #         transactions = self.run_query(
    #             "SELECT * FROM transactions WHERE category_id = ?", (category_id,))
    #         total_amount = sum([transaction[2] for transaction in transactions])
    #         # Add summary string to list
    #         summary = (f"Category: {category_name}\n"
    #                    f"Total amount spent: {total_amount}\n"
    #                    f"Number of transactions: {len(transactions)}\n")
    #         summaries.append(summary)
    #     return summaries
    def summarize_transactions_by_category(self):
        """
        Summarize transactions by category.
        """
        # Get the summary of transactions by category from the database
        result = self.run_query("""
            select categories.name category_name, sum(amount) total
            from categories, transactions
            where categories.id = transactions.category_id
            group by categories.id
        """, ())
        return result

    # feature modified by Tianling Hou
    def run_query(self, query, params, fetch_names=False):
        '''This method executes a SQL query with parameters on the tracker.db database, 
        fetches the resulting rows, and returns them. It also allows for the option to 
        fetch the column names instead of the rows by setting the fetch_names parameter to True.
        '''
        con = sqlite3.connect(DB_FILE_PATH)
        cur = con.cursor()
        cur.execute(query, params)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        if fetch_names:
            return [to_dict(t, self.run_query) for t in tuples]
        return tuples
