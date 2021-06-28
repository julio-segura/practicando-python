import random

guessesTaken = 0

number = random.randint(1, 50)
print("I am thinking a number between 1 and 50")

while guessesTaken < 6:
    print("Take a guess.")
    guess = input()
    guess = int(guess)
    
    guessesTaken = guessesTaken + 1
    
    if guess < number:
        print("You guess is too low.")
        
    if guess > number:
        print("Your guess is too high.")
        
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print(f"Good job, you guessed my number in {guessesTaken} guesses!")
    
if guess != number:
    number = str(number)
    print(f"Nope. I was thinking of {number}.")

