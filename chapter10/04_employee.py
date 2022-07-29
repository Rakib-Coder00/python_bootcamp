#class attribute:

class Employee:
    company = "Google"
    salary = 100000

harry = Employee()
rajni = Employee()
# harry.salary = 300
# rajni.salary = 500

print(harry.company) 
print(rajni.company) 
Employee.company = "Amazon"  
print(harry.company)
print(rajni.company)

# print(harry.salary)
# print(rajni.salary)

