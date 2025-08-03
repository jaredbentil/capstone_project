# Objective: Understand the fundamentals of OOP in Python by implementing a BankAccount class that encapsulates banking operations. Use command line arguments to interact with instances of this class.

# Task Description:
# You will create two Python scripts: bank_account.py, which contains the BankAccount class, and main-0.py, which interfaces with the class through command line arguments to perform banking operations.

# bank_account.py:
# Class Definition:

# Define a class named BankAccount.
# Use the __init__ method to initialize an account_balance attribute. Optionally, accept an initial balance parameter, defaulting to zero.
# Encapsulation and Behaviors:

# Implement deposit(amount), withdraw(amount), and display_balance() methods.
# deposit should add the specified amount to account_balance.
# withdraw should deduct the amount from account_balance if funds are sufficient, returning True; otherwise, return False and do not alter the balance.
# display_balance should print the current balance in a user-friendly format.

# main-0.py for Command Line Interaction:
# This script utilizes BankAccount through command line arguments for banking operations.

# Implementation Notes for you:
# Ensure your BankAccount class in bank_account.py correctly implements the specified functionalities and adheres to the principles of encapsulation.
# Use main.py to test your BankAccount class by performing various operations. Adjust the initial balance as needed for testing different scenarios.
# This task combines learning OOP concepts with practical command line interaction, enhancing your understanding of Python programming.

# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")



