# Rectangle Area and Perimeter Calculator
# Date: December 2024

print("=== Rectangle Calculator ===")
print()

# Get dimensions from user
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

# Calculate area
# Formula: Area = length x width
area = length * width

# Calculate perimeter
# Formula: Perimeter = 2 x (length + width)
perimeter = 2 * (length + width)

# Display results
print()
print("-" * 35)
print("RECTANGLE PROPERTIES")
print("-" * 35)
print(f"Length:    {length} units")
print(f"Width:     {width} units")
print("-" * 35)
print(f"Area:      {area} square units")
print(f"Perimeter: {perimeter} units")
print("-" * 35)
