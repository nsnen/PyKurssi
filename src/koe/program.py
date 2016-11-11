import random

print('--------------------------')
print('      guess NUMBER 2')
print('--------------------------')
print('')

the_num = random.randint(1, 20)
print('Python has chosen a number between 1 and 20.')

for guesses in range(1, 5):
    guess = int(input('take a guess: '))

    if guess < the_num:
        print('ur guess is too LOW.')
    elif guess > the_num:
        print('ur guess is too HIGH.')
    else:
        break

if guess == the_num:
    print('great, you found the right one in ' +  str(guesses) + ' guesses.')
else:
    print('sorry, the right number was ' + str(the_num))

print('')
print('the End.')