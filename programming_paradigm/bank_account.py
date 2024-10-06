class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize with an initial balance, defaulting to zero."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        self.__account_balance += amount

    def withdraw(self, amount):
        """Withdraw the amount if funds are sufficient, otherwise return False."""
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")