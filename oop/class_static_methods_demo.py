# Objective: Solidify your understanding of class methods and static methods in Python by implementing examples of each in a class, demonstrating their usage and differences.

# Task Description:
# Create a Python script named class_static_methods_demo.py. In this script, define a class Calculator that includes both a class method and a static method to perform calculations. This task aims to illustrate when and how to use @classmethod and @staticmethod decorators, highlighting their differences and practical applications.

# class_static_methods_demo.py:
# Calculator Class:

# Static Method - add(a, b): Returns the sum of two numbers. Use the @staticmethod decorator.
# Class Method - multiply(cls, a, b): Returns the product of two numbers. Use the @classmethod decorator and ensure it prints a class attribute named calculation_type before performing the multiplication.
# Class Attribute:

# Define a class attribute calculation_type with a value of "Arithmetic Operations" that the multiply class method will reference.

class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b   

def main():
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")      

if __name__ == "__main__":
    main() 