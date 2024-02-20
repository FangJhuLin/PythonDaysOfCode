#Day 37: Write a program to iterate through a dictionary and print its keys and values.


def print_dict():
    Countries = {
    "Afghanistan" : "Kabul",
    "Albania" : "Tirana",
    "Algeria" : "Algiers",
    "Andorra" : "Andorra la Vella",
    "Angola" : "Luanda",
    "Antigua and Barbuda" : "Saint John’s",
    "Argentina" : "Buenos Aires",
    "Armenia" : "Yerevan",
    "Australia" : "Canberra",
    "Austria" : "Vienna",
    "Azerbaijan" : "Baku"}
    
    result = ""
    for key, value in Countries.items():
        result += f'{key}: {value}\n'
    
    return result


print(print_dict())
