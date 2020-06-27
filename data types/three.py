'''3.	Write a Python program to get a string from a given string where all
occurrences of its first char have been changed to '$', 
except the first char itself.  
Sample String : 'restart' 
Expected Result : 'resta$t' 
'''
def occurrences(s):
  char = s[0]
  s = s.replace(char, '$')
  s = char + s[1:]

  return s

print(occurrences('restart'))

