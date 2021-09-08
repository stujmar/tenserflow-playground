import unittest
from circle import *
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas of positive radii
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), pi)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)