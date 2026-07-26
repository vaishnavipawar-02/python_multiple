from bankaccount import BankAccount

# SavingAccount class inherits BankAccount
class savingaccount(BankAccount):

    # Constructor
    def __init__(self, accno, accholder, accbal, intrest_rate):
        super().__init__(accno, accholder, accbal)

        # Store interest rate
        self.intrest_rate = intrest_rate

    # Calculate interest
    def calculate_ins(self):

        # User enters principal amount
        amount = int(input("Enter amount: "))

        # User enters number of months
        mon = int(input("Enter months: "))

        # Monthly interest rate
        per_mon = 0.7

        # Calculate interest
        interest = (amount * per_mon * mon) / 100

        print(f"Interest Earned: {interest}")

        return interest

    # Add interest to account balance
    def apply_ins(self):

        self.accbal += self.intrest_rate

        return f"Balance after adding interest: {self.accbal}"