'''22.	Write a Python program to remove duplicates from a list.	  '''
a = [1,2,3,4,5,6,7,2,4,5,8,9,0,2,3,5,6,7,8]
duplicates = set()
orginal = []
for x in a:
    if x not in duplicates:
        orginal.append(x)
        duplicates.add(x)
print(duplicates)
