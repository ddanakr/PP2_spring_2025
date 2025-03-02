str = input("Enter a string")

upper_cnt = sum(1 for letter in str if letter.isupper())
lower_cnt = sum(1 for letter in str if letter.islower())


print(f"Number of uppercase letters: {upper_cnt}, number of lowercase letters: {lower_cnt}")