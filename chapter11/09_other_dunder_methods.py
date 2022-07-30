class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print('Lets add two numbers')
        return self.num + num2.num 

    def __mul__(self, num2):
        print('Lets multiply two numbers')
        return self.num * num2.num  

    def __str__(self):
        return f'Decimal Number: {self.num}'  # return a string representation of the object

    def __len__(self):
        return len(str(self.num)) # return the length of the number

n = Number(90)
print(n)
print(len(n))