'''11.	Write a Python program to create a lambda function that
 adds 15 to a given	 number passed in as an argument, also create a 
 lambda function that multiplies argument
 x with argument y and print the result.  '''
result = lambda a : a + 15
print(result(1))
result = lambda x, y : x * y
print(result(2, 4))
