# this programs calculates the bmi of a person
def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / (height (m)^2)

    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: The calculated BMI
    """
    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi):
    """
    Determines the BMI category based on standard BMI ranges.

    Parameters:
    bmi (float): The BMI value to categorize

    Returns:
    str: The BMI category
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


# Get user input
try:
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Category: {category}")

except ValueError:
    print("Please enter valid numeric values for weight and height.")
