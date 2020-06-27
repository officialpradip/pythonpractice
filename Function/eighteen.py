'''18.	Write a Python program
 to check whether a given string is number or not	 using Lambda. '''

check = lambda q: q.replace('.','',1).isdigit()
print(check('2'))
print(check('2.2'))
print("\nPrint checking numbers:")
check_num = lambda r: check(r[1:]) if r[0]=='-' else check(r)
print(check_num('-1'))
