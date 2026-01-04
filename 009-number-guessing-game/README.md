# Number Guessing Game

**Date:** December 2024

## What I Learned
- Importing modules (`import random`)
- Generating random numbers with `random.randint()`
- While loops with multiple conditions
- Tracking state with boolean variables
- String methods like `.lower()`

## Concepts Covered
- Module imports
- Random number generation
- While loops
- Boolean flags
- Game logic and state management
- User input validation

## How It Works
1. Computer generates a random number between 1-100
2. Player has 10 attempts to guess the number
3. After each guess, player gets feedback (too high/too low)
4. Game ends when player guesses correctly or runs out of attempts

## How to Run
```bash
python guessing_game.py
```

## Example Gameplay
```
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100...

Attempt 1/10 - Enter your guess: 50
Too high! Try a lower number.

Attempt 2/10 - Enter your guess: 25
Too low! Try a higher number.

Attempt 3/10 - Enter your guess: 37
Too high! Try a lower number.

Attempt 4/10 - Enter your guess: 31

========================================
Congratulations! You guessed it!
The number was 31
You got it in 4 attempts!
========================================
```
