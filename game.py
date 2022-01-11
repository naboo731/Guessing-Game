"""A number-guessing game."""

from random import randint

attempts = 0
number = randint(1, 100)

print('Hello and welcome to the Number Guessing Game!')
print('What is your name?')

name = input('(type your name)')

print(f'{name}, Im thinking of a number 1 to 100')
print('Can you guess the number?')

while True:
    guess = input('type your guess')

    try:
        guess = int(guess)
    except ValueError:
        print(f'"{guess}" is not a valid number. Please try again')
        continue
    if guess < 1 and guess > 100:
        print('Please enter a number between 1 and 100')
        continue

    attempts += 1

    if guess < number:
        print('Your guess is too low. Try again.')
        continue
    elif guess > number:
        print('Your guess is too high. Try again.')
    else:
        print(f'{guess} is right! Well done, {name}')
        print(f'You were able to guess the number in {attempts} attempts!')
