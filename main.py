from starter_code.bank_account_reader import read_old_bank_accounts
from starter_code.transaction_manager import TransactionManager
from starter_code.transaction_reader import read_transactions
from starter_code.bank_account import BankAccount

def main(): 
    # Load Bank Accounts. Returns a list of accounts holding: (account number, account holder, status, current balance and # of transactions)
    accounts_dict = read_old_bank_accounts("OldMasterBankAccounts.txt")
    # Apparantly should not change the bank_account_reader starter code. 
    # Utilizing the bank account class here
    accounts = []
    for acc in accounts_dict: 
        
        print("the type for balance is: " , type(acc["balance"]))
        bank_account = BankAccount(
            account_number = acc["account_number"], 
            holder_name = acc["name"], 
            status = acc["status"], 
            balance = acc["balance"], 
            transaction_count = acc["total_transactions"], 
            plan = "S", # Files need to be updated to include a plan in them. For now will default to student
        )
        accounts.append(bank_account)
    
    print("\nAccounts loaded: ")
    for acc in accounts:
        print(acc)

    tm = TransactionManager()

    # Read transactions. Returns a list of transactions holding: (transaction code, account holder, account number, amount and misc)
    transactions = read_transactions("MergedBankAccountTransaction.txt")
    
    tm.process_all_transactions(transactions, accounts)
    
    print("\nAccounts after transaction:")
    for acc in accounts:
        print(acc)

if __name__ == "__main__": 
    main()
