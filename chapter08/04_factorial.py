#n! = 1 * 2 * 3 *...* n
#n! = 1 * 2 * 3 *...(n-1) * n
#n! = (n-1) * n



# n = 4
# product = 1
# for i in range(n):
#     product = product * (1+1)
# print(product)


# def factorial_iter(n):
#     product = 1
#     for i in range(n):
#         product = product * (i+1)
#     return  product    
    
# print(factorial_iter(5))    


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n *factorial_recursive(n-1)
    
f =factorial_recursive(5)
print(f)  