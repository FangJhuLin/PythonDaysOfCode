#Day 28: Create a program that removes the nth element from a list.

def remove_nth_element(n):
    
    if n <= len(list_l):
        nth_element = list_l[n-1]
        list_l.pop(n-1)
        return(f'the element removed is {nth_element}, the new list is {list_l}')

    else: 
        return(f'The list does not has the {n}th element, try again')
    
list_l = input('please give me a list, seperate each item by space: ').split()
n = int(input('Which element do you want to remove? '))
print(remove_nth_element(n))
