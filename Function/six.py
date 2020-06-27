'''Write a Python function to check whether a number is in a given range. '''
def test_range(num):
    if num in range(1,5):
        print(f" {num} is in the range")
    else :
        print(f"{num} is Not in given range.")
test_range(2)
test_range(22)
