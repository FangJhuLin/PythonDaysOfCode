#Day 21: Create a program to remove a specific element from a set.

"""
Note:
-different between discard() and remove():
remove() will return an error when the element doesn't exist, but discard() will not.
        
-set_a = set_a.remove(x) this will return 'None', because remove() doesn't has a return value.
-numbers in the set is consider as a int, float, not string. Transform it into String and python can recognize it.


question:
allow user to input a set?
"""

def remove_ele(x):

    set_a = {1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    print("here is a set:\n", set_a)
    
    
    try: 
        x = int(x)
        if x in set_a:
            set_a.remove(x)
            return(f'the set after remove \'{x}\' is:\n{set_a}')
        else:
            return(f'The element \'{x}\'is not in this set, or already removed, please try again.')
        
    except:
        if x in set_a:
            set_a.remove(x)
            
            return(f'the set after remove \'{x}\' is:\n{set_a}')
            
        else:
            return(f'The element \'{x}\'is not in this set, or already removed, please try again.')
        
        
x = input('please tell me the element that you want to remove from this set: ')
print(remove_ele(x))
