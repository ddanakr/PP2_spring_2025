import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

pattern = 'a.*b$'

result = re.match(pattern, text_to_match)

print(result)
