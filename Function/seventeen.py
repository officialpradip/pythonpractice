'''17.	Write a Python program to find
 if a given string starts with a given character	 using Lambda.  '''

word = lambda x: True if x.startswith('P') else False
print(word('Pradip'))
word = lambda x: True if x.startswith('Z') else False
print(word('Thapa'))
