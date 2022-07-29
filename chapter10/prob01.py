class Programmer:
    company = 'microsoft'
    def __init__(self,name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f'the name of the programmer is {self.name} and the product is {self.product}')


rakib = Programmer('Rakib', 'python')
alka  = Programmer('Alka', 'java')
rakib.getinfo()
alka.getinfo()