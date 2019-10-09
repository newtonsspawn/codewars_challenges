from unittest import TestCase
from lastdigit import last_digit


class TestLastDigit(TestCase):
        
    def test_last_digit_01(self):
        self.assertEqual(last_digit([]), 1)
        
    def test_last_digit_02(self):
        self.assertEqual(last_digit([0, 0]), 1)
        
    def test_last_digit_03(self):
        self.assertEqual(last_digit([0, 0, 0]), 0)
        
    def test_last_digit_04(self):
        self.assertEqual(last_digit([1, 2]), 1)
        
    def test_last_digit_05(self):
        self.assertEqual(last_digit([3, 4, 5]), 1)
        
    def test_last_digit_06(self):
        self.assertEqual(last_digit([4, 3, 6]), 4)
        
    def test_last_digit_07(self):
        self.assertEqual(last_digit([7, 6, 21]), 1)
        
    def test_last_digit_08(self):
        self.assertEqual(last_digit([12, 30, 21]), 6)
        
    def test_last_digit_09(self):
        self.assertEqual(last_digit([2, 2, 2, 0]), 4)
        
    def test_last_digit_10(self):
        self.assertEqual(last_digit([937640, 767456, 981242]), 0)
        
    def test_last_digit_11(self):
        self.assertEqual(last_digit([123232, 694022, 140249]), 6)
        
    def test_last_digit_12(self):
        self.assertEqual(last_digit([499942, 898102, 846073]), 6)
