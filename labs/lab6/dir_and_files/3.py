import os

path = input("Enter the path: ")

if os.access(path, os.F_OK):
    print("Path exists")

    dir = os.path.dirname(path)
    filename = os.path.basename(path)

    print(f"Directory: {dir}")
    print(f"Filename: {filename}")

else:
    print("Path does not exist")