#Day 38: Write a program to flatten a nested list.
#[[1,2,3,4,5],[6,7,8,9,10],[20],21, 22, [11,[23, [24]]]]

"""
Note: I accidentally completed it by making flatten_list = [] a local variable, but I am not sure if I understand why.
"""

list_o = [[1,2,3,4,5],[6,7,8,9,10],[20],21, 22, [11,[23, [24]]]]

def flatten(list_o):
    flatten_list = []   

    for ele in list_o:
            
        if isinstance(ele, list):
            flatten_list.extend(flatten(ele))
   
        else:
            flatten_list.append(ele)
    return flatten_list     
    
    
print(flatten(list_o))
