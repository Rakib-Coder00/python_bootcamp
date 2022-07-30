class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print('Lets add two numbers')
        return self.num + num2.num

    def __mul__(self, num2):
        print('Lets multiply two numbers')
        return self.num * num2.num

n1 = Number(10)
n2 = Number(20)  
print(n1 + n2)      
print(n1 * n2)      