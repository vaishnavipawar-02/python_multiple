# Import savingaccount class from savingacc.py
from savingacc import savingaccount

# premium class inherits savingaccount class
class premium(savingaccount):

    # Constructor
    def __init__(self, accno, accholder, accbal, intrest_rate):

        # Call parent (savingaccount) constructor
        super().__init__(accno, accholder, accbal, intrest_rate)

    # Method to calculate premium account benefits
    def calculate_benefits(self):

        # Check minimum balance for premium benefits
        if self.accbal >= 5000:

            # Fixed benefit amount
            benefits = 500

            print(f"You earn Rs {benefits}")

            # Ask user whether to add benefits to account
            choice = input("Do you want to add this benefits amount to your account: ")

            # If user enters 'y', add benefits to balance
            if choice == 'y':
                self.accbal += benefits

                print(f"Benefits added successfully.\nAvailable Balance: {self.accbal}")

            # If user enters anything else
            else:
                print("Benefits not added as per your choice.")

        # If minimum balance is not maintained
        else:
            print("Maintain minimum balance of Rs.5000 for Premium Account.")


# Create object of premium class
obj = premium(
    101,
    "Hemant",
    10000,
    5
)

# Deposit amount into account
obj.deposit()

# Withdraw amount from account
obj.withdraw()

# Calculate interest
obj.calculate_ins()

# Apply interest to account balance
obj.apply_ins()

# Calculate and apply premium benefits
obj.calculate_benefits()