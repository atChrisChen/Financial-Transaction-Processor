from starter_code.bank_account_reader import read_old_bank_accounts
from starter_code.transaction import Transaction
from starter_code.transaction_manager import TransactionManager
from starter_code.transaction_reader import read_transactions

def main(): 
    # Load Bank Accounts. Returns a list of accounts holding: (account number, account holder, status, current balance and # of transactions)
    accounts_dict = read_old_bank_accounts("OldMasterBankAccounts.txt")
    #Note: currently the bank account class is not being used as an object within the accounts_dict list
    
    print("\nAccounts loaded: ")
    for account in accounts_dict:
        print(account)

    tm = TransactionManager()

    # Read transactions. Returns a list of transactions holding: (transaction code, account holder, account number, amount and misc)
    transactions = read_transactions("MergedBankAccountTransaction.txt")
    
    tm.process_all_transactions(transactions, accounts_dict)
    
    print("\nAccounts after transaction:")
    for account in accounts_dict:
        print(account)

if __name__ == "__main__": 
    main()
