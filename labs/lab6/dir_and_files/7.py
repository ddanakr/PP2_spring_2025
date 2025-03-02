file1_name = "test.txt"
file2_name = "new.txt"

with open(file1_name, 'r') as file1, open(file2_name, 'w') as file2:
    file2.write(file1.read())