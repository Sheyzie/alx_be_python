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
    self.assertEqual(self.calc.add(4, 2), 6)  
    self.assertEqual(self.calc.add(-3, -2), -5)  
    # Add more assertions to thoroughly test the add method.

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(4, 1), 3)
    self.assertEqual(self.calc.subtract(-3, 1), -4)
    self.assertEqual(self.calc.subtract(-2, -2), 0)
    self.assertEqual(self.calc.subtract(4, -1), 5)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 2), 4)
    self.assertEqual(self.calc.multiply(3, 0), 0)
    self.assertEqual(self.calc.multiply(-2, 4), -8)
    self.assertEqual(self.calc.multiply(-2, -2), 4)

  def test_division(self):
    self.assertEqual(self.calc.divide(4, 2), 2)
    self.assertEqual(self.calc.divide(0, 3), 0)
    with self.assertRaises(ZeroDivisionError):
      self.calc.divide(10, 0)
    with self.assertRaises(TypeError):
       self.calc.divide('ten', 5)
    
# Remember to write additional test methods for subtract, multiply, and divide.

if __name__ == '__main__':
  unittest.main()