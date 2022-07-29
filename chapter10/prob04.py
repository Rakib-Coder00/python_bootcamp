class Calculator:
    def __init__(self, num):
        self.number = num
    def square(self):
        print(f'{self.number} squared is {self.number**2}')
    def squareRoot(self):
        print(f'{self.number} square root is {self.number**0.5}')
    def cube(self):
        print(f'{self.number} cubed is {self.number**3}')

    @staticmethod
    def greet():
        print('Hello World')



a = Calculator(5)
a.square()
a.squareRoot()
a.cube()
a.greet()