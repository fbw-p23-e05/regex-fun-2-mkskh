import re

# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

date = '2012-01-31'
new_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date)

print(new_date)

