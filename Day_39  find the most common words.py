#Day 39: Write a program to find the most common words in a text file.

"""
- | means "or" to combine more than one condition in the regular expression.
-I use "Alice's Adventures in Wonderland" as my text file. This is where I get the text from: 
 https://www.gutenberg.org/ebooks/11

Thoughts:
    1. remove punctuation.
    2. remove all the punctuation: ",", ".", "()"...
    3. make every word lowercase.
    4. prepare an empty dictionary.
    5. check if the word already exists in the dictionary.
    6. if not, add to the dictionary and set the value as 1.
    7. if the word already existed, add 1 to the value.
    8. print the top 10 from the dictionary.
   
"""
import re

def common_words():
    with open('Alice\'s Adventures in Wonderland.txt', 'r') as file:
        
        content = file.read()
        content = content.lower()
        content = re.sub(r'[^\w\s\']|[_]', '', content)
        content = content.split()
    
    frequency = {}
    
    for word in content:
        if word not in frequency:
            frequency[word] = 1
        
        elif word in frequency:
            frequency[word] += 1
            
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:20]
    for word, time in sorted_frequency:
       print (f"{word}: {time} times")
    
common_words()
