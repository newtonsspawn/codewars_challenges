from unittest import TestCase

from listposition import listPosition


class TestListPosition(TestCase):
    
    def test_listposition_01(self):
        self.assertEqual(listPosition('A'), 1)
    
    def test_listposition_02(self):
        self.assertEqual(listPosition('ABAB'), 2)
    
    def test_listposition_03(self):
        self.assertEqual(listPosition('AAAB'), 1)
    
    def test_listposition_04(self):
        self.assertEqual(listPosition('BAAA'), 4)
    
    def test_listposition_05(self):
        self.assertEqual(listPosition('QUESTION'), 24572)
    
    def test_listposition_06(self):
        self.assertEqual(listPosition('BOOKKEEPER'), 10743)
    
    def test_listposition_07(self):
        self.assertEqual(listPosition('IMMUNOELECTROPHORETICALLY'),
                         718393983731145698173)
    
    def test_listposition_08(self):
        self.assertEqual(listPosition('CRKUUCXRCKJAKPLFTPJILAZCA'),
                         135033625816460679822)
    
    def test_listposition_09(self):
        self.assertEqual(listPosition('CJFOADIYFYBQEUYGDAMLXEKA'),
                         407545408717707663214)
    
    def test_listposition_10(self):
        self.assertEqual(listPosition('DNHJXGNPQUA'), 2635354)
    
    def test_listposition_11(self):
        self.assertEqual(listPosition('QSSIFTRZCJ'), 853409)
    
    def test_listposition_12(self):
        self.assertEqual(listPosition('E'), 1)
    
    def test_listposition_13(self):
        self.assertEqual(listPosition('WJIOISIDLHN'), 6380331)
    
    def test_listposition_14(self):
        self.assertEqual(listPosition('DJIKYBQPOQ'), 224949)
    
    def test_listposition_15(self):
        self.assertEqual(listPosition('YWJALSWWZXMBJHYQO'), 13360924797870)
    
    def test_listposition_16(self):
        self.assertEqual(listPosition('UDMWDZXYMVKCZOMGQFATVLR'),
                         354319087611892810457)
    
    def test_listposition_17(self):
        self.assertEqual(listPosition('ZGFVOOBWONLDQPIWSGDLR'),
                         512438582776399903)
