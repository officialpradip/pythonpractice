'''17.	Write a Python program to multiplies all the items in a list.	  '''

def multiply(items):
    num = 1
    for x in items:
        num *= x
    return num
print(multiply([1,2,3,4,5]))
