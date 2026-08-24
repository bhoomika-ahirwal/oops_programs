class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, entered_pin):
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Available balance: ₹{self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Please collect your cash.")


atm = ATM("1234", 10000)

entered_pin = input("Enter PIN: ")

if not atm.verify_pin(entered_pin):
    print("Incorrect PIN.")
else:

    while True:
        print("\n--- ATM ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter amount: "))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount: "))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice.")