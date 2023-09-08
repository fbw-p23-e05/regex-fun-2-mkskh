import re

# Write a Python program to separate and print the numbers in a given string.

print(re.split(' ', '12 34 567 89'))

print(re.split('\D+', '234, Words and words: 643, and Word 435'))