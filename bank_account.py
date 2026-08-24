class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount:.2f} withdrawn successfully.")

    def display_balance(self):
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Balance: ₹{self.balance:.2f}")


name = input("Enter account holder name: ")
account = BankAccount(name)

while True:
    print("\n--- Banking System ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.display_balance()

    elif choice == "4":
        print("Thank you.")
        break

    else:
        print("Invalid choice.")class Employee:
    def __init__(self, employee_id, name, department, salary):
        self.employee_id = employee_id
        self.name = name
        self.department = department
        self.salary = salary

    def display(self):
        print(
            f"ID: {self.employee_id} | "
            f"Name: {self.name} | "
            f"Department: {self.department} | "
            f"Salary: ₹{self.salary:.2f}"
        )


employees = []

count = int(input("Enter number of employees: "))

for i in range(count):
    print(f"\nEmployee {i + 1}")

    employee_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employee = Employee(
        employee_id,
        name,
        department,
        salary
    )

    employees.append(employee)


print("\n--- Employee Records ---")

for employee in employees:
    employee.display()