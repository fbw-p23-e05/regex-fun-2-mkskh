import re

pattern = '\d{1,3}'

print(re.findall(pattern, "Exercises number 1, 12, 13, and 345 are important"))
