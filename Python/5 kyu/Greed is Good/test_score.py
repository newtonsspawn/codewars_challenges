from unittest import TestCase

from score import score


class TestScore(TestCase):
    
    def test_score_01(self):
        self.assertEqual(score([2, 3, 4, 6, 2]), 0)

    def test_score_02(self):
        self.assertEqual(score([4, 4, 4, 3, 3]), 400)
    
    def test_score_03(self):
        self.assertEqual(score([2, 4, 4, 5, 4]), 450)
    
    def test_score_04(self):
        self.assertEqual(score([5, 1, 3, 4, 1]), 250)
        
    def test_score_05(self):
        self.assertEqual(score([1, 1, 1, 3, 1]), 1100)
