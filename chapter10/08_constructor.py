class Employee:
    company = 'Google'
    def __init__(self, name, salary, subunit): # constructor 
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print(f"I am a constructor{self.name}")
    def getDetails(self):
        print(f'self {self.name}')
        print(f'salary {self.salary}')
        print(f'subunit {self.subunit}')

    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

    @staticmethod     # staticmethod is a decorator to mark a method as static
    def greet():
        print("Hello, I am a static method")    

    @staticmethod
    def time():
        print(f"Current time is")

rakib = Employee('Rakib', 100, 'Google')
rakib.getDetails()