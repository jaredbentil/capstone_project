# test_simple_calculator.py
"""A simple calculator class that supports basic arithmetic operations."""

import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculator:
    """A simple calculator class that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        pass
def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b

# Example usage:
if __name__ == "__main__":
    calc = SimpleCalculator()
    print("Addition:", calc.add(2, 3))          # Output: 5
    print("Subtraction:", calc.subtract(5, 3))  # Output: 2
    print("Multiplication:", calc.multiply(2, 3))  # Output: 6
    print("Division:", calc.divide(6, 3))        # Output: 2.0
    print("Division by zero:", calc.divide(5, 0))  # Output: None
# This code defines a simple calculator class with methods for addition, subtraction, multiplication, and division


