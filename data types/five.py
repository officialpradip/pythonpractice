'''5.	Write a Python program to add 'ing' at the end of a given string 
(length should	 be at least 3). If the given string already ends with 'ing' 
then add 'ly' instead. If the string length of the given string is less 
than 3, leave it unchanged. 
Sample String : 'abc' 
Expected Result : 'abcing'  
Sample String : 'string' 
Expected Result : 'stringly' 
'''
def add_string(s):
  length = len(s)

  if length > 2:
    if s[-3:] == 'ing':
      s += 'ly'
    else:
      s += 'ing'
  return s
print(add_string('abc'))
print(add_string('string'))
