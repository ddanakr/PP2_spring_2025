is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, x - 1))

nums = [1,2,3,4,5,6,7,8,9]

prime_nums = list(filter(is_prime, nums))
print(prime_nums)