'''15.	Write a Python function to insert a string in the middle of a string.
	  Sample function and result :  
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]] 
insert_sting_middle('{{}}', 'PHP') -> {{PHP}} 
'''

def insert(s, word):
	return s[:2] + word + s[2:]
print(insert('[[]]', 'Python'))
print(insert('{{}}', 'PHP'))
print(insert('<<>>', 'HTML'))
