# Objective: Utilize while loops and nested for loops to draw a simple text-based pattern.

#Task Description:

#Develop a Python script named pattern_drawing.py. This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).

#Instructions:

#Prompt User for Pattern Size:

#Ask the user to input a positive integer that represents the size of the pattern (i.e., the length of each side of the square): Enter the size of the pattern:.
#Draw the Pattern:

#First, use a while loop to iterate through each row of the pattern.
#Inside the while loop, use a for loop to print asterisks (*) side by side without advancing to a new line (you can use print("*", end="") for this).
#After completing each row, print a newline character to move to the next row.
#Continue until the pattern forms a square of the inputted size.

size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after printing one row of asterisks
    row += 1

# End of the script