'''8.	Write a Python program to remove 
the n	th index character from a nonempty string.  '''

def remove(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove('Pradip', 0))
print(remove('Pradip', 3))
print(remove('Pradip', 5))
