from unittest import TestCase

from gettotalprimes_02 import get_total_primes


class TestGetTotalPrimes(TestCase):
    def test_get_total_primes_01(self):
        self.assertEqual(get_total_primes(10, 100), 4)  # 23, 37, 53, 73

    def test_get_total_primes_02(self):
        self.assertEqual(get_total_primes(500, 600), 3)  # 523, 557, 577

    def test_get_total_primes_03(self):
        self.assertEqual(get_total_primes(96854, 8949613), 1714)

    def test_get_total_primes_04(self):
        self.assertEqual(get_total_primes(76211, 7424122), 1573)

    def test_get_total_primes_05(self):
        self.assertEqual(get_total_primes(61974, 9979856), 1753)

    def test_get_total_primes_06(self):
        self.assertEqual(get_total_primes(38216, 6753932), 1464)

    def test_get_total_primes_07(self):
        self.assertEqual(get_total_primes(74437, 1379640), 411)

    def test_get_total_primes_08(self):
        self.assertEqual(get_total_primes(89602, 7610472), 1633)

    def test_get_total_primes_09(self):
        self.assertEqual(get_total_primes(69688, 6802908), 1438)

    def test_get_total_primes_10(self):
        self.assertEqual(get_total_primes(97, 6126), 42)
    
    def test_get_total_primes_11(self):
        self.assertEqual(get_total_primes(58, 1501), 16)
    
    def test_get_total_primes_12(self):
        self.assertEqual(get_total_primes(12, 4290), 36)
    
    def test_get_total_primes_13(self):
        self.assertEqual(get_total_primes(78, 7230), 42)
    
    def test_get_total_primes_14(self):
        self.assertEqual(get_total_primes(20, 9573), 57)
    
    def test_get_total_primes_15(self):
        self.assertEqual(get_total_primes(48, 3883), 34)
    
    def test_get_total_primes_16(self):
        self.assertEqual(get_total_primes(3, 3800), 39)
    
    def test_get_total_primes_17(self):
        self.assertEqual(get_total_primes(96, 9294), 53)
    
    def test_get_total_primes_18(self):
        self.assertEqual(get_total_primes(40, 5976), 44)
    
    def test_get_total_primes_19(self):
        self.assertEqual(get_total_primes(68, 7181), 43)
    
    def test_get_total_primes_20(self):
        self.assertEqual(get_total_primes(16, 6217), 46)
    
    def test_get_total_primes_21(self):
        self.assertEqual(get_total_primes(63, 6674), 43)
    
    def test_get_total_primes_22(self):
        self.assertEqual(get_total_primes(25, 9915), 56)
    
    def test_get_total_primes_23(self):
        self.assertEqual(get_total_primes(161, 70558), 142)
    
    def test_get_total_primes_24(self):
        self.assertEqual(get_total_primes(530, 79901), 172)
    
    def test_get_total_primes_25(self):
        self.assertEqual(get_total_primes(389, 47780), 108)
    
    def test_get_total_primes_26(self):
        self.assertEqual(get_total_primes(905, 99793), 166)
    
    def test_get_total_primes_27(self):
        self.assertEqual(get_total_primes(726, 30910), 70)
    
    def test_get_total_primes_28(self):
        self.assertEqual(get_total_primes(166, 581), 11)
    
    def test_get_total_primes_29(self):
        self.assertEqual(get_total_primes(932, 26060), 59)
    
    def test_get_total_primes_30(self):
        self.assertEqual(get_total_primes(651, 25704), 62)
    
    def test_get_total_primes_31(self):
        self.assertEqual(get_total_primes(578, 13522), 42)
    
    def test_get_total_primes_32(self):
        self.assertEqual(get_total_primes(674, 96913), 170)
    
    def test_get_total_primes_33(self):
        self.assertEqual(get_total_primes(478, 34136), 90)
    
    def test_get_total_primes_34(self):
        self.assertEqual(get_total_primes(857, 99894), 166)
    
    def test_get_total_primes_35(self):
        self.assertEqual(get_total_primes(7504, 770144), 505)
    
    def test_get_total_primes_36(self):
        self.assertEqual(get_total_primes(4928, 242611), 200)
    
    def test_get_total_primes_37(self):
        self.assertEqual(get_total_primes(1477, 172371), 166)
    
    def test_get_total_primes_38(self):
        self.assertEqual(get_total_primes(35, 704859), 483)
    
    def test_get_total_primes_39(self):
        self.assertEqual(get_total_primes(9920, 953915), 517)
    
    def test_get_total_primes_40(self):
        self.assertEqual(get_total_primes(8511, 104886), 128)
    
    def test_get_total_primes_41(self):
        self.assertEqual(get_total_primes(5226, 724819), 463)
    
    def test_get_total_primes_42(self):
        self.assertEqual(get_total_primes(2096, 661528), 465)
    
    def test_get_total_primes_43(self):
        self.assertEqual(get_total_primes(1275, 529775), 390)
    
    def test_get_total_primes_44(self):
        self.assertEqual(get_total_primes(5773, 220097), 139)
    
    def test_get_total_primes_45(self):
        self.assertEqual(get_total_primes(5894, 177716), 139)
    
    def test_get_total_primes_46(self):
        self.assertEqual(get_total_primes(1051, 174636), 166)
    
    def test_get_total_primes_47(self):
        self.assertEqual(get_total_primes(7843, 947629), 517)
    
    def test_get_total_primes_48(self):
        self.assertEqual(get_total_primes(2191, 9510881), 1880)
    
    def test_get_total_primes_49(self):
        self.assertEqual(get_total_primes(31464, 6437884), 1499)
    
    def test_get_total_primes_50(self):
        self.assertEqual(get_total_primes(25348, 6661612), 1512)
    
    def test_get_total_primes_51(self):
        self.assertEqual(get_total_primes(89693, 1455164), 389)
    
    def test_get_total_primes_52(self):
        self.assertEqual(get_total_primes(73354, 180360), 26)
