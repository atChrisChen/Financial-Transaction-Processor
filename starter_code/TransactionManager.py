from starter_code.Transaction import Transaction


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