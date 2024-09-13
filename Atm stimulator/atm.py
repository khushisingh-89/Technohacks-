class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    
    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Current balance is {self.balance}"
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn {amount}. current balnce is {self.balance}"
        
def main():
    atm = ATM()

    while True:
        print("\n==== Welcome to Seva bank ATM ====")
        print("1. Check balance")
        print("2. Deposit ")
        print("3. Withdraw ")
        print("4. Other options")
        print("5. Exit")

        choice = input("Enter the selected choice (1-5): ")

        if choice == '1':
            print(f"Your balance is : {atm.check_balance()}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("other options are: ")
        elif choice == '5':
            print("Thanku for using Seva bank ATM.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")


if __name__ == "__main__":
    main()