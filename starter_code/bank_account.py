class BankAccount: 
    """
    Represents a bank account with attributes for account details and methods for transaction handling. 
    """

    def __init__(self, account_number: str, holder_name: str, status: str, balance: float, transaction_count: int, plan: str):
        # Initializes a bank account with given attributes.
        self.account_number = account_number
        self.holder_name = holder_name
        self.status = status
        self.balance = balance
        self.transaction_count = transaction_count
        self.plan = plan

    def is_active(self) -> bool:
        # Checks if account is active.
        return self.status == 'A'

    def apply_transaction(self, amount: float):
        # Applies a transaction to the account.
        if not self.is_active():
            raise ValueError("Cannot apply transaction to a disabled account.")
        
        self.balance += amount
        self.transaction_count += 1
        self.apply_fee()

    def can_withdraw(self, amount: float) -> bool:
        # Checks if withdrawal is allowed based on account balance.
        if not self.is_active():
            return False
        return self.balance >= amount

    def apply_fee(self):
        # Applies a transaction fee based on account type).
        if self.plan == 'SP':
            fee = 0.05
        else:
            fee = 0.10
        self.balance -= fee
        
    def __str__(self) -> str:
        return (
            f"acount number: {self.account_number}\n"
            f"holder name: {self.holder_name}\n"
            f"status: {self.status}\n"
            f"balance: {self.balance}\n"
            f"amount of transactions: {self.transaction_count}\n"
            f"plan type: {self.plan}\n"
        )
    
