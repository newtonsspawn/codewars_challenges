from unittest import TestCase

from isinteresting import is_interesting


class TestIsInteresting(TestCase):
        
    def test_is_interesting_01(self):
        self.assertEqual(is_interesting(1, []), 0)
        
    def test_is_interesting_02(self):
        self.assertEqual(is_interesting(30, []), 0)
        
    def test_is_interesting_03(self):
        self.assertEqual(is_interesting(88, []), 0)
        
    def test_is_interesting_04(self):
        self.assertEqual(is_interesting(97, []), 0)
        
    def test_is_interesting_05(self):
        self.assertEqual(is_interesting(7382, []), 0)
        
    def test_is_interesting_06(self):
        self.assertEqual(is_interesting(99919911, []), 0)
        
    def test_is_interesting_07(self):
        self.assertEqual(is_interesting(7540, []), 0)
        
    def test_is_interesting_08(self):
        self.assertEqual(is_interesting(1590, []), 0)
        
    def test_is_interesting_09(self):
        self.assertEqual(is_interesting(100, []), 2)
        
    def test_is_interesting_10(self):
        self.assertEqual(is_interesting(7000, []), 2)
        
    def test_is_interesting_11(self):
        self.assertEqual(is_interesting(800000, []), 2)
        
    def test_is_interesting_12(self):
        self.assertEqual(is_interesting(111, []), 2)
        
    def test_is_interesting_13(self):
        self.assertEqual(is_interesting(444, []), 2)
        
    def test_is_interesting_14(self):
        self.assertEqual(is_interesting(9999999, []), 2)
        
    def test_is_interesting_15(self):
        self.assertEqual(is_interesting(1337, [1337, 256]), 2)
        
    def test_is_interesting_16(self):
        self.assertEqual(is_interesting(80085, [80085]), 2)
        
    def test_is_interesting_17(self):
        self.assertEqual(is_interesting(256, [1337, 256, 376006]), 2)
        
    def test_is_interesting_18(self):
        self.assertEqual(is_interesting(101, []), 2)
        
    def test_is_interesting_19(self):
        self.assertEqual(is_interesting(11011, []), 2)
        
    def test_is_interesting_20(self):
        self.assertEqual(is_interesting(7473747, []), 2)
        
    def test_is_interesting_21(self):
        self.assertEqual(is_interesting(123, []), 2)
        
    def test_is_interesting_22(self):
        self.assertEqual(is_interesting(1234, []), 2)
        
    def test_is_interesting_23(self):
        self.assertEqual(is_interesting(67890, []), 2)
        
    def test_is_interesting_24(self):
        self.assertEqual(is_interesting(234567890, []), 2)
        
    def test_is_interesting_25(self):
        self.assertEqual(is_interesting(3210, []), 2)
        
    def test_is_interesting_26(self):
        self.assertEqual(is_interesting(654, []), 2)
        
    def test_is_interesting_27(self):
        self.assertEqual(is_interesting(8765, []), 2)
        
    def test_is_interesting_28(self):
        self.assertEqual(is_interesting(987654321, []), 2)
        
    def test_is_interesting_29(self):
        self.assertEqual(is_interesting(98, []), 1)
        
    def test_is_interesting_30(self):
        self.assertEqual(is_interesting(99, []), 1)
        
    def test_is_interesting_31(self):
        self.assertEqual(is_interesting(6998, []), 1)
        
    def test_is_interesting_32(self):
        self.assertEqual(is_interesting(799999, []), 1)
        
    def test_is_interesting_33(self):
        self.assertEqual(is_interesting(109, []), 1)
        
    def test_is_interesting_34(self):
        self.assertEqual(is_interesting(110, []), 1)
        
    def test_is_interesting_35(self):
        self.assertEqual(is_interesting(442, []), 1)
        
    def test_is_interesting_36(self):
        self.assertEqual(is_interesting(9999997, []), 1)
        
    def test_is_interesting_37(self):
        self.assertEqual(is_interesting(1335, [1337, 256]), 1)
        
    def test_is_interesting_38(self):
        self.assertEqual(is_interesting(255, [1337, 256]), 1)
        
    def test_is_interesting_39(self):
        self.assertEqual(is_interesting(80083, [80085]), 1)
        
    def test_is_interesting_40(self):
        self.assertEqual(is_interesting(254, [1337, 256, 376006]), 1)
        
    def test_is_interesting_41(self):
        self.assertEqual(is_interesting(119, []), 1)
        
    def test_is_interesting_42(self):
        self.assertEqual(is_interesting(120, []), 1)
        
    def test_is_interesting_43(self):
        self.assertEqual(is_interesting(7473745, []), 1)
        
    def test_is_interesting_44(self):
        self.assertEqual(is_interesting(122, []), 1)
        
    def test_is_interesting_45(self):
        self.assertEqual(is_interesting(1232, []), 1)
        
    def test_is_interesting_46(self):
        self.assertEqual(is_interesting(67888, []), 1)
        
    def test_is_interesting_47(self):
        self.assertEqual(is_interesting(234567889, []), 1)
        
    def test_is_interesting_48(self):
        self.assertEqual(is_interesting(3208, []), 1)
        
    def test_is_interesting_49(self):
        self.assertEqual(is_interesting(3209, []), 1)
        
    def test_is_interesting_50(self):
        self.assertEqual(is_interesting(987654319, []), 1)
        
    def test_is_interesting_51(self):
        self.assertEqual(is_interesting(987654320, []), 1)
