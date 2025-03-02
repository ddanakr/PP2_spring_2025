import os

path = input("Enter the path to check: ")


if os.access(path, os.F_OK):

    print("Path exists")
    print("------------------")

    if os.access(path, os.R_OK):
        print("Path is readable")
    else:
        print("Path is not readable")

    print("------------------")


    if os.access(path, os.W_OK):
        print("Path is writable")
    else:
        print("Path is not writable")

    print("------------------")

    
    if os.access(path, os.X_OK):
        print("Path is executable")
    else:
        print("Path is not executable")

else:
    print("Path does not exist")