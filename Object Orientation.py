import unittest
import io
import sys

class UserAccount:
    def __init__(self, account_owner, account_num):
        self.account_owner = account_owner
        self.account_num = account_num
        self.account_balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
            else:
                print("Transaction cannot be completed. Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display(self):
        return (f"Account Owner: {self.account_owner}\n"
                f"Account Number: {self.account_num}\n"
                f"Account Balance: ${self.account_balance:.2f}\n")

class TestUserAccount(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.account1 = UserAccount("John Doe", "CHK123")
        self.account2 = UserAccount("Jane Smith", "SAV456")

    def tearDown(self):
        """Clean up after tests."""
        del self.account1
        del self.account2

    def test_deposit(self):
        self.account1.deposit(100)
        self.assertEqual(self.account1.account_balance, 100)

    def test_withdrawal_success(self):
        self.account1.deposit(500)
        self.account1.withdrawal(200)
        self.assertEqual(self.account1.account_balance, 300)

    def test_withdrawal_insufficient_funds(self):
        self.account2.deposit(50)
        self.account2.withdrawal(100)
        self.assertEqual(self.account2.account_balance, 50)  # Balance should remain 50

    def test_negative_deposit(self):
        self.account1.deposit(-50)
        self.assertEqual(self.account1.account_balance, 0)  # Balance should remain 0

    def test_negative_withdrawal(self):
        self.account1.withdrawal(-50)
        self.assertEqual(self.account1.account_balance, 0)  # Balance should remain 0

    def test_display(self):
        expected_output = (f"Account Owner: John Doe\n"
                           f"Account Number: CHK123\n"
                           f"Account Balance: $500.00\n")
        self.account1.deposit(500)
        self.assertEqual(self.account1.display(), expected_output)

def main():
    # Run the tests
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    # Print account information
    print("\nAccount Information:\n")
    account1 = UserAccount("John Doe", "CHK123")
    account2 = UserAccount("Jane Smith", "SAV456")
    
    account1.deposit(400)
    account1.withdrawal(250)
    print("Checking Account:")
    print(account1.display())
    
    account2.deposit(50)
    account2.withdrawal(100)
    print("Savings Account:")
    print(account2.display())

if __name__ == '__main__':
    main()
