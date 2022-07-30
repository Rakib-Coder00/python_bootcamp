class Employee:
    company = 'Visa'
    eCode = 120

class FreeLancer:
    company = 'Fiverr'
    level = 0

    def upgradeLevel(self):
        self.level += 1

class Programmer(Employee, FreeLancer):
    name = 'John'

p = Programmer()  
p.upgradeLevel()
# print(p.level)  
print(p.company)    