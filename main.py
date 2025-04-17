from starter_code.bank_account_reader import read_old_bank_accounts
from starter_code.transaction_manager import TransactionManager
from starter_code.transaction_reader import read_transactions
from starter_code.bank_account import BankAccount
import sys

def main(): 
    if len(sys.argv) != 4: 
        print("Usage: python3 main.py <OldMasterBankAccounts> <MergedTransactionFile> <OutputBankAccountsFile>")
        print("Requires these input")
        sys.exit(1)
    
    # This needs to get incorporated into the rest of the program still. Should replace a lot of the dummy accounts we tested with before
    old_accounts_file = sys.argv[1]
    merged_transactions_file = sys.argv[2]
    output_file = sys.argv[3]
    
    # Load Bank Accounts. Returns a list of accounts holding: (account number, account holder, status, current balance and # of transactions)
    accounts_dict = read_old_bank_accounts(old_accounts_file)
    # Apparantly should not change the bank_account_reader starter code. 
    # Utilizing the bank account class here
    accounts = []
    for acc in accounts_dict: 
        
        # print("the type for balance is: " , type(acc["balance"]))
        bank_account = BankAccount(
            account_number = acc["account_number"], 
            holder_name = acc["name"], 
            status = acc["status"], 
            balance = acc["balance"], 
            transaction_count = acc["total_transactions"], 
            plan = acc["plan"], # Files need to be updated to include a plan in them. For now will default to student
        )
        accounts.append(bank_account)
    
    print("\nAccounts loaded: ")
    for acc in accounts:
        print(acc)

    # Handles transaction processing with bank accounts
    tm = TransactionManager()

    # Read transactions. Returns a list of transactions holding: (transaction code, account holder, account number, amount and misc)
    transactions = read_transactions(merged_transactions_file)
    
    tm.process_all_transactions(transactions, accounts)
    
    print("\nAccounts after transaction:")
    for acc in accounts:
        print(acc)

    # Write updated accounts to output file
    with open(output_file, 'w') as f:
        for acc in accounts:
            # Format: account_number(5) + space + name(20) + space + status(1) + space + balance(8) + space + transactions(4) + space + plan(2)
            line = f"{acc.account_number:05d} {acc.holder_name:20s} {acc.status} {acc.balance:8.2f} {acc.transaction_count:04d} {acc.plan}\n"
            f.write(line)

if __name__ == "__main__": 
    main()
