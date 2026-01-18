import random

class Bank:
    def __init__(self, balance, accno, name, pin):
        self.balance = balance
        self.accno = accno
        self.name = name
        self.pin = pin
        self.trasactions=[]

    def verify_pin(self, entered_pin):
        return self.pin == entered_pin

    def viewaccount(self):
        print("Account holder:", self.name)
        print("Account number:", self.accno)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.trasactions.append(f"Withdrawn amount : {amount}")
            print("Withdrawal successful")
            print("New balance:", self.balance)

    def credit(self, amount):
        self.balance += amount
        self.trasactions.append(f"Credit amount : {amount}")
        print("Credit successful")
        print("New balance:", self.balance)

    def transactionhistory(self):
        if not self.trasactions:
            print("NO transaction history : ")
        else:
            print(" Transaction history ")
            for i,t in enumerate(self.trasactions,start=1):
                print(f"{i}.{t}")






accounts={}
while True:
   ch=int(input("Enter your choice : 1.Create account  ||  2.Login  ||  3.Log out : "))

   if ch==1:
       name=input("Enter your name : ")
       pin=int(input("Set your four digit pin : "))
       accno=random.randint(100000,900000)
       accounts[accno]=Bank(10000,accno,name,pin)
       print("Your account is created")
       print("Your account number is : ",accno)

   elif ch == 2:
       accno = int(input("Enter your account number: "))

       if accno not in accounts:
           print("Account not found")
           continue

       bank = accounts[accno]   # ✅ correct object

       attempts = 3
       authenticated = False

       while attempts > 0:
           pin1 = int(input("Enter your PIN: "))
           if bank.verify_pin(pin1):
               print("Login successful")
               authenticated = True
               break
           else:
               attempts -= 1
               print(f"Wrong PIN. Attempts left: {attempts}")

       if not authenticated:
           print("Account locked temporarily")
           continue

       # ---- ACCOUNT MENU ----
       while True:
           choice = int(input(
               "\n1. View account\n"
               "2. Withdraw\n"
               "3. Credit\n"
               "4.Transaction history\n"
               "5. Logout\n"
           ))

           if choice == 1:
               bank.viewaccount()

           elif choice == 2:
               amt = int(input("Enter withdrawal amount: "))
               bank.withdraw(amt)

           elif choice == 3:
               amt = int(input("Enter credit amount: "))
               bank.credit(amt)

           elif choice==4:
               bank.transactionhistory()

           elif choice == 5:
               print("Logged out")
               break

           else:
               print("Invalid choice")

   else:
       print("THANK YOU")
       break
