import pytest
from transaction import Transaction

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

