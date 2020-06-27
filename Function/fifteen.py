'''15.	Write a Python program to filter a list of integers using Lambda.	  '''


nums = [1, 2, 3, 4, 5]
print(nums)
print("\nEven number:")
even = list(filter(lambda x: x%2 == 0, nums))
print(even)

print("\nOdd number:")
odd = list(filter(lambda x: x%2 != 0, nums))
print(odd)
