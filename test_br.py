import pytest
from transaction_br1 import Transaction

@pytest.fixture
def transaction():
    return Transaction()

def test_show_transactions(self):
        transactions = self.transaction.show_transactions()
        assert len(transactions) == 2
        assert (1, 10.99, "Food", "2022-03-24", "Lunch") in transactions
        assert (2, 25.00, "Entertainment", "2022-03-25", "Movie") in transactions

def test_add_transaction(self):
        self.transaction.add_transaction(5.99, "Food", "2022-03-26", "Snack")
        transactions = self.transaction.show_transactions()
        assert len(transactions) == 3
        assert (3, 5.99, "Food", "2022-03-26", "Snack") in transactions

def test_delete_transaction(self):
        transactions = self.transaction.show_transactions()
        self.transaction.delete_transaction(transactions[0][0])
        transactions = self.transaction.show_transactions()
        assert len(transactions) == 1
        assert (2, 25.00, "Entertainment", "2022-03-25", "Movie") in transactions
        
def test_show_categories(transaction):
    categories = transaction.show_categories()
    assert len(categories) == 2
    assert ("Food",) in categories
    assert ("Entertainment",) in categories

def test_add_category(transaction):
    transaction.add_category("Transportation")
    categories = transaction.show_categories()
    assert len(categories) == 3
    assert ("Transportation",) in categories

def test_modify_category(transaction):
    transaction.modify_category("Entertainment", "Leisure")
    categories = transaction.show_categories()
    assert len(categories) == 2
    assert ("Leisure",) in categories

def test_summarize_transactions_by_category(transaction):
    summary = transaction.summarize_transactions_by_category()
    assert len(summary) == 2
    assert summary[0]["category"] == "Food"
    assert summary[0]["SUM(amount)"] == pytest.approx(16.98, rel=1e-2)
    assert summary[1]["category"] == "Leisure"
    assert summary[1]["SUM(amount)"] == pytest.approx(25.00, rel=1e-2)
