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