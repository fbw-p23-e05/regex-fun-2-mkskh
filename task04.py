import re

# Write a Python program to search for a literal string in a string and also find the location within the original string where the pattern occurs.


match = re.search('fox', 'The quick brown fox jumps over the lazy dog')
start = match.start()
end = match.end()

print(match)
print(f'The word "fox" is in place from {start} to {end}')