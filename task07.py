import re

text = 'The quick brown fox jumps over the lazy dog'
place = ' '
replace = '_'

print(re.sub(place, replace, text))