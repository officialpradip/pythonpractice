'''20.	Write a Python program 
to find intersection of two given arrays using	 Lambda. '''

array1 = [1, 2, 3, 5, 8, 9]
array2 = [1, 2, 4, 8, 9]
print(array1)
print(array2)
intersection = list(filter(lambda x: x in array1, array2)) 
print ("\nIntersection of array1 and array2 are: ",intersection)
