import re

# Write a Python program to check for a number at the end of a string.


pattern = '\d$'

print(re.search(pattern, 'Some text about nothing number 1')) #Match
print(re.search(pattern, 'Some text about nothing number one'))