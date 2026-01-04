# Number Guessing Game
# Date: December 2024

import random

print("=== Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100...")
print()

# Generate random secret number
secret = random.randint(1, 100)

# Track number of attempts
attempts = 0
max_attempts = 10
guessed_correctly = False

# Game loop
while attempts < max_attempts and not guessed_correctly:
    # Get user's guess
    user_input = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
    attempts += 1
    
    # Check the guess
    if user_input > secret:
        print("Too high! Try a lower number.")
        print()
    elif user_input < secret:
        print("Too low! Try a higher number.")
        print()
    else:
        guessed_correctly = True
        print()
        print("=" * 40)
        print(f"Congratulations! You guessed it!")
        print(f"The number was {secret}")
        print(f"You got it in {attempts} attempts!")
        print("=" * 40)

# If player ran out of attempts
if not guessed_correctly:
    print()
    print("=" * 40)
    print("Game Over! You ran out of attempts.")
    print(f"The secret number was: {secret}")
    print("=" * 40)

# Ask to play again
print()
play_again = input("Want to play again? (yes/no): ").lower()
if play_again == 'yes':
    print("Run the program again to play!")
else:
    print("Thanks for playing!")
