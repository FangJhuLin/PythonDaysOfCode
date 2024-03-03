# Day42: Write a program that uses a try-except block to handle division by zero.

def devision(a, b):
    
    try:
        a = int(a)
        b = int(b)
        return a/b
    
    except:
        return('Divisor can\'t be zero. Please input numbers')
        

a = input('Enter the dividend: \n')
b = input('Enter the divisor: \n')

print(devision(a, b))
