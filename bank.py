#Create a more sophisticated banking system simulation that allows a user to manage their
#account with additional features, while still enabling basic operations like deposit,
#withdrawal, and balance checking using do while loop.
#Requirements:
#Initial Setup:
#Start with an initial balance of $5000.
#Operations Menu:
#Prompt the user to choose from the following options:
#Deposit money
#Withdraw money
#Check balance
#Transfer money to another account (implement this with a simple hardcoded recipient
#account)
#Exit the program
#Balance Management:
#After each operation, display the updated balance.
#Ensure that the withdrawal amount does not exceed the current balance.
#Validate the deposit amount to ensure it is positive.
#Transfer Feature:
#Allow the user to transfer a specified amount to a hardcoded recipient account with a
#fixed balance (e.g., $500).
#Ensure that the user has enough balance to complete the transfer.
#Update both the user's balance and the recipient account balance accordingly.
#Looping and User Prompts:
#After each operation, ask the user if they want to perform another action.
#Use a do-while loop to allow for repeated operations within the main menu.
#Use another do-while loop for confirming the action after each operation.
#Exit Confirmation:
#When the user chooses to exit, ask for confirmation to ensure they want to terminate the
#program


class Bank:
    idCounter = 0
    def __init__(self,name,initialBalance):
        Bank.idCounter = Bank.idCounter+1
        self.id  =Bank.idCounter
        self.name=name
        self.balance = initialBalance
    def withdraw(self,withdrawBalance):
        if(withdrawBalance>self.balance or self.balance==0 or withdrawBalance<0):
            print("\nInvalid Amount")
            return self.balance
        else:
            self.balance = self.balance-withdrawBalance
            return self.balance

    def deposit(self,depositBalance):
        if(depositBalance<0):
            print("\nInvaild Amount")
            return self.balance
        else:
            self.balance = self.balance+depositBalance
            return self.balance

    def transferBalance(self,other,transferBalance):
        if(self.balance<transferBalance or self.balance<0 or transferBalance<0):
            return self.balance
        else:
            self.balance = self.balance - transferBalance
            other.balance = other.balance + transferBalance
            return self.balance

    def checkBalance(self):
        return self.balance
    

def main():
    userAccount = Bank("Hamza",1000)
    recipientAccount = Bank("Mustafa",100)
    while(True):
        print("1. Enter for check Balance")
        print("2. Enter for Deposit Balance")
        print("3. Enter for Withdraw Balance")
        print("4. Enter for Transfer Balance")
        print("5. Enter for Exit")
        choice = int(input("Enter Your Choice : "))

        if(choice==1):
            print(f"Your Balance is : {userAccount.checkBalance()}")
        elif(choice==2):
            depositBalance = int(input("Enter your DepositBalance : "))
            print(f"Your Balance is : {userAccount.deposit(depositBalance)}")   
        elif(choice==3):
            withdrawBalance = int(input("Enter WithdrawBalance : "))
            print(f"Your Balance is : {userAccount.withdraw(withdrawBalance)}")
        elif(choice==4):
            transferBalance = int(input("Enter TransferBalance : "))
            print(f"Your Balance is : {userAccount.transferBalance(recipientAccount,transferBalance)}")
        elif(choice==5):
            break
        else:
            print("Invalid Input!!! try Again")

        
if(__name__=="__main__"):
    main()