#Day 24: Write a program to remove vowels from a given string.


def remove_vowels(x):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    removed = ""
    for char in x:
        if char.lower() not in vowels:
            removed = removed + char
    return(removed)


x = input('Please give me a string: ')
print(remove_vowels(x))
