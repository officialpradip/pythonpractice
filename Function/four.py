'''Write a Python program to reverse a string. 
Sample String : "1234abcd" 
Expected Output : "dcba4321" 
'''
def reverse(s):
    rs = ''
    index = len(s)
    while index > 0:
        rs += s[ index - 1 ]
        index = index - 1
    return rs
print(reverse('1234abcd'))
