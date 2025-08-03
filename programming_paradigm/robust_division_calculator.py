# Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.

# Task Description:
# Create two Python scripts: robust_division_calculator.py, which contains the division logic including error handling, and main.py, which interfaces with the user through the command line.

# robust_division_calculator.py:
# Define a function safe_divide(numerator, denominator) that performs division, handling potential errors:

# Division by Zero: Use a try-except block to catch ZeroDivisionError.
# Non-numeric Input: Attempt to convert arguments to floats. Use a try-except block to catch ValueError for non-numeric inputs.
# Return appropriate messages for errors or the result for successful division.
# main.py for Command Line Interaction:
# This script will import safe_divide from robust_division_calculator.py and use it to divide numbers provided as command line arguments.

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    


    