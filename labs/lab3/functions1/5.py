from itertools import permutations

str = input()
perm = permutations(str)

for i in list(perm):
    print(i)