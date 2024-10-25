import random

random_number = random.randint(1,3)
guess = ""
while guess != random_number:
    guess = int(input('guess: '))
    if guess == random_number:
        print('you got it!')
    else:
        print('try again!')