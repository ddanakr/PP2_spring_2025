import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

pattern = '[ ,.]'

result = re.sub(pattern, ":", text_to_match)

print(result)

