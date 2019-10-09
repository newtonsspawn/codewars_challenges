from unittest import TestCase

from permutations import permutations


class TestPermutations(TestCase):
    
    def test_permutations_01(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        
    def test_permutations_02(self):
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        
    def test_permutations_03(self):
        self.assertEqual(sorted(permutations('aabb')),
                         ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])
