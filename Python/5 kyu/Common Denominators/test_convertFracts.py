from unittest import TestCase

from convertfracts import convertFracts


class TestConvertFracts(TestCase):
    
    def test_convertFracts_01(self):
        self.assertEqual(convertFracts([[1, 2], [1, 3], [1, 4]]),
                         [[6, 12], [4, 12], [3, 12]])
    
    def test_convertFracts_02(self):
        self.assertEqual(convertFracts([]), [])

    def test_convertFracts_03(self):
        self.assertEqual(convertFracts([[27115, 5262],
                                        [87546, 11111111],
                                        [43216, 255689]]),
                         [[77033412951888085, 14949283383840498],
                          [117787497858828, 14949283383840498],
                          [2526695441399712, 14949283383840498]])
