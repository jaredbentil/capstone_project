# Objective: Utilize conditional statements to guide program execution based on user input regarding weather conditions.

#Task Description:

#Create a Python script named weather_advice.py. This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

#Instructions:

#Prompt User for Weather Input:

#Ask the user to input the current weather from a predefined set of conditions: sunny, rainy, or cold.
#Use the prompt: What's the weather like today? (sunny/rainy/cold):.
#Provide Clothing Recommendations:

#Based on the user’s input, your program will recommend different types of clothing:
#If the weather is “sunny”, recommend: Wear a t-shirt and sunglasses.
#If the weather is “rainy”, recommend: Don't forget your umbrella and a raincoat.
#If the weather is “cold”, recommend: Make sure to wear a warm coat and a scarf.
#Include an else statement that handles unexpected input by printing: Sorry, I don't have recommendations for this weather.


weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

# End of the script