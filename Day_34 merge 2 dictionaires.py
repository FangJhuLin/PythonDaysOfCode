#Day 34: Write a Python program to merge two dictionaries.

"""
Note: dict.update() return will return None.
"""
def dictionary_merge(dict1, dict2):
    dict1.update(dict2)
    
    return dict1
    


dict1 = {'Germany': 'Berlin', 'Canada': 'Ottawa', 'England': 'London'}
dict2 = {'Japan': 'Tokyo', 'Australia': 'Canberra', 'France': 'Paris'}
print(dictionary_merge(dict1, dict2))
