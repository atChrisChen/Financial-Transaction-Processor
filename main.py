from starter_code.BankAccountReader import read_old_bank_accounts
from starter_code.Transaction import Transaction
from starter_code.TransactionManager import TransactionManager
from starter_code.TransactionReader import read_transactions

def main(): 
    # Load Bank Accounts
    accounts_dict = read_old_bank_accounts("OldMasterBankAccounts.txt")
    
    print("\nAccounts loaded: ")
    for account in accounts_dict:
        print(account)

    tm = TransactionManager()

    # Read transactions
    transactions = read_transactions("MergedBankAccountTransaction.txt")
    
    tm.process_all_transactions(transactions, accounts_dict)
    
    print("\nAccounts after transaction:")
    for account in accounts_dict:
        print(account)

if __name__ == "__main__": 
    main()
