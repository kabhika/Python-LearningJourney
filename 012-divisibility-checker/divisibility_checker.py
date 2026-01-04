# Divisibility and Even/Odd Checker
# Date: December 2024

print("=== Divisibility Checker ===")
print()

# Get user input
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print()
print("-" * 40)
print("RESULTS")
print("-" * 40)

# Check if a is completely divisible by b
if b != 0:  # Avoid division by zero
    if (a % b) == 0:
        print(f"{a} is completely divisible by {b}")
        print(f"  {a} / {b} = {a // b} with no remainder")
    else:
        remainder = a % b
        print(f"{a} is NOT completely divisible by {b}")
        print(f"  {a} / {b} = {a // b} with remainder {remainder}")
else:
    print("Cannot divide by zero!")

print("-" * 40)

# Check if a is even or odd
if (a % 2) == 0:
    print(f"{a} is an EVEN number")
else:
    print(f"{a} is an ODD number")

# Check if b is even or odd
if (b % 2) == 0:
    print(f"{b} is an EVEN number")
else:
    print(f"{b} is an ODD number")

print("-" * 40)
