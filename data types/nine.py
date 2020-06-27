'''9.	Write a Python program to change a given string to a new 
string where the first	 and last chars have been exchanged. '''

def exchange(s):
      return s[-1:] + s[1:-1] + s[:1]	  
print(exchange('nama'))

