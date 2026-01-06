# # Treasure Island - A Text Adventure Game
# # Date: January 2025

# print('Welcome to the treasure hunt game')
# print('Should you choose to play, you need to input one of the following to get started')
# print()

# choice = input('Enter your choice left/right: ')

# if choice == 'right':
#     print('Fall into a hole. Game Over!!')
# elif choice == 'left':
#     print('Good choice, now enter what you will do next.')
#     choice = input('Enter your choice swim/wait: ')
    
#     if choice == 'swim':
#         print('Attacked by trout. Game Over!!')
#     elif choice == 'wait':
#         print('Good choice, now enter what you will do next.')
#         choice = input('Enter your choice red/blue/yellow: ')
        
#         if choice == 'red':
#             print('Burned by fire. Game Over!!')
#         elif choice == 'blue':
#             print('Eaten by beasts. Game Over!!')
#         elif choice == 'yellow':
#             print('You WIN!!')
#         else:
#             print('Invalid choice. Game Over!!')
#     else:
#         print('Invalid choice. Game Over!!')
# else:
#     print('Invalid choice. Game Over!!')

#THis is the rock paper scissors game.


import random

rock="""   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_options=["rock", "paper", "scissor"]

playing = True
while playing:
    print('Welcome to the rock paper scissors game')
    print()
    random_integer=random.randint(0,2)
    choice=input('Please enter your choice from: rock, paper, scissor: \n')
    if choice=="rock":
        print('You have chosen: rock \n', rock)
    elif choice=="paper":
        print('You have chosen: paper \n', paper)
    else:
        print('You have chosen: scissor \n', scissor)

    print(f'computer chooses: {random_integer}')
    if random_integer==0:
        print('Computer has chosen: rock \n', rock)

    elif random_integer==1:
        print('Computer has chosen: paper \n', paper)

    else:
        print('Computer has chosen: scissor \n', scissor)

    if choice=="rock" and random_integer==0:
        print('Duce!')
    elif choice=="paper" and random_integer==0:
        print('You Win')
    elif choice=="scissor" and random_integer==0:
        print('You Lose')
    elif choice=="rock" and random_integer==1:
        print('You Lose')
    elif choice=="paper" and random_integer==1:
        print('Duce!')
    elif choice=="scissor" and random_integer==1:
        print('You Win')
    elif choice=="rock" and random_integer==2:
        print('You Win')
    elif choice=="paper" and random_integer==2:
        print('You Lose')
    else: 
        print('Duce!')

    play_again= input('Do you want to play again (yes/no): ')
    if play_again=='no':
        playing=False
        print('Thanks for playing')