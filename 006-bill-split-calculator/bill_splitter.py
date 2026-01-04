# Restaurant Bill Split Calculator
# Date: December 2024

print("=== Restaurant Bill Splitter ===")
print()

# Get user input
total_bill = float(input("Enter the total bill amount: $"))
number_of_people = int(input("Enter the number of people: "))
tip_percent = int(input("Enter the tip percentage (e.g., 15, 18, 20): "))

# Calculate tip amount
tip_amount = (total_bill * tip_percent) / 100

# Calculate grand total (bill + tip)
grand_total = total_bill + tip_amount

# Calculate per person amount
per_person = grand_total / number_of_people

# Display results
print()
print("-" * 40)
print("BILL SUMMARY")
print("-" * 40)
print(f"Subtotal:           ${total_bill:.2f}")
print(f"Tip ({tip_percent}%):          ${tip_amount:.2f}")
print(f"Grand Total:        ${grand_total:.2f}")
print("-" * 40)
print(f"Split {number_of_people} ways:       ${per_person:.2f} per person")
print("-" * 40)
