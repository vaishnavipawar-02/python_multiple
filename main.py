class BankAccount:
    def  __init__(self,accno,accholder,accbal):
        self.accno=accno
        self.accholder=accholder
        self.accbal=accbal

    def deposit(self,amount):
        if amount>0:
            self.accbal+=amount


















def user_menu(account):
    while True:
        print("\nUser Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.display_balance()
        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == 4:
            break
        else:
            print("Invalid choice!")


def admin_menu(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Create Account")
        print("2. Display Acc Details")
        print("3. Calculate Interest")
        print("4. Deposite")
        print("5. Withdraw")
        print('6. Exit')
        choice=int(input("enter your choice: "))

        if choice==1:
            accno=input("enter account number: ")
            accholder=input("enter account holder name: ")
            accbal=float(input("enter account balance: "))
            interest_rate=float(input("enter interest rate: "))
            account=account(accno,accholder,accbal,interest_rate)
            admin.create_account(account)
        elif choice==2:
            accno=input("enter account no: ")
            admin.display_account_details(accno)
        elif choice==3:
            accno=input("enter account no: ")
            admin.calculate_interest(accno)
        elif choice==4:
            accno=input("enter account no: ")
            amount=float(input("enter amount to deposit: "))
            admin.deposit(accno,amount)
        elif choice==5:
            accno=input("enter account no: ")
            amount=float(input("enter amount to withdraw: "))
            admin.withdraw(accno,amount)
        elif choice==6:
            break


def main():
    admin = admin()
    while True:
        print("\nMain Menu:")
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account_number = input("Enter your account number: ")
            if account_number in admin.accounts:
                user_menu(admin.accounts[account_number])
            else:
                print("Account not found!")
        elif choice == 2:
            admin_menu(admin)
        elif choice == 3:
            break
        else:
            print("Invalid choice!")
