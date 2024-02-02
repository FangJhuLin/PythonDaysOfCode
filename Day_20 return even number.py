#Day 20: Write a function that takes a list of numbers and returns a new list containing only the even numbers.


def return_even(x):
    even = []
    x = x.split()
    for i in x:
        try:
            i = float(i)
            if i % 2 == 0:
                even.append(int(i))
        except:
            return('please input numbers and try again.')
    return even
        

x = input('please give me a number of list, seperate by space: ')
print(return_even(x))
        
