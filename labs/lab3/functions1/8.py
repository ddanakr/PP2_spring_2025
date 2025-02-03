def spy_game(nums):
    seq = [0, 0, 7]
    ind = 0

    for num in nums:
        if num == seq[ind]:
            ind += 1
        if ind == len(seq):
            return True
    
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))