import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

pattern = '[A-Z][a-z]+'

result = re.findall(pattern, text_to_match)

print(result)
