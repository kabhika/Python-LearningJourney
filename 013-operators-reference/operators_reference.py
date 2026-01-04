# Arithmetic and Comparison Operators Reference
# Date: December 2024

print("=" * 50)
print("PYTHON OPERATORS REFERENCE")
print("=" * 50)
print()

# Define test values
a = 15
b = 9

print(f"Test values: a = {a}, b = {b}")
print()

# Arithmetic Operators
print("-" * 50)
print("ARITHMETIC OPERATORS")
print("-" * 50)
print(f"a + b  = {a + b:>6}  (Addition)")
print(f"a - b  = {a - b:>6}  (Subtraction)")
print(f"a * b  = {a * b:>6}  (Multiplication)")
print(f"a / b  = {a / b:>6.2f}  (Division)")
print(f"a // b = {a // b:>6}  (Floor Division)")
print(f"a % b  = {a % b:>6}  (Modulo/Remainder)")
print(f"a ** b = {a ** b:>6}  (Exponentiation)")
print()

# Comparison Operators
print("-" * 50)
print("COMPARISON OPERATORS")
print("-" * 50)
print(f"a > b  = {str(a > b):>6}  (Greater than)")
print(f"a < b  = {str(a < b):>6}  (Less than)")
print(f"a >= b = {str(a >= b):>6}  (Greater than or equal)")
print(f"a <= b = {str(a <= b):>6}  (Less than or equal)")
print(f"a == b = {str(a == b):>6}  (Equal to)")
print(f"a != b = {str(a != b):>6}  (Not equal to)")
print()

# List Operators
print("-" * 50)
print("LIST OPERATORS")
print("-" * 50)
mats_1 = ["Concrete", "Steel", "Glass"]
mats_2 = ["Wood", "Brick"]
mats_3 = mats_1 + mats_2

print(f"mats_1 = {mats_1}")
print(f"mats_2 = {mats_2}")
print(f"mats_1 + mats_2 = {mats_3}  (Concatenation)")
print()
print(f"'Steel' in mats_1     = {str('Steel' in mats_1):>6}  (Membership)")
print(f"'Wood' in mats_1      = {str('Wood' in mats_1):>6}  (Membership)")
print(f"mats_1 == mats_2      = {str(mats_1 == mats_2):>6}  (Equality)")
print(f"mats_1 != mats_2      = {str(mats_1 != mats_2):>6}  (Inequality)")
print()

# Nested Lists
print("-" * 50)
print("NESTED LISTS")
print("-" * 50)
mats_4 = [["Concrete", "Steel", "Glass"], ["Wood", "Brick"]]
print(f"mats_4 = {mats_4}")
print(f"mats_2 in mats_4 = {mats_2 in mats_4}  (Check if list is in nested list)")
print()

print("=" * 50)
print("END OF REFERENCE")
print("=" * 50)
