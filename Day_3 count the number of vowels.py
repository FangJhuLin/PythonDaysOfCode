#Day 3: Write a function to count the number of vowels in a given string 

a = input('give me a word:')

def count_vowels(string):
	vowels = ['a', 'e', 'i', 'o', 'u']
	return sum([1 for char in string if char.lower() in vowels])
print(count_vowels(a))
