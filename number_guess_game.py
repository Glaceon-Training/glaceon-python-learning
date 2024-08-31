import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = input('Guess the number: ')
    guess = int(guess)

    if guess == number:
        print('You got the number!')
        break
    else:
        print('Ha! Try it again, dude!')
