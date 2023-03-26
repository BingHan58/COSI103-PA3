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
    get_transaction.runQuery("INSERT INTO categories(name) VALUES ('Groceries')")
    get_transaction.runQuery("INSERT INTO categories(name) VALUES ('Gas')")
    
    # Get the categories
    categories = get_transaction.show_categories()
    
    # Check that the returned categories are correct
    expected = [(1, 'Groceries'), (2, 'Gas')]
    assert categories == expected

# feature created by Yingshan Hu    
def test_add_category(get_transaction):
    # Ensure that an empty category name cannot be added
    get_transaction.add_category("")
    assert get_transaction.show_categories() == []
    
    # Add a category to the database
    get_transaction.add_category("Dining out")
    
    # Get the categories
    categories = get_transaction.runQuery("SELECT * FROM categories", ())
    
    # Check that the category was added correctly
    expected = [(1, 'Dining out')]
    assert categories == expected

# feature created by Yingshan Hu    
def test_modify_category(get_transaction):
    # Ensure that modifying a non-existent category does not result in an error
    get_transaction.modify_category("Non-existent Category", "New Category")
    assert get_transaction.show_categories() == []
    
    # Add a category to the database
    get_transaction.runQuery("INSERT INTO categories(name) VALUES ('Entertainment')")
    
    # Modify the category
    get_transaction.modify_category("Entertainment", "Movies")
    
    # Get the categories
    categories = get_transaction.runQuery("SELECT * FROM categories", ())
    
    # Check that the category was modified correctly
    expected = [(1, 'Movies')]
    assert categories == expected
    
def test_add_show_transaction(get_transaction):
    params_lst = [("2022-03-26", "Snack", 5.99),
                  ("2022-03-26", "Food", 7.99),
                  ("2022-03-26", "Snack", 9.99),
                  ("2022-03-26", "Food", 10.99)]
    for params in params_lst:
        get_transaction.add_transaction(*params)
    actual = get_transaction.show_transactions()
    # add id to params
    expected = [(i + 1,) + row for i, row in enumerate(params_lst)]
    assert expected == actual


def test_add_delete_show_transaction(get_transaction):
    params_lst = [("2022-03-26", "Snack", 5.99),
                  ("2022-03-26", "Food", 7.99),
                  ("2022-03-26", "Snack", 9.99),
                  ("2022-03-26", "Food", 10.99)]
    for params in params_lst:
        get_transaction.add_transaction(*params)

    get_transaction.delete_transaction(2)
    actual = get_transaction.show_transactions()
    # add id to params
    expected = [(i + 1,) + row for i, row in enumerate(params_lst) if i != 1]
    assert expected == actual


# feature created by Feifan He
@pytest.fixture
def get_transactions_for_summarize():
    if os.path.exists(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)
    transaction = Transaction()
    params_lst = [("2021-03-26", "Snack", 5.99),
                  ("2021-03-26", "Food", 7.99),
                  ("2022-03-27", "Snack", 9.99),
                  ("2022-03-27", "Food", 10.99),
                  ("2022-04-10", "Food", 7.99),
                  ("2022-04-11", "Snack", 9.99),
                  ("2023-03-01", "Food", 7.99),
                  ("2023-03-02", "Snack", 9.99),
                  ("2023-05-02", "Food", 10.99)]
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
def test_summarize_transactions_by_category(transaction):
    summary = transaction.summarize_transactions_by_category()
    assert len(summary) == 2
    assert summary[0]["category"] == "Food"
    assert summary[0]["SUM(amount)"] == pytest.approx(16.98, rel=1e-2)
    assert summary[1]["category"] == "Leisure"
    assert summary[1]["SUM(amount)"] == pytest.approx(25.00, rel=1e-2)
