# Calculator using match/case (Python 3.10+)
# Date: December 2024

print("=== Calculator with Match/Case ===")
print()

# Get user input
first_number = int(input("Please input the first number: "))
second_number = int(input("Please input the second number: "))
math_operator = input("Please input the math operator (+, -, *, /): ")

# Using match/case statement (Python 3.10+ feature)
match math_operator:
    case '+':
        result = first_number + second_number
    case '-':
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case '/':
        if second_number != 0:
            result = first_number / second_number
        else:
            print("Error: Cannot divide by zero!")
            result = None
    case _:
        print("Invalid operator! Please use +, -, *, or /")
        result = None

# Display result
if result is not None:
    print(f"{first_number} {math_operator} {second_number} = {result}")
