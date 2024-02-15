#Day 29: Create a function that generates a random number between a given range.

import random

def random_number(high, low):
    if high == low:
        return(high)
    elif high > low:
        return(random.randint(low, high))
    
    else:
        return(random.randint(high, low))
        

high = int(input('Please enter starting range: '))
low = int(input('please enter ending range: '))
print(random_number(high, low))
