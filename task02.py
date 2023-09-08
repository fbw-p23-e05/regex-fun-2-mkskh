import re

# Write a Python program to search for numbers (0-9) of length between 1 and 3 in the given string.
# "Exercises number 1, 12, 13, and 345 are important"


pattern = '\d{1,3}'

print(re.findall(pattern, "Exercises number 1, 12, 13, and 345 are important"))
