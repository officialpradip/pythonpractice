'''Write a Python function to find the Max of three numbers. '''
def max_two( num1, num2 ):
    if num1 > num2:
        return num1
    return num2
def max_three( num1, num2, num3):
    return max_two( num1, max_two( num2, num3 ) )
print(max_three(1, 2, 3))
