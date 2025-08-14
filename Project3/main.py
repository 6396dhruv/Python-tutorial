# password guessing game

import random

easy = ["apple", "mango", "india", "tiger", "train"]
medium = ["dhruv", "python", "bottle", "planet", "laptop"]
hard = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Welcome to the password guessing game ")
print("Choose your difficulty level: easy medium and hard ")

level = input("Enter your difficulty: ").lower()

if level == "easy":
    secret = random.choice(easy)
elif level == "medium":
    secret = random.choice(medium)
elif level == "hard":
    secret = random.choice(hard)
else:
    print("Invalid choice! You are attending easy level")
    secret = random.choice(easy)

attemps =0

while True:
    guess = input("Enter your guess: ").lower()
    attemps += 1

    if guess == secret:
        print(f"Congratulations :) You guessed it in {attemps} attempts. ")
        break

    hint = ""

    for i in range(len(secret)):
        if i<len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
        
    print("Hint: ", hint)
print("Game Over! ")



