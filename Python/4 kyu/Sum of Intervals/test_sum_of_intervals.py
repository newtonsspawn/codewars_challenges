from unittest import TestCase

from sumofintervals import sum_of_intervals


class TestSumOfIntervals(TestCase):
    
    def test_sum_of_intervals_01(self):
        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
    
    def test_sum_of_intervals_02(self):
        self.assertEqual(sum_of_intervals([(1, 5), (3, 6)]), 5)
    
    def test_sum_of_intervals_07(self):
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
    
    def test_sum_of_intervals_08(self):
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)
    
    def test_sum_of_intervals_09(self):
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
    
    def test_sum_of_intervals_10(self):
        self.assertEqual(sum_of_intervals(
                [(166, 258), (-63, -55), (161, 229), (-256, -179)]), 182)
    
    def test_sum_of_intervals_11(self):
        self.assertEqual(sum_of_intervals(
                [(-201, 204), (-31, 77), (315, 475), (-229, 397), (-457, -442),
                 (-144, 280), (-332, -35)]), 822)
    
    def test_sum_of_intervals_12(self):
        self.assertEqual(sum_of_intervals(
                [(228, 251), (-441, -131), (411, 417), (482, 485), (22, 349),
                 (91, 162), (-193, 88), (114, 204), (-148, -97), (-327, 417),
                 (-269, -256), (375, 499), (84, 166), (-87, 162), (51, 350),
                 (101, 286), (38, 112), (145, 498), (37, 474), (-326, -231)]),
                         940)
    
    def test_sum_of_intervals_13(self):
        self.assertEqual(sum_of_intervals([(253, 442)]), 189)
    
    def test_sum_of_intervals_14(self):
        self.assertEqual(sum_of_intervals(
                [(257, 265), (-325, 394), (191, 289), (300, 479), (326, 417),
                 (-154, 309), (-500, 12)]), 979)
    
    def test_sum_of_intervals_15(self):
        self.assertEqual(sum_of_intervals(
                [(-66, 73), (239, 417), (-154, 98), (-65, 419), (375, 465),
                 (24, 270), (-301, -167), (-277, 318), (308, 460)]), 766)
    
    def test_sum_of_intervals_16(self):
        self.assertEqual(sum_of_intervals(
                [(-381, -351), (112, 491), (26, 259), (120, 259), (-192, 226),
                 (-223, 495), (58, 132), (-291, 350), (-46, 499), (-272, 438),
                 (383, 454), (-148, 193), (60, 353), (-475, -210), (-190, 421),
                 (-230, -228), (-39, 156), (257, 425), (-266, 191)]), 974)
    
    def test_sum_of_intervals_17(self):
        self.assertEqual(sum_of_intervals(
                [(342, 418), (-232, 458), (-72, 304), (120, 371), (311, 410),
                 (6, 36), (484, 492), (-139, 123), (270, 430), (174, 437),
                 (153, 221), (241, 485), (-341, 335), (-434, -146),
                 (134, 378)]), 926)
    
    def test_sum_of_intervals_18(self):
        self.assertEqual(sum_of_intervals(
                [(314, 445), (492, 499), (367, 402), (114, 381), (-76, 39),
                 (167, 202), (-18, 209), (482, 500), (-195, 29), (133, 251),
                 (-434, 179), (-113, 7), (-17, 324), (332, 369), (-427, 99),
                 (437, 442), (380, 405)]), 897)
    
    def test_sum_of_intervals_19(self):
        self.assertEqual(sum_of_intervals(
                [(-205, 340), (232, 458), (205, 304), (-248, -236), (-400, 291),
                 (481, 497), (31, 104), (30, 283), (251, 364)]), 874)
    
    def test_sum_of_intervals_20(self):
        self.assertEqual(
            sum_of_intervals([(-212, -14), (489, 498), (66, 371), (414, 464)]),
            562)
    
    def test_sum_of_intervals_21(self):
        self.assertEqual(sum_of_intervals(
                [(-401, 167), (265, 475), (-159, 233), (419, 484), (442, 475),
                 (413, 470), (-21, 98), (-72, -1), (-457, -181), (66, 207)]),
                         909)
    
    def test_sum_of_intervals_22(self):
        self.assertEqual(sum_of_intervals(
                [(-237, 493), (128, 307), (-62, 117), (-170, 299)]), 730)
    
    def test_sum_of_intervals_23(self):
        self.assertEqual(sum_of_intervals(
                [(10, 177), (223, 429), (14, 382), (15, 273), (497, 500),
                 (25, 130), (-197, -73), (420, 470), (-385, 242), (-29, 451),
                 (147, 343), (-149, -52), (202, 468), (257, 289), (-258, 0),
                 (330, 371), (62, 310), (-453, -231)]), 926)
    
    def test_sum_of_intervals_24(self):
        self.assertEqual(sum_of_intervals(
                [(197, 233), (-101, 48), (335, 405), (359, 414), (360, 438),
                 (-484, -27), (-498, -442)]), 685)
    
    def test_sum_of_intervals_25(self):
        self.assertEqual(sum_of_intervals(
                [(-81, -70), (-162, 235), (175, 452), (25, 143), (-10, 321),
                 (-204, 231), (414, 453), (91, 121), (52, 360), (-187, -90),
                 (-399, -292), (94, 312), (-188, 267), (29, 131), (-51, 239),
                 (-194, -144), (-342, 157), (-367, 18), (-324, 388)]), 852)
    
    def test_sum_of_intervals_26(self):
        self.assertEqual(sum_of_intervals(
                [(354, 366), (-253, 69), (-220, 225), (-47, 232), (-379, 13)]),
                         623)
    
    def test_sum_of_intervals_27(self):
        self.assertEqual(sum_of_intervals(
                [(317, 348), (455, 483), (-414, -127), (-311, 461)]), 897)
    
    def test_sum_of_intervals_28(self):
        self.assertEqual(sum_of_intervals(
                [(-35, 102), (-238, -195), (-164, 473), (-129, 205), (-16, 30),
                 (-355, -66), (247, 429)]), 828)
    
    def test_sum_of_intervals_29(self):
        self.assertEqual(sum_of_intervals(
                [(-11, 454), (21, 397), (-410, -35), (-234, 232), (178, 313),
                 (114, 247), (-33, 200), (98, 444), (469, 484), (-476, 79),
                 (371, 498), (-462, 466), (-59, 233), (311, 446), (250, 365),
                 (367, 483), (-173, 136)]), 974)
    
    def test_sum_of_intervals_30(self):
        self.assertEqual(sum_of_intervals(
                [(420, 461), (392, 474), (-13, 474), (30, 313), (440, 458),
                 (-60, 33), (203, 467), (-132, -88), (-465, 173), (337, 412),
                 (355, 444), (152, 368)]), 939)
    
    def test_sum_of_intervals_31(self):
        self.assertEqual(sum_of_intervals(
                [(-358, 252), (-247, -3), (-380, 42), (-482, -87), (407, 460)]),
                         787)
    
    def test_sum_of_intervals_32(self):
        self.assertEqual(sum_of_intervals(
                [(200, 239), (259, 321), (-296, 443), (-338, 130), (-419, -217),
                 (123, 300), (-112, 364), (-168, 305), (-116, 279), (-284, -47),
                 (-246, 71), (-421, 475), (-53, 148)]), 896)
    
    def test_sum_of_intervals_33(self):
        self.assertEqual(sum_of_intervals(
                [(119, 500), (192, 218), (183, 234), (-464, 329), (-86, 11),
                 (8, 413), (-134, -35), (-331, -292), (-2, 57), (277, 396),
                 (160, 188), (249, 467), (-298, -23), (205, 242), (-325, 434)]),
                         964)
    
    def test_sum_of_intervals_34(self):
        self.assertEqual(sum_of_intervals(
                [(-146, 14), (-223, -92), (-152, 270), (-213, 230), (-482, 147),
                 (-331, 113), (184, 199), (178, 407), (127, 375), (168, 397),
                 (-231, -159), (-192, -58), (-255, -1), (163, 286), (403, 492),
                 (396, 478)]), 974)
    
    def test_sum_of_intervals_35(self):
        self.assertEqual(sum_of_intervals(
                [(-288, -32), (399, 499), (324, 363), (-201, 357), (481, 489),
                 (-185, 458), (-281, -93), (495, 497), (-35, 165), (-133, 134),
                 (345, 473), (145, 147)]), 787)
    
    def test_sum_of_intervals_36(self):
        self.assertEqual(sum_of_intervals(
                [(-41, 493), (468, 482), (221, 274), (-497, -421), (-381, 305),
                 (-122, 356), (-169, 233), (243, 462), (-264, -196),
                 (407, 480)]), 950)
