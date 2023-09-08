import re

# Write a Python program to replace maximum 2 occurrences of space, comma, or dot with a colon.


text = '234, Words, Road   (3spaces)and words: 643      (6spaces)andOOOO End 435.'

print(re.sub('(\s{1,2}|\.|,)+', ':', text))