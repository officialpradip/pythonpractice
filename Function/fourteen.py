'''14.	Write a Python program to sort a list of dictionaries using Lambda.'''


bio = [{'name':'ram', 'age':67, 'address':'ktm'},
 {'name':'arpan', 'age':2, 'address':'bkt'},
  {'name':'shyam', 'age': 27, 'address':'pkr'}]
print(bio)
sorted_bio = sorted(bio, key = lambda x: x['age'])
print('sorted bio as per age is', sorted_bio)
