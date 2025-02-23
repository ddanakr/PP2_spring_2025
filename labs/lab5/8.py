import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

s = "HelloWorldAndDana"

result = re.split('(?=[A-Z])', s)
result = [word for word in result if word]

print(result)

