#Day 26: Create a program that uses a lambda function to square each element of a list.
"""
Question: I tried to set the list numbers to float, but I will receive several numbers after the decimal point, I don't know how to improve it yet.
不知道是不是要視為浮點數或是整數，若是浮點數，就會有很多小數。
"""
def sequare(numbers):
    func = lambda x: x**2
    return[func(x) for x in numbers]

numbers = input('please give me a numbers list, seperated by space: ').split()
numbers = [int(x) for x in numbers]
print(sequare(numbers))
