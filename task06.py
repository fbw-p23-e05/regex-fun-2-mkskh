import re

# Write a Python program to find the occurrence and position of substrings within a string.


match = re.search('over', 'The quick brown fox jumps over the lazy dog')
start = match.start()
end = match.end()

print(match)
print(f'The word "over" is in place from {start} to {end}')