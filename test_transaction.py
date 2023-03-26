import os

import pytest
from transaction import Transaction, DB_FILE_PATH

@pytest.fixture
def get_transaction():
    if os.path.exists(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)
    transaction = Transaction()
    return transaction

# feature created by Yingshan Hu
def test_show_categories(get_transaction):
    # Test when there are no categories initially
    assert get_transaction.show_categories() == []

   # Add some categories to the database
    get_transaction.runQuery("INSERT INTO categories(name) VALUES (?)", ('Groceries',))
    get_transaction.runQuery("INSERT INTO categories(name) VALUES (?)", ('Gas',))
    
    # Get the categories
    actual = get_transaction.show_categories()
    
    # Check that the returned categories are correct
    expected = [(1, 'Groceries'), (2, 'Gas')]
    assert expected == actual

# feature created by Yingshan Hu    
def test_add_category(get_transaction):
    # Ensure that an empty category name cannot be added
    get_transaction.add_category("")
    assert get_transaction.show_categories() == []
    
    # Add a category to the database
    get_transaction.add_category("Dining out")
    
    # Get the categories
    actual = get_transaction.runQuery("SELECT * FROM categories", ())
    
    # Check that the category was added correctly
    expected = [(1, 'Dining out')]
    assert expected == actual

# feature created by Yingshan Hu    
def test_modify_category(get_transaction):
    # Add some categories to the database
    get_transaction.add_category("Groceries")
    get_transaction.add_category("Gas")

    # Test modifying an existing category
    get_transaction.modify_category("Groceries", "Food")
    actual = get_transaction.show_categories()
    expected = [(1, "Food"), (2, "Gas")]
    assert expected == actual

    # Test modifying a non-existent category
    get_transaction.modify_category("Utilities", "Bills")
    actual = get_transaction.show_categories()
    expected = [(1, "Food"), (2, "Gas")]
    assert expected == actual

    # Test modifying a category to an empty string
    get_transaction.modify_category("Gas", "")
    actual = get_transaction.show_categories()
    expected = [(1, "Food"), (2, "Gas")]
    assert expected == actual

    # Test modifying an empty string to a non-empty string
    get_transaction.modify_category("", "Transportation")
    actual = get_transaction.show_categories()
    expected = [(1, "Food"), (2, "Gas")]
    assert expected == actual

    # Test modifying an empty string to another empty string
    get_transaction.modify_category("", "")
    actual = get_transaction.show_categories()
    expected = [(1, "Food"), (2, "Gas")]
    assert expected == actual

 # feature created by Bing Han 
def test_show_transactions_empty(get_transaction):
    result = get_transaction.show_transactions()
    assert result == ('No transactions found.', [])
 # feature created by Bing Han 
def test_show_transactions_nonempty(get_transaction):
    get_transaction.add_transaction('2023-03-26', 'Groceries', 100.0, 1)
    get_transaction.add_transaction('2023-03-27', 'Gasoline', 50.0, 2)
    result = get_transaction.show_transactions()
    assert len(result) == 2
    assert result[0][1] == 'Groceries'
    assert result[0][2] == 100.0
    assert result[0][3] == '2023-03-26'
    assert result[0][4] == 1
    assert result[1][1] == 'Gasoline'
    assert result[1][2] == 50.0
    assert result[1][3] == '2023-03-27'
    assert result[1][4] == 2

 # feature created by Bing Han 
def test_add_show_transaction(get_transaction):
    params_lst = [
        ("2022-03-26", "Snack", 5.99, 1),
        ("2022-03-26", "Food", 7.99, 2),
        ("2022-03-26", "Snack", 9.99, 1),
        ("2022-03-26", "Food", 10.99, 2)
    ]
    for params in params_lst:
        get_transaction.add_transaction(*params)
    actual = get_transaction.show_transactions()
    # modify the expected output format
    expected = [
        (1, "Snack", 5.99, "2022-03-26", 1),
        (2, "Food", 7.99, "2022-03-26", 2),
        (3, "Snack", 9.99, "2022-03-26", 1),
        (4, "Food", 10.99, "2022-03-26", 2)
    ]
    assert expected == actual


 # feature created by Bing Han 
def test_add_delete_show_transaction(get_transaction):
 def test_add_delete_show_transaction(get_transaction):
     params_lst = [("2022-03-26", "Snack", 5.99, 1),
                   ("2022-03-26", "Food", 7.99, 2),
                   ("2022-03-26", "Snack", 9.99, 1),
                   ("2022-03-26", "Food", 10.99, 2)]
     for params in params_lst:
         get_transaction.add_transaction(*params)

     get_transaction.delete_transaction(2)
     actual = get_transaction.show_transactions()
     expected = [(params[3],) + params for i, params in enumerate(params_lst) if i != 1]
     assert expected == actual


# feature created by Feifan He
@pytest.fixture
def get_transactions_for_summarize():
    if os.path.exists(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)
    transaction = Transaction()
    params_lst = [("2021-03-26", "Snack", 5.99, 1),
                  ("2021-03-26", "Food", 7.99, 2),
                  ("2022-03-27", "Snack", 9.99, 1),
                  ("2022-03-27", "Food", 10.99, 2),
                  ("2022-04-10", "Food", 7.99, 2),
                  ("2022-04-11", "Snack", 9.99, 1),
                  ("2023-03-01", "Food", 7.99, 2),
                  ("2023-03-02", "Snack", 9.99, 1),
                  ("2023-05-02", "Food", 10.99, 2)]
    for params in params_lst:
        transaction.add_transaction(*params)
    return transaction


# feature created by Feifan He
def test_summarize_transactions_by_date(get_transactions_for_summarize):
    transaction = get_transactions_for_summarize
    expected = [('2021-03-26', 13.98), ('2022-03-27', 20.98), ('2022-04-10', 7.99), ('2022-04-11', 9.99),
                ('2023-03-01', 7.99), ('2023-03-02', 9.99), ('2023-05-02', 10.99)]
    actual = transaction.summarize_transactions_by_date()
    assert expected == actual


# feature created by Feifan He
def test_summarize_transactions_by_month(get_transactions_for_summarize):
    transaction = get_transactions_for_summarize
    expected = [('2021-03', 13.98), ('2022-03', 20.98), ('2022-04', 17.98), ('2023-03', 17.98), ('2023-05', 10.99)]
    actual = transaction.summarize_transactions_by_month()
    assert expected == actual


# feature created by Feifan He
def test_summarize_transactions_by_year(get_transactions_for_summarize):
    transaction = get_transactions_for_summarize
    expected = [('2021', 13.98), ('2022', 38.96), ('2023', 28.97)]
    actual = transaction.summarize_transactions_by_year()
    assert expected == actual

# feature created by Tianling Hou
@pytest.fixture
def transaction_test():
    # Initialize Transaction object
    transaction = Transaction()
    
    # Add a few transactions to the database
    transaction.add_transaction("2023-03-01", "Groceries", 50, 1)
    transaction.add_transaction("2023-03-02", "Gas", 30, 2)
    transaction.add_transaction("2023-03-03", "Coffee", 5, 3)
    
    yield transaction
    
    # Clean up the database
    transaction.runQuery("DELETE FROM transactions", ())
    

def test_summarize_transactions_by_category(transaction_test):
    # Test the summarize_transactions_by_category method
    result = transaction_test.summarize_transactions_by_category()
    
    # Assert that the result is a list of strings
    assert isinstance(result, list)
    for summary in result:
        assert isinstance(summary, str)
        
    # Assert that the summary strings contain the correct information
    expected_summaries = [
        "Category: Groceries\nTotal amount spent: 50\nNumber of transactions: 1\n",
        "Category: Gas\nTotal amount spent: 30\nNumber of transactions: 1\n",
        "Category: Coffee\nTotal amount spent: 5\nNumber of transactions: 1\n"
    ]
    assert result == expected_summaries
