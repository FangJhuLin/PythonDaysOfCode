#Day 22: Create a program to find the second-largest element in a list.


"""
Thought:
Sort the input list and print list[-2]    
    

Note: 
* Difference between list.sort() and sorted(list)
x = [1, 2, 100, 5, 3, 4, 5]

x = x.sort() 
# return None, simply use x.sort() will sort the list in place.

x = sorted(x) 
#return sorted x
    
* in the function x = [float(i) for i in x] transfer elements into float, but outside of the function, it's still a string, if I want this to be float, x = [float(i) for i in x] has to be outside of the function'
    
Question:
How do I keep integer as an integer (not a float) for output?    
"""

def Second_largest(x):
    x = [float(i) for i in x]  
    x = sorted(x)
        
    return(x[-2])


x = input('please give me a list of numbers, seperate by space: ').split()
 
print('The the second largest number is: ', Second_largest(x))
