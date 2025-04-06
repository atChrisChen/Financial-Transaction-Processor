# To run test do the following in the terminal in the root directory:
# python3 -m starter_code.Phase5_Testing.test_apply_transaction

import unittest
from starter_code.bank_account import BankAccount

class TestBankAccountTransactions(unittest.TestCase):

    def test_apply_transaction_positive_amount(self):
        account = BankAccount("12345", "Test User", "A", 100.0, 0, "SP")
        account.apply_transaction(50.0)
        self.assertEqual(account.balance, 149.95)
        self.assertEqual(account.transaction_count, 1)
        print("test_apply_transaction_positive_amount passed")

    def test_apply_transaction_negative_amount(self):
        account = BankAccount("12345", "Test User", "A", 100.0, 0, "SP")
        account.apply_transaction(-30.0)
        self.assertEqual(account.balance, 69.95)
        self.assertEqual(account.transaction_count, 1)
        print("test_apply_transaction_negative_amount passed")

    def test_apply_transaction_zero_amount(self):
        account = BankAccount("12345", "Test User", "A", 0.0, 0, "SP")
        account.apply_transaction(0.0)
        self.assertEqual(account.balance, -0.05)
        self.assertEqual(account.transaction_count, 1)
        print("test_apply_transaction_zero_amount passed")

    def test_apply_transaction_disabled_account(self):
        account = BankAccount("12345", "Test User", "D", 100.0, 0, "SP")
        with self.assertRaises(ValueError):
            account.apply_transaction(50.0)
        print("test_apply_transaction_disabled_account passed")

    def test_apply_transaction_student_fee(self):
        account = BankAccount("12345", "Student User", "A", 100.0, 0, "SP")
        account.apply_transaction(100.0)
        self.assertAlmostEqual(account.balance, 199.95)
        self.assertEqual(account.transaction_count, 1)
        print("test_apply_transaction_student_fee passed")

    def test_apply_transaction_non_student_fee(self):
        account = BankAccount("12345", "NonStudent User", "A", 100.0, 0, "NP")
        account.apply_transaction(100.0)
        self.assertAlmostEqual(account.balance, 199.90)
        self.assertEqual(account.transaction_count, 1)
        print("test_apply_transaction_non_student_fee passed")

if __name__ == '__main__':
    unittest.main()