from starter_code.BankAccountReader import read_old_bank_accounts

def main(): 
    file_path = "OldMasterBankAccounts.txt"
    accounts = read_old_bank_accounts(file_path)
    
    print("\nAccounts loaded: ")
    for account in accounts:
        print(account)

if __name__ == "__main__": 
    main()