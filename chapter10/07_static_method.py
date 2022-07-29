class Employee:
    company = 'Google'
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    @staticmethod     # staticmethod is a decorator to mark a method as static
    def greet():
        print("Hello, I am a static method")    

    @staticmethod
    def time():
        print(f"Current time is")


harry = Employee()
harry.salary = 100000
harry.greet() # Employee.greet(harry)
harry.time() # Employee.time()