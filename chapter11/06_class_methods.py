class Employee:
    company = "Google"
    salary = 100
    location = "Mountain View"

    # def changeSalary(self, sal):
    #     self.__class__.salary = sal 

    @classmethod  # decorator to define a class method
    def changeSalary(cls, sal):
        cls.salary = sal 
    

e = Employee()
print(e.salary)
e.changeSalary(200)
print(e.salary)
print(Employee.salary)