import re

url = 'http://example.com/users/12345/bids?start=01-31-2012&end='
date = re.findall('\d{2}\-\d{2}\-\d{4}', url)

print(date)


