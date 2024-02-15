#Day 30: Create a function that finds the second smallest element in a list.

"""
Question: I want to learn how it's sorted if the input isn't numbers but strings.
"""

def second_smallest(x):
    
    if len(x) < 2:
        return 'List should have at least two elements, try again.'
    else:
        for ele in x:
            x = [int(ele) for ele in x]
            x.sort()
            second = x[1]
            return second

x = input('Please give me a list, seperate each item by space: ').split()
print(second_smallest(x))
