import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()



camel_case = re.sub('_([a-z])', lambda x: x.group(1).upper(), text_to_match)


print(camel_case)

