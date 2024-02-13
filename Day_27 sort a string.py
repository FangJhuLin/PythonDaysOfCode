#Day 27: Create a program that sorts a list of strings alphabetically.

def sorting_list(x):
    if len(x) == 0:
        return('You didn\'t put a string, try again')
    
    else:
        for i in x:
            i = i.lower()
        x.sort()
        return(x)

print('Please give me a string, seperate by space: \n')
x = input().split()
print(sorting_list(x))
