#Day 47: Create a program that imports the math module and uses its functions.

from math import gcd

def find_gcd(x, y):
    x = abs(int(x))
    y = abs(int(y))
    
    return f'The GCD is: {gcd(x, y)}'


x = input('Please give me an integer:\n')
y = input('Please give me another integer:\n')
print(find_gcd(x, y))
