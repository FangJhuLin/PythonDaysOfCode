#Day 36: Write a Python program to check if two strings are anagrams.


"""
Thoughts:
-Make all the letter into lower case.
-Compare the two strings to see if they are equal.
"""

def anagrams(a, b):
    if len(a) == len(b):  
        a_lower = sorted(a.lower())
        b_lower = sorted(b.lower())            
        if a_lower == b_lower:
            return('These two strings are anagrams.')
        else:
            return('These two strings are NOT anagrams.')
    else:
        return('These two strings are NOT anagrams.')

        
a = input('please give me word 1: ')
b = input('please give me word 2: ')
print(anagrams(a, b))
