from starter_code.Transaction import Transaction
from starter_code.TransactionManager import TransactionManager
from starter_code.BankAccountReader import read_old_bank_accounts

def read_transactions(file_path):
    """
    Reads and parses the merged transaction file.
    Returns a list of Transaction objects.
    """
    transactions = []
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, 1):
            clean_line = line.rstrip('\n')
            try:
                transaction_code = clean_line[:2]
                account_holder = clean_line[3:23].strip() 
                account_number = clean_line[23:29].strip() 
                amount = float(clean_line[29:37].strip()) 
                misc_data = clean_line[37:].strip() 

                print(f"Line {line_num}:")
                print(f"  Transaction Code: {transaction_code}")
                print(f"  Account Holder: {account_holder}")
                print(f"  Account Number: {account_number}")
                print(f"  Amount: {amount}")
                print(f"  Misc Data: {misc_data}")

                transaction = Transaction(transaction_code, account_holder, account_number, amount, misc_data)
                transactions.append(transaction)

            except Exception as e:
                print(f"ERROR: Fatal error - Line {line_num}: Unexpected error: {str(e)}")
                continue

    return transactions

def main():
    accounts_dict = read_old_bank_accounts("OldMasterBankAccounts.txt")
    
    print("\nAccounts loaded: ")
    for account in accounts_dict:
        print(account)

    transactions = read_transactions("MergedBankAccountTransaction.txt")

    # Process transactions.
    tm = TransactionManager()
    tm.process_all_transactions(transactions, accounts_dict)

    print("\nAccounts after transactions:")
    for account in accounts_dict:
        print(account)

if __name__ == "__main__":
    main()
