from bank_account import BankAccount
from minimum_balance import MinimumBalanceAccount
from atm import ATM

account1 = BankAccount("user", "1234", balance=500)
account2 = MinimumBalanceAccount("admin", "1234", balance=1000, minimum_balance=200)

accounts = [account1, account2]

atm = ATM(accounts)
