"""
Sample tests
"""

from django.test import SimpleTestCase

from .calc import add, multiply, subtract

class TestCalc(SimpleTestCase):
    def test_add(self):
        sum = add(1, 2)

        self.assertEqual(sum, 3)
    
    def test_multiply(self):
        res = multiply(2, 4)

        self.assertEqual(res, 8)

    def test_subtract(self):
        res = subtract(4, 2)

        self.assertEqual(res, 2)