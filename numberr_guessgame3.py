import random

number = random.randint(1, 10)
guess = None

while True:
    guess = input('Guess the number: ')

    try:
        guess = int(guess)
    except:
        print('Sorry that is not a number, please input a number')
        continue

    if guess != number:
        if guess > number:
            print(guess, 'is greater than secret number')
        elif guess < number:
            print(guess, 'is smaller than secret number')
    else:
        print('You got the number, Champ! It is', number, '!')
        break
