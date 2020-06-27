'''Write a Python program to count the number of strings where the string	
 length is 2 or more and the first and last character are same from a given
  list of strings.  
Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 
'''

def match(words):
  num = 0
  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      num += 1
  return num
print(match(['abc', 'xyz', 'aba', '1221']))
