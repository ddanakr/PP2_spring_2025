import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

s = "HelloWorldAndDana"

snake_case = re.sub('([a-z])([A-Z])', r'\1_\2', s)
snake_case = snake_case.lower()

print(snake_case)
