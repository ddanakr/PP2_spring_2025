import random

num = random.randint(1, 20)
name = input("Hello! What is your name? ")

print("well,", name + ", I am thinking of a number between 1 and 20.")
cnt = 0
while True:
    guess = int(input(" Take a guess. "))

    if guess == num:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    elif guess > num:
        cnt += 1
        print("Your guess is too high.")
    elif guess < num:
        cnt += 1
        print("Your guess is too low.")