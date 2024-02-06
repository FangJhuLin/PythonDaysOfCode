#Day 25: Create a program to concatenate two lists.

"""
Note:
I set a default for both list incase the user doesn't give any input.
"""

def concatenate_lists(list1, list2):
    if list1 == []:
        list1 = ['I', 'love', 'you']
    if list2 == []:
        list2 = ['Me', 'too']
    
    concatenate_list = list1 + list2
    return(concatenate_list)


list1 = input('please give me the FIRST list,\n (default is [\'I\', \'love\', \'you\'] if not receiving any value.)\n use space to seperate items, : \n ').split()


list2 = input('please give me the SECOND list,\n (default is [\'Me\', \'too\'] if not receiving any value.)\n use space to seperate items, : \n ').split()

print(concatenate_lists(list1, list2))
