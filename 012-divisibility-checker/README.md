# Divisibility and Even/Odd Checker

**Date:** December 2024

## What I Learned
- Modulo operator (`%`) for finding remainders
- Checking divisibility (remainder == 0)
- Checking even/odd (number % 2)
- Nested if statements
- Avoiding division by zero errors

## Key Concept: Modulo Operator
The modulo operator `%` returns the remainder of a division:
```python
10 % 3 = 1    # 10 divided by 3 = 3 remainder 1
12 % 4 = 0    # 12 divided by 4 = 3 remainder 0 (completely divisible)
7 % 2 = 1     # 7 is odd (remainder when divided by 2)
8 % 2 = 0     # 8 is even (no remainder when divided by 2)
```

## Concepts Covered
- Modulo operations
- Divisibility testing
- Even/odd determination
- Error prevention (division by zero)
- Nested conditionals

## How to Run
```bash
python divisibility_checker.py
```

## Example Usage
```
=== Divisibility Checker ===

Enter the value of a: 15
Enter the value of b: 5

----------------------------------------
RESULTS
----------------------------------------
15 is completely divisible by 5
  15 / 5 = 3 with no remainder
----------------------------------------
15 is an ODD number
5 is an ODD number
----------------------------------------
```
