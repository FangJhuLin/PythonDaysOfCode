#Day 17: Create a program that capitalizes the first letter of each word in a sentence.

"""
Note:
    
-str.capitalize()
Return a copy of the string with its first character capitalized and the rest lowercased.

-str.title()
Make the first letter in each word upper case.
"""
import re

def cap(x):
    x = x.title()
    return(f'this is your output:\n{x}')

x = input('please give me a sentence or string: ')
print(cap(x))
