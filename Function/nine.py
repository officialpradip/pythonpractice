'''9.	Write a Python function that takes a number as a parameter 
and check the	 number is prime or not. 
Note : A prime number (or a prime) is a natural number greater than
 1 and that has no positive divisors other than 1 and itself.  
'''
def prime(num):
    if (num==1):
        return False
    elif (num==2):
        return True;
    else:
        for x in range(2,num):
            if(num % x==0):
                return False
        return True             
print(prime(9))
print(prime(10))
print(prime(11))
