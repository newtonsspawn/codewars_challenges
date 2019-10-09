from unittest import TestCase
from fib import fib


class TestFib(TestCase):
    
    def test_fib_01(self):
        self.assertEqual(fib(0), 0)
    
    def test_fib_02(self):
        self.assertEqual(fib(1), 1)
    
    def test_fib_03(self):
        self.assertEqual(fib(2), 1)
    
    def test_fib_04(self):
        self.assertEqual(fib(3), 2)
    
    def test_fib_05(self):
        self.assertEqual(fib(4), 3)
    
    def test_fib_06(self):
        self.assertEqual(fib(5), 5)
    
    def test_fib_07(self):
        self.assertEqual(fib(-6), -8)
    
    def test_fib_08(self):
        self.assertEqual(fib(-96), -51680708854858323072L)
    
    def test_fib_09(self):
        self.assertEqual(fib(-95), 31940434634990099905L)
    
    def test_fib_10(self):
        self.assertEqual(fib(-97), 83621143489848422977L)
    
    def test_fib_11(self):
        self.assertEqual(fib(-16), -987)
    
    def test_fib_12(self):
        self.assertEqual(fib(-77), 5527939700884757)
    
    def test_fib_13(self):
        self.assertEqual(fib(-46), -1836311903)
    
    def test_fib_14(self):
        self.assertEqual(fib(-82), -61305790721611591)
    
    def test_fib_15(self):
        self.assertEqual(fib(-13), 233)
    
    def test_fib_16(self):
        self.assertEqual(fib(-58), -591286729879)
    
    def test_fib_17(self):
        self.assertEqual(fib(-64), -10610209857723)
    
    def test_fib_18(self):
        self.assertEqual(fib(-81), 37889062373143906)
