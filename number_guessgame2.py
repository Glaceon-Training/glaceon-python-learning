import random

number = random.randint(1, 10)

guess = input('Guess the number: ')
guess = int(guess)

if guess == number:
    print('You got it, man!')
else:
    print('Try again!')
