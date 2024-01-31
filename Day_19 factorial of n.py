#Day 19: Write a function to calculate the factorial of a number.
"""
Note:
0! and 1! are both 1

-python offers a direct function that can compute the factorial of a number without writing the whole code for computing factorial.


# Python code to demonstrate math.factorial()
import math
 
print("The factorial of 23 is : ", end="")
print(math.factorial(23))


-for i in range(1, n+1), that start from 1 but doesn't include n+1.

"""

def factorial(n):
    try:
        n = int(n)
        f = 1
        for i in range(1, n+1):
            f = f * i
        
        return(f)
    
    except:
        return('Please give me a positive integer and try again.')
    
n = input('please give me a number: ')
print(f'the factorial of {n} is : {factorial(n)}')
