# Going over while loops

'''
i = 1
while i <= 5:
    print(i)
    i = i + 1
print('Done')
'''
'''
i = 1
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')
'''


# Guessing game

'''
secret = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret:
        print('you win!')
        break
else:
    print('you failed your 3 guesses')
'''

command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('car is already started')
        else:
            started = True
            print('the car has started')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = False
            print('the car stopped')
    elif command == 'help':
        print('start - to start the car\nstop - to stop the car\nquit - to exit')
    elif command == 'quit':
        break
    else:
        print('sorry i dont understand')
