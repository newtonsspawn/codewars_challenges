from unittest import TestCase
from interpreter import Interpreter


# ##### TEST CASE 01 #####

interpreter_01 = Interpreter()


class TestInterpreter01(TestCase):
    
    # Basic Arithmetic
    def test_input01_01(self):
        self.assertEqual(interpreter_01.input("1 + 1"), 2)
    
    def test_input01_02(self):
        self.assertEqual(interpreter_01.input("2 - 1"), 1)
    
    def test_input01_03(self):
        self.assertEqual(interpreter_01.input("2 * 3"), 6)
    
    def test_input01_04(self):
        self.assertEqual(interpreter_01.input("8 / 4"), 2)
    
    def test_input01_05(self):
        self.assertEqual(interpreter_01.input("7 % 4"), 3)
    
    # Variables
    def test_input01_06(self):
        self.assertEqual(interpreter_01.input("x = 1"), 1)
    
    def test_input01_07(self):
        self.assertEqual(interpreter_01.input("x"), 1)
    
    def test_input01_08(self):
        self.assertEqual(interpreter_01.input("x + 3"), 4)
    
    def test_input01_error_01(self):
        self.assertRaises(BaseException, interpreter_01.input("y"))


# ##### TEST CASE 01 #####

interpreter_02 = Interpreter()


class TestInterpreter02(TestCase):
    
    # Basic Arithmetic
    def test_input02_01(self):
        self.assertEqual(interpreter_02.input(""), '')
    
    def test_input02_02(self):
        self.assertEqual(interpreter_02.input(" "), '')
    
    def test_input02_error_01(self):
        self.assertRaises(BaseException, interpreter_02.input("1 2"))
    
    def test_input02_error_02(self):
        self.assertRaises(BaseException, interpreter_02.input("1two"))
    
    def test_input02_03(self):
        self.assertEqual(interpreter_02.input("1 + 1"), 2)
    
    def test_input02_04(self):
        self.assertEqual(interpreter_02.input("2+2"), 4)
    
    def test_input02_05(self):
        self.assertEqual(interpreter_02.input("2 - 1"), 1)
    
    def test_input02_06(self):
        self.assertEqual(interpreter_02.input("4-6"), -2)
    
    def test_input02_07(self):
        self.assertEqual(interpreter_02.input("2 * 3"), 6)
    
    def test_input02_08(self):
        self.assertEqual(interpreter_02.input("8 / 4"), 2)
    
    def test_input02_09(self):
        self.assertEqual(interpreter_02.input("7 % 4"), 3)
    
    # Complex Expressions
    def test_input02_10(self):
        self.assertEqual(interpreter_02.input("4 + 2 * 3"), 10)
    
    def test_input02_11(self):
        self.assertEqual(interpreter_02.input("4 / 2 * 3"), 6)
    
    def test_input02_12(self):
        self.assertEqual(interpreter_02.input("7 % 2 * 8"), 8)
    
    def test_input02_13(self):
        self.assertEqual(interpreter_02.input("(4 + 2) * 3"), 18)
    
    def test_input02_14(self):
        self.assertEqual(interpreter_02.input("(7 + 3) / (2 * 2 + 1)"), 2)
    
    def test_input02_15(self):
        self.assertEqual(interpreter_02.input("(8 - (4 + 2)) * 3"), 6)
    
    def test_input02_16(self):
        self.assertEqual(interpreter_02.input("(10 / (8 - (4 + 2))) * 3"), 15)
    
    # Variables
    def test_input02_17(self):
        self.assertEqual(interpreter_02.input("x = 7"), 7)
    
    def test_input02_18(self):
        self.assertEqual(interpreter_02.input("x"), 7)
    
    def test_input02_19(self):
        self.assertEqual(interpreter_02.input("x + 3"), 10)
    
    def test_input02_error_03(self):
        self.assertRaises(BaseException, interpreter_02.input("y"))
    
    def test_input02_20(self):
        self.assertEqual(interpreter_02.input("y = x + 5"), 12)
    
    def test_input02_21(self):
        self.assertEqual(interpreter_02.input("y"), 12)
