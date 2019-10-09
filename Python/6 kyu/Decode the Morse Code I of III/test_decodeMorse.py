from unittest import TestCase

from decodemorse import decodeMorse


class TestDecodeMorse(TestCase):
    
    def test_decodeMorse_01(self):
        self.assertEqual(decodeMorse(".... . -.--   .--- ..- -.. ."),
                         'HEY JUDE')
    
    def test_decodeMorse_02(self):
        self.assertEqual(decodeMorse(".-"), 'A')
    
    def test_decodeMorse_03(self):
        self.assertEqual(decodeMorse("."), 'E')
    
    def test_decodeMorse_04(self):
        self.assertEqual(decodeMorse(".."), 'I')
    
    def test_decodeMorse_05(self):
        self.assertEqual(decodeMorse(". ."), 'EE')
    
    def test_decodeMorse_06(self):
        self.assertEqual(decodeMorse(".   ."), 'E E')
    
    def test_decodeMorse_07(self):
        self.assertEqual(decodeMorse("...---..."), 'SOS')
    
    def test_decodeMorse_08(self):
        self.assertEqual(decodeMorse("... --- ..."), 'SOS')
    
    def test_decodeMorse_09(self):
        self.assertEqual(decodeMorse("...   ---   ..."), 'S O S')
    
    def test_decodeMorse_10(self):
        self.assertEqual(decodeMorse(" . "), 'E')
    
    def test_decodeMorse_11(self):
        self.assertEqual(decodeMorse("   .   . "), 'E E')
    
    def test_decodeMorse_12(self):
        self.assertEqual(decodeMorse(
            "      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... "
            ".-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- "
            ". .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  "),
                         'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')
