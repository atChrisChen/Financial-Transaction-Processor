from starter_code.transaction_manager import TransactionManager
from starter_code.bank_account import BankAccount

def test_withdraw():
    manager = TransactionManager()
    passed = True

    print("Starting withdraw tests...\n")

    test_cases = [
        ("Test 1: Successful withdrawal", BankAccount("12345", "Name one", "A", 1000.00, 0, "SP"), 500.00, {"balance": 500.00, "transaction_count": 1}, True),
        ("Test 2: Failed withdrawal (inactive account)",  BankAccount("11111", "Name two", "D", 1000.00, 0, "SP"), 500.00, {"balance": 1000.00, "transaction_count": 0}, False),
        ("Test 3: Failed withdrawal (insufficient balance)",  BankAccount("12222", "Name three", "A", 100.00, 0, "SP"), 500.00, {"balance": 100.00, "transaction_count": 0}, False)
    ]

    for description, account, amount, expected_state, expected_result in test_cases:
        print(description)
        result = manager.withdraw(account, amount)
        if (result == expected_result and 
            account.balance == expected_state["balance"] and 
            account.transaction_count == expected_state["transaction_count"]):
            print("Test Passed!")
        else:
            print("Test Failed!")
            passed = False

    if passed:
        print("\nAll withdraw tests passed")
    else:
        print("\nSome withdraw tests failed")

test_withdraw()