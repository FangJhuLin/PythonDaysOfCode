#Day 32: Create a function that calculates the average of a list of numbers.
def average_of_list(lst):
    float_lst = [float(ele) for ele in lst]
    
    avg = sum(float_lst)/ len(float_lst)
    
    return(avg)

lst = input('please give me a list of numbers, seperte each item by space: ').split()
print(average_of_list(lst))
