list1 = list(i for i in input().split())
new_list = []

for elem in list1:
    if not elem in new_list:
        new_list.append(elem)

print(new_list)