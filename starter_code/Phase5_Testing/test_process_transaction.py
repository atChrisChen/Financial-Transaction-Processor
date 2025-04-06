class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number

class Transaction:
    def __init__(self, account_number, transaction_code, amount=0):
        self.account_number = account_number
        self.transaction_code = transaction_code
        self.amount = amount

class TransactionManager:
    def __init__(self):
        pass

    def process_transaction(self, transaction, bank_accounts):
        account = None
        transaction_acc_number = transaction.account_number.lstrip('0') or '0'

        for acc in bank_accounts:
            if acc.account_number == transaction_acc_number:
                account = acc
                break
        
        if account is None:
            return False

        if transaction.transaction_code == "00":
            return True
        elif transaction.transaction_code == "01":
            return self.withdraw(account, transaction.amount)
        elif transaction.transaction_code == "03":
            return self.paybill(account, transaction.amount)
        elif transaction.transaction_code == "04":
            return self.deposit(account, transaction.amount)
        elif transaction.transaction_code == "05":
            return self.create(account)
        elif transaction.transaction_code == "06":
            return self.delete(account)
        elif transaction.transaction_code == "07":
            return self.disable(account)
        elif transaction.transaction_code == "08":
            return self.changePlan(account)
        else:
            return False

    def withdraw(self, account, amount): return True
    def paybill(self, account, amount): return True
    def deposit(self, account, amount): return True
    def create(self, account): return True
    def delete(self, account): return True
    def disable(self, account): return True
    def changePlan(self, account): return True


# Test w/ mock.
def test_process_transaction():
    manager = TransactionManager()
    passed = True

    print("Starting tests...\n")

    test_cases = [
        # Finding account.
        ("Test 1: No account found", Transaction("999", "01"), [BankAccount("123")], False),
        ("Test 2: Account found on first iteration", Transaction("123", "04", 100), [BankAccount("123")], True),
        ("Test 3: Account found on second iteration", Transaction("123", "04", 100), [BankAccount("999"), BankAccount("123")], True),
        ("Test 4: Account found on last iteration", Transaction("123", "04", 100), [BankAccount("456"), BankAccount("789"), BankAccount("123")], True),
        ("Test 5: Empty account list", Transaction("123", "01"), [], False),
        
        # Transaction codes.
        ("Test 6: Transaction '00' End of session", Transaction("123", "00"), [BankAccount("123")], True),
        ("Test 7: Transaction '01' Withdraw", Transaction("123", "01", 100), [BankAccount("123")], True),
        ("Test 8: Transaction '03' Paybill", Transaction("123", "03", 100), [BankAccount("123")], True),
        ("Test 9: Transaction '04' Deposit", Transaction("123", "04", 100), [BankAccount("123")], True),
        ("Test 10: Transaction '05' Create", Transaction("123", "05"), [BankAccount("123")], True),
        ("Test 11: Transaction '06' Delete", Transaction("123", "06"), [BankAccount("123")], True),
        ("Test 12: Transaction '07' Disable", Transaction("123", "07"), [BankAccount("123")], True),
        ("Test 13: Transaction '08' Change Plan", Transaction("123", "08"), [BankAccount("123")], True),
        ("Test 14: Invalid transaction code", Transaction("123", "99"), [BankAccount("123")], False),
    ]

    for description, txn, accounts, expected in test_cases:
        print(description)
        result = manager.process_transaction(txn, accounts)
        if result == expected:
            print(f"PASS")
        else:
            print(f"FAIL")
            passed = False

    if passed:
        print("\nAll tests passed!")
    else:
        print("\nSome tests failed!")

test_process_transaction()