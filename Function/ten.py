'''10.	Write a Python program to print the even numbers from a given list.	  
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]  
Expected Result : [2, 4, 6, 8] 
'''
def even_num(l):
    num = []
    for n in l:
        if n % 2 == 0:
            num.append(n)
    return num
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))
