from unittest import TestCase

from selectsubarray import select_subarray


class TestSelectSubarray(TestCase):
    
    def test_select_subarray_01(self):
        self.assertEqual(select_subarray([1, 23, 2, -8, 5]),
                         [3, -8])
    
    def test_select_subarray_02(self):
        self.assertEqual(select_subarray([1, 3, 23, 4, 2, -8, 5, 18]),
                         [2, 23])

    def test_select_subarray_03(self):
        self.assertEqual(select_subarray([10, 20, -30, 100, 200]),
                         [[3, 100], [4, 200]])

    def test_select_subarray_04(self):
        self.assertEqual(select_subarray([128, 64, 134, -120, 137, -118, 139,
                                          142, 143, 16, -106, 23, -101, 156,
                                          30, 159, 32, 34, 35, 198, -179, 41,
                                          -165, -85, -82, 50, 181, -73, -200,
                                          58, -197, 188, 61, -194, -193, -64,
                                          193, 194, -61, -113, -186, 73, -9,
                                          77, -96, 80, -47, -174, 163, -170,
                                          87, -168, 89, 91, -34, -31, -158,
                                          -29, 38, -183, 81, -152, -151, -146,
                                          113, 83, -12, 117, 119, -136, -133,
                                          -132, 170]),
                         [19, 198])
    
    def test_select_subarray_05(self):
        self.assertEqual(select_subarray([135, -20, 139, 15, 144, 150, -39,
                                          -103, 155, 156, -99, -92, -89, 40,
                                          170, -84, -142, -82, -81, -79, 179,
                                          52, 55, 184, -199, -69, -66, 64, -63,
                                          66, -60, -59, -185, 76, 79, -72, 82,
                                          -42, -168, 36, 90, 91, -35, 103, 104,
                                          -21, 108, -147, -167, -143, 114,
                                          -141, 62, -136, 122, -5, 126]),
                         [24, -199])
