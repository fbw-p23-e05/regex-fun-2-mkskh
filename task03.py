import re

# Write a Python program to search for literal strings within a string. Sample text : 'The quick brown fox jumps over the lazy dog.' Searched words : 'fox', 'dog', 'horse'


set_patterns = ['fox', 'dog', 'horse']
text = 'The quick brown fox jumps over the lazy dog.'

for pattern in set_patterns:
    print(f'Searching a word "{pattern}": ')
    if re.search(pattern, text):
        print(f'"{pattern}" exist in our text')
    else:
        print(f'"{pattern}" doesnt exist in our text')



# FIRST TRY

# pattern1 = 'fox'
# pattern2 = 'dog'
# pattern3 = 'horse'

# print(re.search(pattern1, 'The quick brown fox jumps over the lazy dog.'))
# print(re.search(pattern2, 'The quick brown fox jumps over the lazy dog.'))
# print(re.search(pattern3, 'The quick brown fox jumps over the lazy dog.'))