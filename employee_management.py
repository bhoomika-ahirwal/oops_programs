class Employee:
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