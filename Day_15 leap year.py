#Day 15: Create a program that checks if a year is a leap year.

"""
Notes: 
-Wiki pedia: Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. 

-For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are
"""

def leap_year(n):
    if n % 400 == 0:
        return(f'{n} is a leap year.')
    elif n % 4 == 0 and n % 100 != 0 :
        return(f'{n} is a leap year.')
    else:
        return(f'{n} is not a leap year.')
    

n = abs(int(input('let\'s check if it is a leap year, please input a number:')))

print(leap_year(n))
