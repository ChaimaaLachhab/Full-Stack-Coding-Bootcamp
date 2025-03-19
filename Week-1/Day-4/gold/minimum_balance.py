from bank_account import BankAccount;

class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("Authentication required!")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < self.minimum_balance:
            raise ValueError(f"Cannot withdraw! Balance cannot go below minimum balance of {self.minimum_balance}.")
        self.balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.balance}")
