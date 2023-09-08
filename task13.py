import re 

# Write a Python program to separate and print the numbers and their position in a given string.

text = '234, Words and words: 643, andOOOO End 435'

for number in re.finditer('\d+', text):
    print(number)