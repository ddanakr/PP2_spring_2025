str = input("string: ")

str = str.lower()

str_reversed = str[::-1]

if str == str_reversed:
    print("palindrome")
else:
    print("not a polindrome")