#Day 46: Write a function to check if a given list is sorted.

def check_sorted(lst):
    
    if len(lst) <= 2:
        return 'This list is too short, please provide at least 3 items.'
        
    elif lst == sorted(lst) or lst == sorted(lst, reverse = True):
        return 'Your input is already a sorted list.' 
       
    else:
        return 'Your input is NOT a sorted list.'  

lst = input('Please give me a list, seperate each item by space:\n').split()
print(check_sorted(lst))
