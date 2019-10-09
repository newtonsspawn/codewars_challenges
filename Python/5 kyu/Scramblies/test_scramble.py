from unittest import TestCase

from scramble_03 import scramble


class TestScramble(TestCase):
    def test_scramble_01(self):
        self.assertEqual(scramble('rkqodlw', 'world'), True)
    
    def test_scramble_02(self):
        self.assertEqual(scramble('cedewaraaossoqqyt', 'codewars'), True)
    
    def test_scramble_03(self):
        self.assertEqual(scramble('katas', 'steak'), False)
    
    def test_scramble_04(self):
        self.assertEqual(scramble('scriptjava', 'javascript'), True)
    
    def test_scramble_05(self):
        self.assertEqual(scramble('scriptingjava', 'javascript'), True)

    def test_scramble_06(self):
        self.assertEqual(scramble('eqspppzgexxd', 'zkxiwmcizcrqimxhjv'), False)