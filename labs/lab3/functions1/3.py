def solve(numheads, numlegs):
    rabbits = numlegs / 2 - numheads
    chickens = numheads - rabbits

    print("Number of chickens:", chickens)
    print("Number of rabbits:", rabbits)

numheads = int(input("Number of heads: "))
numlegs = int(input("Number of legs: "))

solve(numheads, numlegs)

