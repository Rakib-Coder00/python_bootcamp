class Employee:
    company = 'Google'

    def showDetails(self):
        print("This is an Employee")

class Programmer(Employee):
    lang = 'Python'
    company = 'Amazon'

    def getLang(self):
        print(f'The language is {self.lang}')

    def showDetails(self):
        print("This is an Programmer")

e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()

print(p.company)