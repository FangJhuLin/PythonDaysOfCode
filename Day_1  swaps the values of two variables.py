#Create a program that swaps the values of two variables.
print("Enter two values, could be a string or number")
print("Enter the first value: ")
FIRST_VALUE = str(input())
print("Enter the second value: ")
SECOND_VALUE = str(input())

# Swap the values
FIRST_VALUE, SECOND_VALUE = SECOND_VALUE, FIRST_VALUE

# Display the values after swapping
print("After swapping: ", FIRST_VALUE, ",", SECOND_VALUE)
