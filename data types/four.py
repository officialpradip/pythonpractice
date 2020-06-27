'''4.	Write a Python program to get a single string from two given 
strings, separated	 by a space and swap the first two characters of 
each string. 
Sample String : 'abc', 'xyz'  
Expected Result : 'xyc abz' 
'''
a = 'abc'
b = 'xyz'
change_a = b[:2] + a[2:]
change_b = a[:2] + b[2:]
print(f'change of a & b is {change_a} {change_b}')

