'''30.	Write a Python script to check whether a given key 
already exists in a	 dictionary. '''
d = {1: 0, 2: 20, 3: 90, 4: 4, 5: 50, 11: 66}
def is_key(x):
  if x in d:
      print('Key is already exists in a	 dictionary ')
  else:
      print('Key is not exists in a	 dictionary')
is_key(11)
is_key(0)
