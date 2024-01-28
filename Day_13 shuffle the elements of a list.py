#Day 13: Write a program to shuffle the elements of a list randomly.
"""
use python built function random.shuffle(x)
in Chinese: https://docs.python.org/zh-tw/3/library/random.html
in English: https://docs.python.org/3/library/random.html#random.shuffle
"""
import random

def shuffle_input_list():
    
    input_string = input('Please give me a list, and split by space: ')
    input_list = input_string.split()
    random.shuffle(input_list)
    
    return input_list

shuffled_list = shuffle_input_list()
print(shuffled_list)

"""
Note:
list_1r = random.shuffle(list_1), this will only return "None"

I learned how to define function today, I did wrong in my previous challenges, I might go back to check it later.
I should also put ".py" in the name.
"""
