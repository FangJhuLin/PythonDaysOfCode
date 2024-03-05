#Day 45: Write a function to check if a number is a prime number.
"""
Day 33 is a similiar task to this.
"""

def prime(x):
    try:
        x = int(x)
        
        if x <= 1:
            return'A prime number must be greater than 2'
        elif x ==2:
            return'2 is a prime number.'
        
        else:
            x_square = round(x ** 1/2)
            
            for i in range(2, x_square + 1):
                if x%i == 0:
                    return f'{x} is not a prime number.'
                else:
                    return f'{x} is a prime number.'
                
                
    except:
        return 'Please input an integer.'
    
x = input('Please give me an integer:\n')
print(prime(x))
