'''
1.	Write a Python program to count the number of characters
 (character	 frequency) in a string. Sample String : google.com' 
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} 

'''
def frequency(s):
    count = {}
    for character in s:
        count[character] = s.count(character)
    return count
print(frequency('google.com'))