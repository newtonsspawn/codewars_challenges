from unittest import TestCase

from samestructureas import same_structure_as


class TestSameStructureAs(TestCase):
        
    def test_same_structure_as_01(self):
        self.assertEqual(same_structure_as([1, 1, 1], [2, 2, 2]), True)
        
    def test_same_structure_as_02(self):
        self.assertEqual(same_structure_as([1, [1, 1]], [2, [2, 2]]), True)
        
    def test_same_structure_as_03(self):
        self.assertEqual(same_structure_as([1, [1, 1]], [[2, 2], 2]), False)
        
    def test_same_structure_as_04(self):
        self.assertEqual(same_structure_as([1, [1, 1]], [2, [2]]), False)
        
    def test_same_structure_as_05(self):
        self.assertEqual(same_structure_as([[[], []]], [[[], []]]), True)
        
    def test_same_structure_as_06(self):
        self.assertEqual(same_structure_as([[[], []]], [[1, 1]]), False)
        
    def test_same_structure_as_07(self):
        self.assertEqual(same_structure_as([1, [[[1]]]], [2, [[[2]]]]), True)
        
    def test_same_structure_as_08(self):
        self.assertEqual(same_structure_as([], 1), False)
        
    def test_same_structure_as_09(self):
        self.assertEqual(same_structure_as([], {}), False)
        
    def test_same_structure_as_10(self):
        self.assertEqual(same_structure_as([1, '[', ']'], ['[', ']', 1]), True)
