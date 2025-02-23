import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

pattern = '^ab{2,3}$'

result = re.match(pattern, text_to_match)

print(result)


test_strings = ["a", "ab", "abb", "abbb", "b", "ba", "aab"]
for test in test_strings:
    result2 = re.match(pattern, test)
    print(f"String: '{test}' matches: {result2}")