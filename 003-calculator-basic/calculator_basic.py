# Basic Calculator using if/elif statements
# Date: December 2024

print("=== Simple Calculator ===")
print()

# Get user input
first_number = float(input("Please input the first number: "))
second_number = float(input("Please input the second number: "))
math_operator = input("Please input the math operator (+, -, *, /): ")

# Perform calculation based on operator
if math_operator == '+':
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif math_operator == '-':
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif math_operator == '*':
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif math_operator == '/':
    if second_number != 0:
        result = first_number / second_number
        print(f"{first_number} / {second_number} = {result}")
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator! Please use +, -, *, or /")
