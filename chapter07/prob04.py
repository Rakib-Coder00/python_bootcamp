#n! = 1 * 2 * 3 *...*8*n

from math import factorial


num = int(input("Enter the Number :\n"))
factorial = 1
for i in range(1, num+1):
    factorial = factorial * i

print(f"The number is {factorial}")