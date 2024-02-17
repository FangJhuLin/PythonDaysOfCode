#Day 33: Write a test case for a function that checks if a number is prime.

"""
Question: I don't know how to make a test case yet, I might come back later for it.
I only make a function to test if it's a prime number. 
"""

def prime_or_not(x): 
    if x.isdigit():  
        x = int(x)
        if x < 2:
            return(f'{x} is not a prime number.')
            
        elif x % 2 == 0:
            return(f'{x} is not a prime number. It has a factor 2.')
        
        else:
            x_square_root = int(x ** 0.5)
            for i in range(2, x_square_root+1):
                if x % i == 0:
                    return(f'{x} is not a prime number. It has at least a factor {i}.')
                    break
            else:
                return(f'{x} is a prime number.')
    
    
    else: 
        return(f'{x} is not an integer, try again.')
        
x = input('Please give me a number: ')
print(prime_or_not(x))
