#Day 16: Write a function that counts the frequency of each word in a sentence.


"""
thoughts:
    1. input sentence.
    2. remove all the punctuation: ",", ".", "()"...
    3. make every word lower case.
    4. prepare an empty dictionary.
    5. check if word already exist in dictionary.
    6. if not, add to dictionary and set value as 1.
    7. if word already existed, add 1 to the value.
    
    想法：分割字串、去除標點符號、全部小寫、如果有在字典裡，值加一。沒有的話就新增進字典，把值記為一。
    
important:
The split() function returns the strings as a list.
lower() method returns the lowercase string.
replace() is method of string, not list.
Therefore, if we split the sentence first, we get a list, then lower() and split() won't work.


Question: I don't know what to do with "isn't, doesn't, didn't..." yet, these type of words is splited.
"""
import string

def frequent_count(sentence):
    frequency = {}
    
    puncuation = string.punctuation
    for ele in sentence:
        if ele in puncuation:
            sentence = sentence.replace(ele, " ")
    sentence = sentence.lower().split()
    
    for word in sentence:
        if word not in frequency:
            frequency[word] = 1
            
        elif word in frequency:
            frequency[word] += 1
    
    return frequency

sentence = input('please give me a sentence or paragraph: ')
print(frequent_count(sentence))
