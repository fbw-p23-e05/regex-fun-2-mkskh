import re

# Write a Python program to replace whitespaces with an underscore and vice versa.

text = 'The quick brown fox jumps over the lazy dog'
place = ' '
replace = '_'

print(re.sub(place, replace, text))