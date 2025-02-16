def num_gen(num):
    for i in range(num + 1):
        if i % 12 == 0:
            yield i


num = int(input())

print(*num_gen(num))

