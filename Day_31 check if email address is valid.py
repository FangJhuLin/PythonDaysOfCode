#Day 31: Create a program that checks if a given string is a valid email address.

import re

pattern = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
user_id = input('enter an email id to check: ')

if re.search(pattern, user_id):
    print('This is a valid email id.')
    
else:
    print('This is an invalid email id.')
