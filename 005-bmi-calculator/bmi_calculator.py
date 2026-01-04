# BMI Calculator with Health Categories
# Date: December 2024

print("=== BMI Calculator ===")
print()

# Get user input
height_cm = float(input("Please enter your height in cm: "))
weight_kg = float(input("Please enter your weight in kg: "))

# Convert height to meters
height_m = height_cm / 100

# Calculate BMI
# Formula: BMI = weight(kg) / height(m)^2
bmi = weight_kg / (height_m ** 2)

# Display results
print()
print(f"Your height: {height_cm} cm ({height_m:.2f} m)")
print(f"Your weight: {weight_kg} kg")
print(f"Your BMI: {bmi:.2f}")
print()

# Determine health category
if bmi < 18.5:
    category = "Underweight"
    advice = "You may need to gain some weight. Consult a healthcare provider."
elif bmi >= 18.5 and bmi < 25:
    category = "Normal weight"
    advice = "Great! You are in a healthy weight range."
elif bmi >= 25 and bmi < 30:
    category = "Overweight"
    advice = "Consider a balanced diet and regular exercise."
else:
    category = "Obese"
    advice = "Please consult a healthcare provider for guidance."

print(f"Category: {category}")
print(f"Advice: {advice}")
