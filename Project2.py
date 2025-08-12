# The Perfect Guess

from random import randint
n = randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input('Guess A Number: '))
    if(a == n):
        break
    if(a > n):
        print("Lower Number Please")
    else:
        print("Higher Number Please")

print(f"You have guessed the number correctly in {guesses} attempt")








