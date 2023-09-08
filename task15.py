import re

# Write a Python program to replace all occurrences of a space, comma, or dot with a colon.


text = '234, Words, Road and words: 643, andOOOO End 435.'

print(re.sub('[\., ]', ':', text))