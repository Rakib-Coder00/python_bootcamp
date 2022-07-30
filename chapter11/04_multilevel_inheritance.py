class Person:
    country = "America"

    def takeBreak(self):
        print("Take a break")
class Employee(Person):
    company = "Google"

    def getSalary(self):
        print(f"Salary: {self.salary}")

    def takeBreak(self):
        print("I am at work.....")


class Programmer(Employee):
    company = "Facebook"
    def getSalary(self):
        print(f"Salary: {self.salary}")


p = Person()
e = Employee()
e.takeBreak()
pr = Programmer()