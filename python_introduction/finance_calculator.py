# Objective: Use user input, variables, and arithmetic operations to calculate and provide feedback on a user’s monthly savings and potential future savings without applying conditional statements.

#Task Description:

#You will create a script named finance_calculator.py. This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

#Instructions:

#User Input for Financial Details:

#Prompt the user for their monthly income: “Enter your monthly income: ”.
#Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
#Calculate Monthly Savings:

#Calculate the monthly savings by subtracting monthly expenses from the monthly income.
#Project Annual Savings:

#Assume a simple annual interest rate of 5%.
#Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).

monthly_income = float(input("Enter your monthly income: "))  # Get user input for monthly income
monthly_expenses = float(input("Enter your total monthly expenses: "))  # Get user input for monthly expenses
monthly_savings = monthly_income - monthly_expenses  # Calculate monthly savings
annual_savings = monthly_savings * 12  # Calculate total savings for the year
projected_savings = annual_savings + (annual_savings * 0.05)  # Calculate projected savings after one year with 5% interest
print("Your monthly savings are:", monthly_savings)  # Output monthly savings
print("Your projected savings after one year is:", projected_savings)  # Output projected savings
# The script should output the user's monthly savings and projected savings in a clear and readable format.
# The expected output should look like this:
# Enter your monthly income: 3000
# Enter your total monthly expenses: 2000
# Your monthly savings are: 1000.0
# Your projected savings after one year is: 12600.0

# The script should not include any conditional statements, focusing solely on arithmetic operations and user input.
# end of finance_calculator.py