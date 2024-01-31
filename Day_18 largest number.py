#Day 18: Create a program to find the largest among three numbers.

def max_n(x):
    x_max = max(x)
    
    return(f'the largest number is {x_max}')

x = input('please give me 3 numbers, seperate with space: ').split()
print(max_n(x)) 
