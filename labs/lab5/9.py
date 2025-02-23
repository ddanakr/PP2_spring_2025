import re

'''
with open('row.txt', 'r') as file:
    text_to_match = file.read()
'''


s = "HelloWorldAndDana"

result = re.sub('([a-z])([A-Z])', r'\1 \2', s)


print(result)

