# Day43: Write a program that removes all whitespaces from a given string.

def removeString(string):
    string = string.replace(" ", "")
    return (f'This is your result:\n{string}')

string = input('please give me a string with spaces:\n')
print(removeString(string))
