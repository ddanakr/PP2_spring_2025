import string

letters = list(string.ascii_uppercase)

for letter in letters:
    file_name = f"{letter}.txt"

    with open(file_name, 'x') as file:
        pass
