# BankAccount class
class BankAccount:

    # Constructor
    def __init__(self, accno, accholder, accbal):

        # Store account number
        self.accno = accno

        # Store account holder name
        self.accholder = accholder

        # Store initial account balance
        self.accbal = accbal

    # Method to deposit money
    def deposit(self):

        # Take deposit amount from user
        amount = int(input("Enter amount to deposit: "))

        # Check amount is greater than 0
        if amount > 0:
            self.accbal += amount
            print(f"Amount Deposited Successfully.")
        else:
            print("Invalid Amount")

        # Display updated balance
        print(f"Available Balance: {self.accbal}")

    # Method to withdraw money
    def withdraw(self):

        # Take withdrawal amount from user
        amount = int(input("Enter amount to withdraw: "))

        # Check sufficient balance
        if amount <= self.accbal:
            self.accbal -= amount
            print("Amount Withdrawn Successfully.")
            print(f"Remaining Balance: {self.accbal}")
        else:
            print("Insufficient Balance")

    # Method to check account balance
    def check_bal(self):

        # Return current balance
        return f"Available Balance is: {self.accbal}"