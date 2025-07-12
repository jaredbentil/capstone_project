# Objective: Practice receiving user input in Python and perform a simple arithmetic operation to calculate the user’s age in a future year.

#Task Description:

#Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

#Instructions:

#Create a file named future_age_calculator.py.
#Prompt the user to input their current age with the question: “How old are you? ”.
#Assume the user will input a valid integer value.
#Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.

current_age = int(input("How old are you? "))  # Get user input for current age
future_age = current_age + 27  # Calculate age in 2050
print("In the year 2050, you will be", future_age, "years old")  # Output the future age
# The script should output the user's future age in a clear and readable format.
# The expected output should look like this: