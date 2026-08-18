# Employee Management System

class Employee:
    def __init__(self, employee_id, name, salary, category):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.category = category

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Category:", self.category)
        print()


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_all_employees(self):
        print("\n--- Employee Information ---")
        for employee in self.employees:
            employee.display()


company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    print("\nEnter details for Employee", i + 1)
    employee_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    salary = float(input("Enter Salary: "))

    if salary >= 70000:
        category = "High Salary"
    elif salary >= 40000:
        category = "Medium Salary"
    else:
        category = "Low Salary"

    employee = Employee(employee_id, name, salary, category)
    company.add_employee(employee)

company.display_all_employees()

'''
Output

Enter number of employees: 2

Enter details for Employee 1
Enter Employee ID: 334
Enter Name: Sahil
Enter Salary: 75000

Enter details for Employee 2
Enter Employee ID: 345
Enter Name: Prasad
Enter Salary: 30000

--- Employee Information ---
Employee ID: 334
Name: Sahil
Salary: 75000.0
Category: High Salary

Employee ID: 345
Name: Prasad
Salary: 30000.0
Category: Low Salary
'''