"""A number-guessing game."""

from random import randint

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
    if
