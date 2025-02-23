import re

with open('row.txt', 'r') as file:
    text_to_match = file.read()

pattern = '[a-z]+(?:_[a-z]+)*'

result = re.fullmatch(pattern, text_to_match)

print(result)



test_strings = ["this_is_a_test_string",  # valid sequence
    "hello_world", "a_b_c_d", "abc_123_test", "_underscore", "anotherExample"]
for test in test_strings:
    result2 = re.fullmatch(pattern, test)
    print(f"String: '{test}' matches: {result2}")
