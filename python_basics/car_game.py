started = False
stopped = False
while True:
    command = input('>').lower()    
    if command == 'help':
        print('start - to start the car ')
        print('stop - to stop the car ')
        print('quit - to exit')

    elif command == 'start':
        if started:
            print('Car is already started')
            continue
        print('Car started , Let"s go')
        started = True
        stopped = False
        
    elif command == 'stop':
        if stopped:
            print('Car is already stopped')
            continue
        print('car stopped')
        stopped = True
        started = False

    elif command == 'quit':
        print('Thanks for playing')
        break

    else :
        print('I didn"t get that , type "help" to know more')

