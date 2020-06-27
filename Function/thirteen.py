'''13.	Write a Python program to sort a list of tuples using Lambda.'''

age = [('Ram', 80), ('Shyam', 42), ('Hari', 5)]
print(age)
age.sort(key = lambda x: x[1])
print('sorted age is:',age)
