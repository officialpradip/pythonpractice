'''16.	Write a Python program to sum all the items in a list.'''

def sum(lists):
    numbers = 0
    for x in lists:
        numbers += x
    return numbers
print(sum([1,2,3,4]))


