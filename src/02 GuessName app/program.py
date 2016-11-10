import random

print('----------------------------')
print('       Guess the NUMBER')
print('----------------------------')
print('')

num = random.randint(0, 100)
guess = -1
name = input('Hello, what is your name? ')

while guess != num:
    guess0 = input('Pick a number between 0 and 100: ')
    guess = int(guess0)

    if guess > num:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    elif guess < num:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    else:
        print('Yey {}, you got it right!'.format(name))
print('')
print('The end')