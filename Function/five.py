'''Write a Python function to calculate the factorial of a number
 (a non-negative integer).
 The function accepts the number as an argument. '''
def factorial(num):
     if num == 0:
        return 1
     else:
        return num * factorial(num-1)
num=int(input("Enter any Number : "))
print(factorial(num))
