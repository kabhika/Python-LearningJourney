# Rock Paper Scissors Game
# Date: January 2025

import random

rock = """   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_options = ["rock", "paper", "scissor"]

playing = True
while playing:
    random_integer = random.randint(0, 2)
    
    print('Welcome to the Rock Paper Scissors game')
    print()
    
    choice = input('Please enter your choice from: rock, paper, scissor: \n')
    
    if choice == "rock":
        print('You have chosen: rock \n', rock)
    elif choice == "paper":
        print('You have chosen: paper \n', paper)
    else:
        print('You have chosen: scissor \n', scissor)
    
    print(f'Computer chooses: {random_integer}')
    
    if random_integer == 0:
        print('Computer has chosen: rock \n', rock)
    elif random_integer == 1:
        print('Computer has chosen: paper \n', paper)
    else:
        print('Computer has chosen: scissor \n', scissor)
    
    if choice == "rock" and random_integer == 0:
        print('Draw!')
    elif choice == "paper" and random_integer == 0:
        print('You Win!')
    elif choice == "scissor" and random_integer == 0:
        print('You Lose!')
    elif choice == "rock" and random_integer == 1:
        print('You Lose!')
    elif choice == "paper" and random_integer == 1:
        print('Draw!')
    elif choice == "scissor" and random_integer == 1:
        print('You Win!')
    elif choice == "rock" and random_integer == 2:
        print('You Win!')
    elif choice == "paper" and random_integer == 2:
        print('You Lose!')
    else:
        print('Draw!')
    
    play_again = input('Do you want to play again (yes/no): ')
    if play_again == 'no':
        playing = False
        print('Thanks for playing!')
