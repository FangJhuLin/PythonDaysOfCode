#Day 2: Create a program to calculate the area of a circle given its radius.

import math
print("please imput a radius:")

#data type of an input value is default as string, but pi is a float, so coercion it to float.
r = float(input())

# calculate the area and round up to two decimal places.
area =round(math.pi * r**2, 2)

print('the area is:', area)
