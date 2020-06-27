'''Write a Python program to remove an item from a tuple'''

tuplex = 'r','a','m'
print(tuplex)
tuplex = tuplex[:2] + tuplex[3:]
print(tuplex)
listx = list(tuplex) 
listx.remove("a") 
tuplex = tuple(listx)
print(tuplex)
