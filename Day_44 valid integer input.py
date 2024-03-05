#Day 44: Write a program that reads an integer from the user and handles invalid inputs.

def check_int(x):
    try: 
        x = int(x)
        return "This is an integer"
    except:
        return f'{x} is not an integer, please try again.'
    

x = input('type something here: ')
print(check_int(x))
