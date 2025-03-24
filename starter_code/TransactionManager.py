from starter_code.Transaction import Transaction
from starter_code.BankAccount import BankAccount

class TransactionManager:
    """
    Service class that handles transaction processing by interacting with bank accounts
    """

    def process_transaction(self, transaction: Transaction, bank_accounts: list) -> bool:
        """
        Processes a single transaction and updates the corresponding bank account.
        Returns True if successful, False if failed.

        Args:
            transaction (Transaction): The transaction to be processed.
            bank_accounts (list): A list of BankAccount objects representing the current accounts.

        Returns:
            bool: True if the transaction was processed successfully, False otherwise.
        """
        for acc in bank_accounts:
            if acc.account_number == transaction.account_number:
                account = acc
                break
        else:
            print(f"Account {transaction.account_number} not found.")
            return False
        
        if transaction.transaction_code == "00": 
            print("End of session.")
            return True
        elif transaction.transaction_code == "01":  
            return self.withdraw(account, transaction.amount)
        elif transaction.transaction_code == "03":  
            return self.paybill(account, transaction.amount)
        elif transaction.transaction_code == "04":  
            return self.deposit(account, transaction.amount)
        elif transaction.transaction_code == "05": 
            return self.create(transaction, bank_accounts)
        elif transaction.transaction_code == "06": 
            return self.delete(account, bank_accounts)
        elif transaction.transaction_code == "07": 
            return self.disable(account)
        elif transaction.transaction_code == "08": 
            return self.changePlan(account)
        else:
            print(f"Unknown transaction code: {transaction.transaction_code}")
            return False

    ### maybe handle each transaction as separate functions here
    def withdraw(self, account, amount):
        pass
    def transfer(self, sourceAccount, destinationAccount, amount, bankAccounts):
        pass
    def paybill(self, account, amount):
        pass
    def deposit(self, account, amount):
        pass


    def process_all_transactions(self, transactions: list[Transaction], bank_accounts: list) -> None:
        """
        Processes a batch of transactions sequentially. Applies each transaction to the relevant bank account.

        Args:
            transactions (list[Transaction]): A list of transactions to process.
            bank_accounts (list): A list of BankAccount objects representing the current accounts.
        """
        for transaction in transactions:
            if not self.process_transaction(transaction, bank_accounts):
                print(f"Transaction failed: {transaction.transaction_code} for account {transaction.account_number}.")