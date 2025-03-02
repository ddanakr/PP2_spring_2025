import os

path = input("Enter the path: ")

print("only directories:")

print([dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path,dir))])

print("---------")
print("only files:")

print([file for file in os.listdir(path) if os.path.isfile(os.path.join(path,file))])

print("----------")
print("both files and directories:")

print(os.listdir(path))