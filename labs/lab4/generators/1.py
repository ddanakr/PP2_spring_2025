a = 1

def func(num):
    result = []
    global a

    while a <= num:
        result.append(a**2)
        a += 1
    
    return result

print(func(10))
    

