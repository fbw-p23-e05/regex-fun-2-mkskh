import re

# Write a Python program to abbreviate 'Road' as 'Rd.' in a given string.

text = '234, Words, Road and words: 643, andOOOO End 435'

print(re.sub('Road', 'Rd', text))

