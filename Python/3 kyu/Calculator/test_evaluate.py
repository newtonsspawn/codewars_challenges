from unittest import TestCase

from evaluate import Calculator

calc = Calculator()


class TestCalculator(TestCase):
    
    def test_evaluate_01(self):
        self.assertEqual(calc.evaluate(string='127'), 127)
    
    def test_evaluate_02(self):
        self.assertEqual(calc.evaluate(string='2 + 3'), 5)
    
    def test_evaluate_03(self):
        self.assertEqual(calc.evaluate(string='2 - 3 - 4'), -5)
    
    def test_evaluate_04(self):
        self.assertEqual(calc.evaluate(string='10 * 5 / 2'), 25)
    
    def test_evaluate_05(self):
        self.assertEqual(calc.evaluate(string='2 / 2 + 3 * 4 - 6'), 7)
    
    def test_evaluate_06(self):
        self.assertEqual(calc.evaluate(string='2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'),
                         8)
    
    def test_evaluate_07(self):
        self.assertEqual(calc.evaluate(string='1.1 + 2.2 + 3.3'), 6.6)
    
    def test_evaluate_08(self):
        self.assertEqual(calc.evaluate(string='1.1 * 2.2 * 3.3'), 7.986)
