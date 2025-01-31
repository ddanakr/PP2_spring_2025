def filter_prime(nums):
    prime_nums = []
   
    for n in nums:
        is_prime = True
        num = int(n)
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_nums.append(num)

    return prime_nums


nums = [int(x) for x in input("Numbers: ").split()]
print(filter_prime(nums))