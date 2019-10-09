from unittest import TestCase

from bowlingscore import bowling_score


class TestBowlingScore(TestCase):
    
    def test_bowling_score_01(self):
        self.assertEqual(bowling_score('11 11 11 11 11 11 11 11 11 11'), 20)
    
    def test_bowling_score_02(self):
        self.assertEqual(bowling_score('X X X X X X X X X XXX'), 300)
    
    def test_bowling_score_03(self):
        self.assertEqual(bowling_score('00 5/ 4/ 53 33 22 4/ 5/ 45 XXX'), 115)
    
    def test_bowling_score_04(self):
        self.assertEqual(bowling_score('5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 8/8'), 150)
    
    def test_bowling_score_05(self):
        self.assertEqual(bowling_score('5/ 4/ 3/ 2/ 1/ 0/ X 9/ 4/ 7/2'), 143)
    
    def test_bowling_score_06(self):
        self.assertEqual(bowling_score('X X 9/ 80 X X 90 8/ 7/ 44'), 171)
    
    def test_bowling_score_07(self):
        self.assertEqual(bowling_score('6/ 5/ 6/ 2/ 3/ 0/ 1/ 8/ 3/ 6/5'), 139)
    
    def test_bowling_score_08(self):
        self.assertEqual(bowling_score('00 00 00 00 00 00 00 00 00 0/X'), 20)
    
    def test_bowling_score_09(self):
        self.assertEqual(bowling_score('00 00 00 00 00 00 00 00 X 0/X'), 40)
    
    def test_bowling_score_10(self):
        self.assertEqual(bowling_score('41 18 X X 12 05 16 34 8/ XX1'), 111)
    
    def test_bowling_score_11(self):
        self.assertEqual(bowling_score('9/ 71 40 X 53 80 09 50 01 1/X'), 98)
    
    def test_bowling_score_12(self):
        self.assertEqual(bowling_score('8/ 72 9/ 27 9/ 34 51 22 31 34'), 88)
    
    def test_bowling_score_13(self):
        self.assertEqual(bowling_score('33 81 07 8/ X 80 60 X X XX1'), 155)
    
    def test_bowling_score_14(self):
        self.assertEqual(bowling_score('80 54 50 70 80 16 34 9/ 05 1/X'), 86)
    
    def test_bowling_score_15(self):
        self.assertEqual(bowling_score('8/ 72 1/ 44 26 03 62 50 10 12'), 76)
    
    def test_bowling_score_16(self):
        self.assertEqual(bowling_score('81 8/ 50 53 9/ 1/ 25 00 24 XXX'), 103)
    
    def test_bowling_score_17(self):
        self.assertEqual(bowling_score('90 3/ 80 45 4/ 09 80 32 42 53'), 90)
    
    def test_bowling_score_18(self):
        self.assertEqual(bowling_score('5/ 14 17 31 08 62 42 41 43 XXX'), 92)
    
    def test_bowling_score_19(self):
        self.assertEqual(bowling_score('30 9/ 80 70 4/ 09 7/ 15 7/ XXX'), 122)
