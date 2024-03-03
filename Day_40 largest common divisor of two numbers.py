#Day 40: Write a function to find the largest common divisor of two numbers using a function.

"""
Note:
    -0 is a multiple of any integer. 0是任何整數的倍數。
    -1 and -1 are factors of any integer. 1和-1是任何數的因數。
"""

def gcd(a, b):
    if a == 0:
        return(f'The GCD of {a} and {b} is {b}.')
    
    elif b == 0:
        return(f'The GCD of {a} and {b} is {a}.')
    
    elif a == 1 or b == 1:
        return(f'The GCD of {a} and {b} is 1.')
    
    elif a == b:
        return (f'The GCD of {a} and {b} is {a}.')
    
    else:
        for i in range(a, 0, -1):
            if a % i == 0 and b % i == 0:
                return (f'The GCD of {a} and {b} is {i}.')

a = int(input('Please give me the first number: '))
b = int(input('Please give me the second number: '))

print(gcd(a, b))
