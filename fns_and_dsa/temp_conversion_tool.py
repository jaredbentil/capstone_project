# Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.

#Task Description:
#Create a Python script named temp_conversion_tool.py. This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

#Requirements:
# Define Global Conversion Factors:

#At the top of your script, define two global variables FAHRENHEIT_TO_CELSIUS_FACTOR and CELSIUS_TO_FAHRENHEIT_FACTOR to store the conversion factors (e.g., (5/9) for F to C and (9/5) for C to F, respectively).
#Implement Conversion Functions:

#Write a function convert_to_celsius(fahrenheit) that takes a temperature in Fahrenheit and returns the temperature converted to Celsius.
#Write a function convert_to_fahrenheit(celsius) that takes a temperature in Celsius and returns the temperature converted to Fahrenheit.
#Inside each function, use the respective global conversion factor to perform the conversion.
#User Interaction:

#Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
#Based on the user’s input, call the appropriate conversion function and display the converted temperature.
#If the user entered a wrong input,raise an error “Invalid temperature. Please enter a numeric value.”
#Guidance:
#Remember to access global variables using the global keyword if you need to modify them inside functions. However, for this task, you’ll only be reading their values.
#Use input validation to ensure that the user enters a valid temperature and unit.

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    try:
        celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        return celsius
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")      
    
def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    try:
        fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        return fahrenheit
    except TypeError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
def main():
    try:
        temperature = float(input("Enter a temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            celsius = temperature
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is {fahrenheit:.2f}°F")
        elif unit == 'F':
            fahrenheit = temperature
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is {celsius:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)    

if __name__ == "__main__":
    main()
# This script provides a simple command-line interface for converting temperatures between Celsius and Fahrenheit, using global

    

