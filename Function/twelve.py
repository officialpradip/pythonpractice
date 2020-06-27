'''12.	Write a Python program to create a function that takes one argument,
 and	 that argument will be multiplied with an unknown given number.  '''

 
def multiplied(n):
    return lambda x : x * n
result = multiplied(2)
print("Multiplication of 2 with 1 is =", result(1))
result = multiplied(3)
print("Multiplication of 3 with 2 is =", result(2))


