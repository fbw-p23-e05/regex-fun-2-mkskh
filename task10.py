import re

#Write a Python program to match if two words from a list of words start with the letter 'P'. 

list = ['Peter', 'Max', 'Pavel', 'Mike', 'Polly']
pattern = '^P'
matched = []

for word in list:
    if re.match(pattern, word):
        matched.append(word)

quantity_in_matched = len(matched)

if quantity_in_matched >= 2:
    print("At least 2 words in the list of words start with the letter 'P'")
else:
    print("Less than 2 words in the list of words start with the letter 'P")






    # if re.match(pattern, word):
    #     print('For word', word + ': Matched! First letter is not "P". Details:', re.match(pattern, word))
    # else:
    #     print('For word', word + ': Does not match. First letter is not "P"')