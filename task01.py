import re

pattern = '\d$'

print(re.search(pattern, 'Some text about nothing number 1')) #Match
print(re.search(pattern, 'Some text about nothing number one'))