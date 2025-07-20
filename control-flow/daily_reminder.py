#Objective: Create a simplified Python script that uses conditional statements, Match Case, and loops to remind the user about a single, priority task for the day based on time sensitivity.

#Task Description:

#Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

#Instructions:

#Prompt for a Single Task:

#Ask the user to input a task description and save it into a task variable
#Prompt for the task’s priority (high, medium, low) and save it into a priority variable
#In a time_bound variable, Ask if the task is time-bound (yes or no)
#Process the Task Based on Priority and Time Sensitivity:

#Use a Match Case statement to react differently based on the task’s priority.
#Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
#Provide a Customized Reminder:

#Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
#A message should be ‘that requires immediate attention today!’

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
match priority:
    case "high":
        reminder = f"High priority task: {task}."
        if time_bound == "yes":
            print("This task requires immediate attention today!")
        else:
            print("This task can be addressed later.") 
    case "medium":
        reminder = f"Medium priority task: {task}."
        if time_bound == "yes":
            print("This task should be completed soon.")
        else:
            print("This task can wait until later.")    
    case "low":
        reminder = f"Low priority task: {task}."
        if time_bound == "yes":
            print("This task should be completed soon.")
        else:
            print("This task can wait until later.")    
    case _:
        reminder = "Invalid priority level."