class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!! Welcome to the Deposit & Withdrawal Machine")

    def deposit(self):
        amount=float(input("Enter amount to be deposited:"))
        self.balance+=amount
        print("\nAmount Deposited:",amount)

    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn:"))
        if(self.balance>=amount):
            self.balance=self.balance-amount
            print("\n You withdrew:",amount)
        else:
            print("\n Insufficient Balance")

    def display(self):
        print("\n Net available Balance=",self.balance)

l=Bank_Account()
l.deposit()
l.withdraw()
l.display()
        
