def num_gen(num):
    for i in range(num, -1, -1):
        yield i


num = int(input())

print(*num_gen(num))

