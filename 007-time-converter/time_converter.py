# Time Converter - Seconds to Hours, Minutes, Seconds
# Date: December 2024

print("=== Time Converter ===")
print("Convert seconds to hours, minutes, and seconds")
print()

# Get user input with validation
time_in_seconds = int(input("Please enter the time in seconds: "))

# Validate input (no negative numbers)
while time_in_seconds < 0:
    print("Error: Time cannot be negative!")
    time_in_seconds = int(input("Please enter a positive number of seconds: "))

# Store original value for display
original_seconds = time_in_seconds

# Calculate hours
# Floor division (//) gives whole hours
total_hours = time_in_seconds // 3600

# Calculate remaining seconds after removing hours
remainder_seconds = time_in_seconds % 3600

# Calculate minutes from remainder
total_minutes = remainder_seconds // 60

# Calculate final remaining seconds
total_seconds = remainder_seconds % 60

# Display results
print()
print("-" * 40)
print(f"Input: {original_seconds} seconds")
print("-" * 40)
print(f"Hours:   {total_hours}")
print(f"Minutes: {total_minutes}")
print(f"Seconds: {total_seconds}")
print("-" * 40)
print(f"Formatted: {total_hours:02d}:{total_minutes:02d}:{total_seconds:02d}")
print("-" * 40)
