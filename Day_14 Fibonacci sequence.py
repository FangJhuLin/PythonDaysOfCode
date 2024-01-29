#Day 14: Write a program to print the first n numbers of a Fibonacci sequence.

"""
Notes: 
-Mathematically, Fibonacci sequence is defined as: F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1 (the seeds)

-0, 1, 1, 2, 3, 5, 8, 13, ......(Fibonacci sequence)
-1, 2, 3, 4, 5, 6, 7, 8 ........(index)

-n has to be 0 or more and n has to be an integer.

"""

def fibonacci (n):
    n = abs(n)
    list_f =[0]
    # there is no negative in Fibonacci sequence, if the user put a negative number, turn it into positive.
    if n <= 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    else:
        a = 0
        b = 1
        for i in range(1, n):
            a, b = b, a+b
            list_f.append(a)
        return list_f
    

n = int(input('I am going to print the first n numbers of a Fibonacci sequence. Give me a n: '))

print(fibonacci(n))
