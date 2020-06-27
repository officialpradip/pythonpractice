'''Write a Python program to convert a tuple to a string'''

def convertTuple(t): 
	str = ''.join(t) 
	return str
tuple = ('r', 'a', 'm') 
str = convertTuple(tuple) 
print(str) 
