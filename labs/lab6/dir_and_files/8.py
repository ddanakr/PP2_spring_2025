import os

path = input("Enter the path to file: ")

if os.access(path, os.F_OK):

    os.remove(path)

else:
    print("Path does not exist")