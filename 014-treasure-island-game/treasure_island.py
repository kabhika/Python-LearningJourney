# Treasure Island - A Text Adventure Game
# Date: January 2025

print('Welcome to the treasure hunt game')
print('Should you choose to play, you need to input one of the following to get started')
print()

choice = input('Enter your choice left/right: ')

if choice == 'right':
    print('Fall into a hole. Game Over!!')
elif choice == 'left':
    print('Good choice, now enter what you will do next.')
    choice = input('Enter your choice swim/wait: ')
    
    if choice == 'swim':
        print('Attacked by trout. Game Over!!')
    elif choice == 'wait':
        print('Good choice, now enter what you will do next.')
        choice = input('Enter your choice red/blue/yellow: ')
        
        if choice == 'red':
            print('Burned by fire. Game Over!!')
        elif choice == 'blue':
            print('Eaten by beasts. Game Over!!')
        elif choice == 'yellow':
            print('You WIN!!')
        else:
            print('Invalid choice. Game Over!!')
    else:
        print('Invalid choice. Game Over!!')
else:
    print('Invalid choice. Game Over!!')
