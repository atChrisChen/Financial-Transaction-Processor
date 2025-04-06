from starter_code.transaction import Transaction
from starter_code.bank_account import BankAccount
from starter_code.bank_account_writer import write_new_current_accounts
from starter_code.bank_account_reader import read_old_bank_accounts

class TransactionManager:
    """
    Service class that handles transaction processing by interacting with bank accounts.
    """

    def process_transaction(self, transaction: Transaction, bank_accounts: list[BankAccount]) -> bool:
        """
        Processes a single transaction on a dict-based account system.
        """
        account = None
        transaction_acc_number = transaction.account_number.lstrip('0') or '0'

        # NOTE: if there is a transaction where a new account is being created, then it will not be in the masterBankAccounts file,
        #       therefore the following logic does not allow for "05" create account transaction
        # Search for the account
        for acc in bank_accounts:
            # Account found.
            if acc.account_number == transaction_acc_number:
                print(f"\nThe current account number: {acc.account_number} and the transaction account number: {transaction_acc_number} match")
                account = acc
                break
        # No account found.
        if account is None:
            print(f"Account {transaction.account_number} was not found.")
            return False

        # Process transaction based on transaction code.
        if transaction.transaction_code == "00":
            print("End of session.")
            return True
        elif transaction.transaction_code == "01":
            return self.withdraw(account, transaction.amount)
        #Note:  Missing transfer "02"
        
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
            print(f"Unknown transaction code: {transaction.transaction_code}")
            return False


    def withdraw(self, account: BankAccount, amount: float) -> bool:
        print("Withdraw function")
        if account.status == 'A' and account.balance >= amount:
            account.balance -= amount
            account.transaction_count += 1
            print("Withdrawal success.")
            return True
        else:
            print("Withdrawal fail.")
            return False
        
    def paybill(self, account: BankAccount, amount: float) -> bool:
        if account.status == 'A' and account.balance >= amount:
            account.balance -= amount
            account.transaction_count += 1
            print("Paybill successful.")
            return True
        print("Paybill failed.")
        return False
    
    def deposit(self, account: BankAccount, amount: float) -> bool:
        if account.status == 'A':
            account.balance += amount
            account.transaction_count += 1
            print("Deposit successful.")
            return True
        print("Deposit failed.")
        return False
    
    def create(self, account: BankAccount):
        # Add logic to see if it is already within the list of bank_accounts 
        current_accounts = read_old_bank_accounts("OldMasterBankAccounts.txt")
        current_accounts.append(account)
        # This should be creating a new current bank accounts file? 
            # Note: Perhaps we make a new currentMasterBankAccounts file? 
            # Also call the write_new_current_accounts() after all transacitons have been made and altered to each (account) or added / deleted from bank_accounts
        write_new_current_accounts(current_accounts, "OldMasterBankAccounts.txt")
        print("Account creation successful")
        account.transaction_count += 1

    def delete(self, account_to_delete: BankAccount) -> bool:
        current_accounts = read_old_bank_accounts("OldMasterBankAccounts.txt")
        # Note: directly changing the oldMasterBankAccounts file will cause issues when testing
            # our program. If we delete a bank account within the file, the next time we run the transactions, 
            # it won't be able to find that account since it has been deleted.
            # this is deleting the appropriate OldMasterBankAccounts.txt. Should it instead be
            # (similarly mentioned within the create function) deleting within the bank_accounts and then have write_new_current_accounts()  
            # called later to create the new currentMasterBankAccounts
        
        # for index, account in enumerate(current_accounts):
        #     if (account["account_number"] == account_to_delete.account_number and
        #         account["name"] == account_to_delete.holder_name):
        #         del current_accounts[index]
        #         print("Account deletion successful")
        #         write_new_current_accounts(current_accounts, "OldMasterBankAccounts.txt")
        #         return True
        print("Bank account not found")
        return False

    def disable(self, account_to_disable: BankAccount) -> bool:
        current_accounts = read_old_bank_accounts("OldMasterBankAccounts.txt")
        # Note: same idea mentioned in delete and create. Also the logic below is not necessary. We have already looped 
        # through each of the accounts to find the right one. Should be able to just change the status as mentioned
        account_to_disable.status = "D"
        return True
        # for index, account in enumerate(current_accounts):
        #     if (account["account_number"] == account_to_disable.account_number and
        #         account["name"] == account_to_disable.holder_name):
        #         current_accounts[index].status = "D"
        #         print("Account disabling successful")
        #         write_new_current_accounts(current_accounts, "OldMasterBankAccounts.txt")
        #         return True
        # print("Bank account not found")
        # return False

    def changePlan(self, account: BankAccount) -> bool:
        if account.status == 'A':
            if account.plan == "SP":
                account.plan = "NP"
            elif account.plan == "NP":
                account.plan = "SP"
            account.transaction_count += 1
            print("Plan change successful.")
            return True
        print("Plan change failed.")
        return False


    def process_all_transactions(self, transactions: list[Transaction], bank_accounts: list[BankAccount]) -> None:
        """
        Processes a batch of transactions sequentially. Applies each transaction to the relevant bank account.

        Args:
            transactions (list[Transaction]): A list of transactions to process.
            bank_accounts (list): A list of BankAccount objects representing the current accounts.
        """
        for transaction in transactions:
            # Conduct transaction process. If false, display error. 
            if not self.process_transaction(transaction, bank_accounts):
                print(f"Transaction code: {transaction.transaction_code} failed for account number: {transaction.account_number}.\n")
