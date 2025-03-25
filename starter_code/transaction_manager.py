from starter_code.transaction import Transaction
from starter_code.bank_account import BankAccount

class TransactionManager:
    """
    Service class that handles transaction processing by interacting with bank accounts.
    """

    def process_transaction(self, transaction: Transaction, bank_accounts: list) -> bool:
        """
        Processes a single transaction on a dict-based account system.
        """
        account = None
        transaction_acc_number = transaction.account_number.lstrip('0') or '0'

        # Search for the account
        for acc in bank_accounts:
            print(f"The current account number: {acc['account_number']} and the transaction account number: {transaction_acc_number}")
            # Account found.
            if acc['account_number'] == transaction_acc_number:
                account = acc
                break
        # No account found.
        if account is None:
            print(f"Account {transaction.account_number} not found.")
            return False

        print(f"The transaction code is: {transaction.transaction_code}")


        # Process transaction based on transaction code.
        if transaction.transaction_code == "00":
            print("End of session.")
            return True
        elif transaction.transaction_code == "01":
            return self.withdraw(account, transaction.amount)
        elif transaction.transaction_code == "04":
            return self.deposit(account, transaction.amount)
        else:
            print(f"Unknown transaction code: {transaction.transaction_code}")
            return False


    def withdraw(self, account: dict, amount: float) -> bool:
        print("Withdraw function")
        if account['status'] == 'A' and account['balance'] >= amount:
            account['balance'] -= amount
            account['total_transactions'] += 1
            print("Withdrawal success.")
            return True
        else:
            print("Withdrawal fail.")
            return False

    def deposit(self, account: dict, amount: float) -> bool:
        if account['status'] == 'A':
            account['balance'] += amount
            account['total_transactions'] += 1
            print("Deposit successful.")
            return True
        print("Deposit failed.")
        return False

    def process_all_transactions(self, transactions: list[Transaction], bank_accounts: list) -> None:
        """
        Processes a batch of transactions sequentially. Applies each transaction to the relevant bank account.

        Args:
            transactions (list[Transaction]): A list of transactions to process.
            bank_accounts (list): A list of BankAccount objects representing the current accounts.
        """
        for transaction in transactions:
            if not self.process_transaction(transaction, bank_accounts):
                print(f"Transaction code: {transaction.transaction_code} failed for account number: {transaction.account_number}.")
