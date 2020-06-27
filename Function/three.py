'''Write a Python function to multiply all the numbers in a list.  
Sample List : (8, 2, 3, -1, 7) 
Expected Output : -336  
'''
def multiply(myList) : 
	result = 1
	for x in myList: 
		result = result * x 
	return result 
	
list1 = [8, 2, 3, -1, 7] 
print(multiply(list1)) 

