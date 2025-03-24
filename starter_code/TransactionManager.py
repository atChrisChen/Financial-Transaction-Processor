from starter_code.Transaction import Transaction
from starter_code.BankAccount import BankAccount

class TransactionManager:
    """
    Service class that handles transaction processing by interacting with bank accounts
    """

    def process_transaction(self, transaction: Transaction, bank_accounts: list) -> bool:
        """
        Processes a single transaction on a dict-based account system.
        """
        for acc in bank_accounts:
            # Note: Needs fix, currently the account numbers are of different format. 
            # print("the current account number: ", acc['account_number'], "and the transaction account number: transaction.account_number", transaction.account_number.lstrip('0') or '0')
            if acc['account_number'] == transaction.account_number.lstrip('0') or '0':
                account = acc
                break
            else:
                print(f"Account {transaction.account_number} not found.")
                return False
        
        print("The transaction code is :" ,transaction.transaction_code)
        if transaction.transaction_code == "00":
            print("End of session.")
            return True
        elif transaction.transaction_code == "01":
            return self.withdraw(account, transaction.amount)
        elif transaction.transaction_code == "02":
            # Missing 2 required positional arguments: 'amount' and bankAccounts
            # return self.transfer(account, transaction.amount)
            pass
        elif transaction.transaction_code == "03":
            return self.paybill(account, transaction.amount)
        elif transaction.transaction_code == "04":
            return self.deposit(account, transaction.amount)
        elif transaction.transaction_code == "05":
            return self.create(transaction, bank_accounts)
        elif transaction.transaction_code == "06":
            return self.delete(account, bank_accounts)
        elif transaction.transaction_code == "07":
            return self.disable(account, bank_accounts)
        elif transaction.transaction_code == "08":
            return self.change_plan(account, bank_accounts)
        else:
            print(f"Unknown transaction code: {transaction.transaction_code}")
            return False

    ### maybe handle each transaction as separate functions here
    def withdraw(self, account: dict, amount: float) -> bool:
        print("Withdraw function")
        if account['status'] == 'A' and account['balance'] >= amount:
            account['balance'] -= amount
            account['total_transactions'] += 1
            # Not yet a function
            # self.apply_fee(account)
            print(f"Withdrawal success.")
            return True
        else:
            print(f"Withdrawal failed.")
            return False
        
    def transfer(self, sourceAccount, destinationAccount, amount, bankAccounts):
        pass
    def paybill(self, account, amount):
        pass
    def deposit(self, account, amount):
        pass
    def create(self, account, amount):
        pass
    def delete(self, account, amount):
        pass
    def disable(self, account, amount):
        pass
    def change_plan(self, account, amount):
        pass

    


    def process_all_transactions(self, transactions: list[Transaction], bank_accounts: list) -> None:
        """
        Processes a batch of transactions sequentially. Applies each transaction to the relevant bank account.

        Args:
            transactions (list[Transaction]): A list of transactions to process.
            bank_accounts (list): A list of BankAccount objects representing the current accounts.
        """
        # loop through every transaction within the list
        for transaction in transactions:
            if not self.process_transaction(transaction, bank_accounts):
                print(f"Transaction code: {transaction.transaction_code} failed for account number: {transaction.account_number}.")