'''2.	Write a Python program to get a string made of the first 2 and the 
last 2 chars from a given a string.If the string length is less than 2, 
return instead of the empty string. 
Sample String : 'Python'    Expected Result : 'Pyon' 
Sample String : 'Py'        Expected Result : 'PyPy' 
Sample String : ' w'        Expected Result : Empty String  
'''
def first2_last_2(s):
  if len(s) < 2:
    return ''

  return s[0:2] + s[-2:]

print(first2_last_2('Python'))
print(first2_last_2('Py'))
print(first2_last_2('w'))


