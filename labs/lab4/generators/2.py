def num_gen(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

num = int(input())

print(*num_gen(num), sep=', ')