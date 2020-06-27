'''Write a Python program to multiply all the items in a dictionary.  '''
dict = {'num1':100,'num2':4,}
result=1
for key in dict:    
    result=result * dict[key]

print(result)
