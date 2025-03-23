class Transaction:
    """
    Represents a banking transaction with details about the transaction type, involved account, amount, and additional data.
    """
    
    def __init__(self, transaction_code: str, account_holder: str, account_number: str, amount: float, misc_data: str):
        """
        Initializes a transaction with the provided details.
        
        Args:
            transaction_code (str): The code representing the transaction type (e.g., "01" for withdrawal).
            account_holder (str): The name of the account holder involved in the transaction.
            account_number (str): The account number involved in the transaction.
            amount (float): The amount of money involved in the transaction.
            misc_data (str): Any additional information related to the transaction (e.g., recipient account for transfers).
        """
        self.transaction_code = transaction_code
        self.account_holder = account_holder
        self.account_number = account_number
        self.amount = amount
        self.misc_data = misc_data