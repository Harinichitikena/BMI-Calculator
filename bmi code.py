def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

# Example usage:
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))

bmi_value, bmi_category = calculate_bmi(weight, height)
print(f"BMI: {bmi_value:.2f} - {bmi_category}")