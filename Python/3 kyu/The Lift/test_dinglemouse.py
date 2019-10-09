from unittest import TestCase

from dinglemouse import Dinglemouse


class TestDinglemouse(TestCase):
    
    def test_thelift_01(self):
        lift = Dinglemouse(((), (), (5, 5, 5), (), (), (), ()), 5)
        self.assertEqual(lift.theLift(), [0, 2, 5, 0])
    
    def test_thelift_02(self):
        lift = Dinglemouse(((), (), (1, 1), (), (), (), ()), 5)
        self.assertEqual(lift.theLift(), [0, 2, 1, 0])
    
    def test_thelift_03(self):
        lift = Dinglemouse(((), (3,), (4,), (), (5,), (), ()), 5)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 4, 5, 0])
    
    def test_thelift_04(self):
        lift = Dinglemouse(((), (0,), (), (), (2,), (3,), ()), 5)
        self.assertEqual(lift.theLift(), [0, 5, 4, 3, 2, 1, 0])
    
    def test_thelift_05(self):
        lift = Dinglemouse(((3,), (2,), (0,), (2,), (), (), (5,)), 5)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 6, 5, 3, 2, 0])
    
    def test_thelift_06(self):
        lift = Dinglemouse(((), (), (4, 4, 4, 4), (), (2, 2, 2, 2), (), ()),
                           2)
        self.assertEqual(lift.theLift(), [0, 2, 4, 2, 4, 2, 0])
    
    def test_thelift_07(self):
        lift = Dinglemouse(((1, 2, 3, 4), (), (), (), (), (), ()), 5)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 4, 0])
    
    def test_thelift_08(self):
        lift = Dinglemouse(((3, 3, 3, 3, 3, 3), (), (), (), (), (), ()), 5)
        self.assertEqual(lift.theLift(), [0, 3, 0, 3, 0])
    
    def test_thelift_09(self):
        lift = Dinglemouse(
                ((), (), (), (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (), (), ()),
                5)
        self.assertEqual(lift.theLift(), [0, 3, 1, 3, 1, 3, 1, 0])
    
    def test_thelift_10(self):
        lift = Dinglemouse(
                ((3, 3, 3, 3, 3, 3), (), (), (), (), (4, 4, 4, 4, 4, 4), ()),
                5)
        self.assertEqual(lift.theLift(), [0, 3, 5, 4, 0, 3, 5, 4, 0])
    
    def test_thelift_11(self):
        lift = Dinglemouse(
                ((), (0, 0, 0, 6), (), (), (), (6, 6, 0, 0, 0, 6), ()), 5)
        self.assertEqual(lift.theLift(), [0, 1, 5, 6, 5, 1, 0, 1, 0])
    
    def test_thelift_12(self):
        lift = Dinglemouse(((), (2,), (3, 3, 3), (1,), (), (), ()), 1)
        self.assertEqual(lift.theLift(), [0, 1, 2, 3, 1, 2, 3, 2, 3, 0])
    
    def test_thelift_13(self):
        lift = Dinglemouse((
                (), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
                (0, 0, 0, 0), (0, 0, 0, 0)), 5)
        self.assertEqual(lift.theLift(),
                         [0, 6, 5, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 0, 4, 3, 2, 1,
                          0, 3, 2, 1, 0, 1, 0])
    
    def test_thelift_14(self):
        lift = Dinglemouse(((), (), (), (), (), (), ()), 5)
        self.assertEqual(lift.theLift(), [0])
    
    def test_thelift_15(self):
        lift = Dinglemouse((
                (2, 1, 2, 6, 5), (4,), (6, 0, 6, 6), (2, 5, 1, 5), (5, 2),
                (1, 0, 2, 6, 0), (0,)), 2)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 2, 3, 6, 5, 4,
                          3, 2, 0, 2, 3, 5, 6, 5, 4, 3, 2, 0, 3, 5, 3, 2, 1, 0])
    
    def test_thelift_16(self):
        lift = Dinglemouse((
                (2,), (4, 14, 10), (4,), (5, 1, 1, 2, 8), (), (),
                (4, 14, 8, 8, 4),
                (12, 5), (9,), (), (), (0, 3), (5,), (6,), (12, 5)), 1)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 6, 7, 8, 14, 13, 12, 11, 7, 6, 5, 3, 1,
                          3, 4, 6, 7, 8, 9, 14, 13, 11, 7, 6, 5, 3, 1, 3, 6, 7,
                          14, 13, 11, 7, 6, 4, 3, 2, 1, 3, 6, 7, 10, 11, 7, 6,
                          0, 3, 5, 6, 7, 8, 11, 7, 6, 3, 7, 8, 7, 6, 5, 7, 12,
                          6, 4, 0])
    
    def test_thelift_17(self):
        lift = Dinglemouse((
                (2,), (0, 5, 9, 2, 5), (5, 3, 0, 11), (2,), (14,),
                (0, 13, 0, 0, 1),
                (7,), (), (), (), (1,), (4, 0, 10), (10, 7, 2, 14, 4), (),
                (8, 11, 6)),
                4)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 6, 7, 9, 12, 13, 14, 12, 11, 10, 8,
                          6, 5, 4, 3, 2, 1, 0, 1, 2, 5, 11, 12, 11, 7, 5, 4, 2,
                          0, 11, 10, 5, 1, 0])
    
    def test_thelift_18(self):
        lift = Dinglemouse((
                (), (8, 3, 11, 12), (9,), (), (), (), (), (10,),
                (6, 14, 9, 15, 3),
                (5, 5, 12, 5), (5, 15, 12, 4), (), (3, 15, 14, 9), (8, 5), (9,),
                (7,)),
                2)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 7, 8, 9, 10, 12, 14, 15, 14, 13, 12, 10,
                          9, 8, 7, 5, 1, 2, 8, 9, 10, 11, 12, 14, 15, 13, 12,
                          10, 9, 8, 6, 5, 2, 8, 9, 10, 12, 10, 9, 8, 5, 3, 8,
                          15, 10, 9, 8, 5, 4, 9, 8, 5, 3, 0])
    
    def test_thelift_19(self):
        lift = Dinglemouse((
                (16, 1, 10), (14, 11, 3, 15), (4, 7, 10), (11, 8, 15),
                (1, 3, 0, 7),
                (2, 8, 11, 4), (11, 14, 16), (13, 2, 13), (16, 9, 0), (0,),
                (14,), (5,),
                (0, 14, 7, 5, 9), (14, 11, 11), (), (10, 12), (4, 10)), 3)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 16, 15, 13,
                          12, 11, 10, 9, 8, 7, 5, 4, 1, 0, 1, 2, 3, 4, 5, 6, 7,
                          8, 11, 12, 13, 14, 15, 13, 12, 11, 7, 5, 4, 2, 0, 2,
                          3, 4, 5, 6, 7, 8, 10, 13, 12, 9, 7, 5, 4, 3, 0, 3, 5,
                          6, 8, 9, 15, 16, 5, 6, 11, 14, 6, 16, 0])
    
    def test_thelift_20(self):
        lift = Dinglemouse((
                (11, 13, 7, 7), (18,), (0, 4, 6, 1), (18, 17, 17, 7),
                (6, 15, 6),
                (3, 11, 16, 10, 8), (), (), (1, 10), (10,), (17, 14, 16), (14,),
                (2, 7, 14, 17, 0), (12,), (2, 9, 9, 12, 4), (13, 3, 11), (4,),
                (0, 11, 6), (8, 2)), 3)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 17, 18,
                          17, 16, 15, 14, 13, 12, 8, 5, 2, 1, 0, 1, 2, 3, 4, 5,
                          6, 7, 9, 10, 12, 14, 16, 18, 17, 16, 15, 14, 13, 12,
                          11, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 12, 14, 17, 18,
                          15, 14, 13, 12, 11, 3, 2, 3, 4, 5, 7, 12, 15, 17, 14,
                          12, 9, 2, 4, 5, 6, 11, 16, 14, 12, 7, 4, 0, 5, 8, 10,
                          0])
    
    def test_thelift_21(self):
        lift = Dinglemouse((
                (6, 7), (), (4, 5), (5,), (0, 5, 0, 1, 7), (2, 1, 4, 3, 0),
                (1, 4, 0),
                (3, 2)), 3)
        self.assertEqual(lift.theLift(),
                         [0, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 7,
                          6, 5, 4, 2, 0, 5, 4, 3, 1, 0, 5, 4, 1, 0])
    
    def test_thelift_22(self):
        lift = Dinglemouse(
                ((1, 1, 1, 1), (2, 4, 0, 3, 3), (3, 4, 3), (2, 4), ()), 3)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 0])
    
    def test_thelift_23(self):
        lift = Dinglemouse(
                ((3, 3, 4, 1), (3, 0), (3, 3, 0, 1), (1, 2, 0, 1, 2), (3,)),
                3)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0])
    
    def test_thelift_24(self):
        lift = Dinglemouse(((1, 1, 1), (0,)), 3)
        self.assertEqual(lift.theLift(), [0, 1, 0])
    
    def test_thelift_25(self):
        lift = Dinglemouse(((), (), (3,), (), ()), 1)
        self.assertEqual(lift.theLift(), [0, 2, 3, 0])
    
    def test_thelift_26(self):
        lift = Dinglemouse((
                (11, 3, 9, 7, 2), (6, 4, 9), (), (11, 10, 9), (5, 7, 6),
                (3, 10, 4, 7),
                (), (9, 5, 1, 5, 10), (6, 11, 10, 2), (3, 3, 5), (7, 4, 3),
                (3, 9, 7, 4, 8)), 5)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 10, 9, 8, 7, 6, 5,
                          4, 3, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 8, 7, 5,
                          4, 3, 1, 4, 5, 6, 7, 8, 10, 8, 7, 5, 2, 0])
    
    def test_thelift_27(self):
        lift = Dinglemouse((
                (8, 5, 6, 4, 6), (3,), (7, 8, 5), (4,), (6, 5), (1, 3), (1, 4),
                (),
                ()), 1)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 8, 6, 5, 1, 0, 1, 2, 3, 4, 5, 6, 5, 4,
                          0, 1, 2, 3, 4, 6, 5, 1, 0, 1, 2, 3, 4, 6, 5, 3, 0, 1,
                          2, 3, 4, 6, 1, 2, 3, 4, 5, 2, 7, 2, 8, 2, 5, 0])
    
    def test_thelift_28(self):
        lift = Dinglemouse(((1,), (0, 0, 2), (0,)), 4)
        self.assertEqual(lift.theLift(), [0, 1, 2, 1, 0])
    
    def test_thelift_29(self):
        lift = Dinglemouse((
                (12,), (8, 2, 10, 3, 10), (4, 11, 9, 3), (1, 12),
                (11, 8, 10, 9),
                (3, 10, 1, 2, 0), (3, 9, 11), (11, 3, 10), (2, 2, 1),
                (0, 5, 6, 1), (),
                (3, 10, 6, 3), (3, 10, 8, 7)), 5)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 11, 10, 9, 8,
                          7, 6, 5, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                          11, 10, 9, 8, 6, 5, 3, 1, 4, 5, 6, 7, 9, 10, 11, 8, 5,
                          2, 1, 0, 7, 10, 0])
    
    def test_thelift_30(self):
        lift = Dinglemouse((
                (6, 5, 7, 6, 4), (7,), (6, 0), (8,), (1, 9, 2, 5, 9),
                (9, 10, 0), (),
                (), (2, 6, 10, 7), (3,), (6, 1, 2, 7)), 4)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 5, 4, 2,
                          1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 4, 3, 2, 4,
                          5, 9, 10, 0])
    
    def test_thelift_31(self):
        lift = Dinglemouse((
                (6, 11, 2, 2), (14, 12, 8, 10, 0), (12, 11, 5, 8), (6, 13, 2),
                (),
                (10, 3, 3, 1), (), (12, 12, 12), (14, 6), (13, 7, 1), (2, 7),
                (3, 1),
                (), (3, 11, 1, 3), (11, 3, 4, 0, 8)), 4)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 14, 13, 11, 10, 9,
                          8, 5, 4, 3, 2, 1, 0, 1, 2, 3, 5, 7, 8, 9, 10, 12, 14,
                          13, 11, 10, 9, 8, 6, 5, 3, 1, 2, 3, 5, 6, 7, 8, 9, 10,
                          12, 13, 10, 9, 7, 5, 3, 2, 1, 7, 12, 9, 1, 0])
    
    def test_thelift_32(self):
        lift = Dinglemouse((
                (8, 9, 11, 8), (7, 4), (), (), (11, 8), (10, 10, 6, 11),
                (1, 0, 8),
                (10, 4), (10,), (6, 11, 5, 5), (5, 4, 9, 7), (4, 3, 2, 0, 10)),
                5)
        self.assertEqual(lift.theLift(),
                         [0, 1, 4, 5, 6, 7, 8, 9, 10, 11, 10, 9, 7, 6, 5, 4, 3,
                          2, 0, 1, 4, 5, 6, 8, 10, 11, 10, 9, 7, 6, 5, 4, 1, 5,
                          11, 6, 0])
    
    def test_thelift_33(self):
        lift = Dinglemouse(((3,), (), (), (4, 0), (), (6,), (1,), (3, 1)), 4)
        self.assertEqual(lift.theLift(), [0, 3, 4, 5, 6, 7, 6, 3, 1, 0])
    
    def test_thelift_34(self):
        lift = Dinglemouse((
                (1, 3, 2, 1, 3), (3,), (5, 5), (5, 2, 2), (0, 3, 1, 5), (1,)),
                3)
        self.assertEqual(lift.theLift(),
                         [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0, 1, 2, 3, 5, 4, 3, 2,
                          1, 0])
