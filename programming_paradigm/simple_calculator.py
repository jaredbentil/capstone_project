import unittest
from simple_calculator import SimpleCalculator  

class TestSimpleCalculator(unittest.TestCase):  
    
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero should return None
        self.assertEqual(self.calc.divide(0, 5), 0)   # Zero divided by any number should return zero   

    def test_division_negative(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
    def test_division_float(self):
        """Test division with float numbers."""
        self.assertAlmostEqual(self.calc.divide(5.0, 2.0), 2.5)
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)         
        self.assertAlmostEqual(self.calc.divide(0.0, 1.0), 0.0)

if __name__ == "__main__":
    unittest.main()
# This will run all the tests defined in the TestSimpleCalculator class.
