class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

    def bonus(self):
        print("Bonus:", self.salary * 0.10)


e1 = Employee("Sahil", 30000)
e2 = Employee("Rahul", 45000)

e1.display()
e1.bonus()

print()

e2.display()
e2.bonus()