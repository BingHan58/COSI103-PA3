import os

import pytest
from transaction import Transaction, DB_FILE_PATH


@pytest.fixture
def get_transaction():
    if os.path.exists(DB_FILE_PATH):
        os.remove(DB_FILE_PATH)
    transaction = Transaction()
    return transaction


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
