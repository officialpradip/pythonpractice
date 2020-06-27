'''10.	Write a Python program to remove the 
characters which have odd index	 values of a given string.  '''
def odd(s):
  display = "" 
  for i in range(len(s)):
    if i % 2 == 0:
      display = display + s[i]
  return display

print(odd('123456'))

