from bank_account import BankAccount

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list) or not all(isinstance(acc, BankAccount) for acc in account_list):
            raise ValueError("Account_list must contain only BankAccount or MinimumBalanceAccount instances.")
        if not isinstance(try_limit, int) or try_limit <= 0:
            print("Invalid try limit, setting to default (2).")
            self.try_limit = 2
        else:
            self.try_limit = try_limit
        self.account_list = account_list
        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\nATM MENU")
            print("1️ Log In")
            print("2️ Exit")
            choice = input("Select an option: ")

            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == "2":
                print("Exiting ATM. Have a nice day!")
                break
            else:
                print("Invalid choice, please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                self.show_account_menu(account)
                return

        self.current_tries += 1
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down...")
            exit()
        else:
            print(f"Attempt {self.current_tries}/{self.try_limit}. Try again.")

    def show_account_menu(self, account):
        while True:
            print("\n🏦 ACCOUNT MENU")
            print("1️ Deposit")
            print("2️ Withdraw")
            print("3️ Logout")
            choice = input("Select an option: ")

            if choice == "1":
                try:
                    amount = int(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError as e:
                    print(f"{e}")

            elif choice == "2":
                try:
                    amount = int(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError as e:
                    print(f"{e}")

            elif choice == "3":
                print("Logging out...")
                account.authenticated = False
                break

            else:
                print("Invalid choice, please try again.")
