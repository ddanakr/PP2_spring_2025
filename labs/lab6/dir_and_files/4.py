file_name = 'test.txt'

with open(file_name, 'r') as file:
    lines_list = list(file)


print('Length:', len(lines_list))