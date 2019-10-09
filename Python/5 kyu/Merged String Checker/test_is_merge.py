import unittest

from ismerge_02 import is_merge


class TestIsMerge(unittest.TestCase):
    def test_is_merge_01(self):
        self.assertEqual(is_merge('codewars', 'code', 'wars'), True)

    def test_is_merge_02(self):
        self.assertEqual(is_merge('codewars', 'cdw', 'oears'), True)

    def test_is_merge_03(self):
        self.assertEqual(is_merge('codewars', 'cod', 'wars'), False)

    def test_is_merge_04(self):
        self.assertEqual(is_merge('Making progress', 'Mak pross', 'inggre'),
                         True)

    def test_is_merge_05(self):
        self.assertEqual(is_merge('codewars', 'code', 'code'), False)

    def test_is_merge_06(self):
        self.assertEqual(is_merge('More progress', 'More ess', 'pro'), False)

    def test_is_merge_07(self):
        self.assertEqual(is_merge('codewars', 'codewars', ''), True)

    def test_is_merge_08(self):
        self.assertEqual(is_merge('codewars', '', 'codewars'), True)

    def test_is_merge_09(self):
        self.assertEqual(is_merge('', '', ''), True)

    def test_is_merge_10(self):
        self.assertEqual(is_merge('', 'no', 'siree'), False)

    def test_is_merge_11(self):
        self.assertEqual(is_merge('codewars', 'code', 'war'), False)

    def test_is_merge_12(self):
        self.assertEqual(is_merge('codewars', 'c', 'o'), False)

    def test_is_merge_13(self):
        self.assertEqual(is_merge('codewars', 'code', 'warss'), False)
    
    def test_is_merge_14(self):
        self.assertEqual(is_merge('codewars', 'codes', 'wars'), False)

    def test_is_merge_15(self):
        self.assertEqual(is_merge('codewars', 'code', 'wasr'), False)

    def test_is_merge_16(self):
        self.assertEqual(is_merge('codewars', 'cwdr', 'oeas'), False)

    def test_is_merge_17(self):
        self.assertEqual(is_merge('Bananas from Bahamas', 'Bahas',
                                  'Bananas from am'), True)

    def test_is_merge_18(self):
        self.assertEqual(is_merge("Can we merge it? No, we can't",
                                  "an e mergit? e, ec!", "Cwe Ysw an"), False)

    def test_is_merge_19(self):
        self.assertEqual(is_merge('$>J\'525s\\7ND$>J\'55F.VhqzO8G. R"',
                                  '$>J\'55F.VO8G. R"',
                                  '$>J\'525s\\7NDhqz'), True)


if __name__ == '__main__':
    unittest.main()
