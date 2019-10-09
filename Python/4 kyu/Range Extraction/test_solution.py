from unittest import TestCase

from solution_re import solution


class TestSolution(TestCase):
    
    def test_solution_01(self):
        self.assertEqual(solution(
                [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18,
                 19, 20]), '-6,-3-1,3-5,7-11,14,15,17-20')
    
    def test_solution_02(self):
        self.assertEqual(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]),
                         '-3--1,2,10,15,16,18-20')
    
    def test_solution_03(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), '1-5')
    
    def test_solution_04(self):
        self.assertEqual(solution(
                [-94, -93, -91, -88, -86, -84, -83, -80, -78, -75, -72, -70,
                 -67, -65, -63, -60, -59, -57, -55, -54, -52, -50, -48, -46,
                 -45, -43, -41, -38]),
                '-94,-93,-91,-88,-86,-84,-83,-80,-78,-75,-72,-70,'
                '-67,-65,-63,-60,-59,-57,-55,-54,-52,-50,-48,-46,'
                '-45,-43,-41,-38')
    
    def test_solution_05(self):
        self.assertEqual(solution(
                [-64, -61, -60, -59, -57, -55, -54, -53, -51, -49, -47, -46,
                 -43, -42, -41, -40, -39, -38, -36, -34, -31, -28, -27, -25,
                 -23, -21, -18]),
                '-64,-61--59,-57,-55--53,-51,-49,-47,-46,-43--38,'
                '-36,-34,-31,-28,-27,-25,-23,-21,-18')
    
    def test_solution_06(self):
        self.assertEqual(solution(
                [-52, -49, -46, -45, -42, -39, -36, -34, -32, -31, -28, -26,
                 -24, -23, -22, -19, -16, -13, -12, -9, -6, -4, -2, -1, 2]),
                '-52,-49,-46,-45,-42,-39,-36,-34,-32,-31,-28,-26,'
                '-24--22,-19,-16,-13,-12,-9,-6,-4,-2,-1,2')
    
    def test_solution_07(self):
        self.assertEqual(solution(
                [-93, -90, -88, -85, -82, -80, -79, -77, -75, -74, -71, -69,
                 -67, -66, -63, -61, -59, -57, -56, -54, -52, -51, -48, -47,
                 -45, -44, -42, -40]),
                '-93,-90,-88,-85,-82,-80,-79,-77,-75,-74,-71,-69,'
                '-67,-66,-63,-61,-59,-57,-56,-54,-52,-51,-48,-47,'
                '-45,-44,-42,-40')
    
    def test_solution_08(self):
        self.assertEqual(solution(
                [-84, -83, -82, -79, -76, -75, -74, -71, -70, -69, -67, -66,
                 -63, -61, -60, -57, -55, -52, -50, -47, -45, -43, -41, -39,
                 -36, -33, -30, -27, -24, -23, -22]),
                '-84--82,-79,-76--74,-71--69,-67,-66,-63,-61,-60,'
                '-57,-55,-52,-50,-47,-45,-43,-41,-39,-36,-33,-30,'
                '-27,-24--22')
    
    def test_solution_09(self):
        self.assertEqual(solution(
                [-52, -50, -49, -46, -44, -41, -39, -37, -35, -34, -33, -31,
                 -29, -27, -25, -23, -22, -21, -20]),
                '-52,-50,-49,-46,-44,-41,-39,-37,-35--33,-31,-29,'
                '-27,-25,-23--20')
    
    def test_solution_10(self):
        self.assertEqual(solution(
                [-62, -59, -57, -55, -54, -51, -50, -48, -47, -44, -43, -41]),
                '-62,-59,-57,-55,-54,-51,-50,-48,-47,-44,-43,-41')
    
    def test_solution_11(self):
        self.assertEqual(solution(
                [-87, -86, -83, -80, -79, -77, -76, -75, -73, -72, -69, -67,
                 -64, -61, -60, -58, -55, -54, -51, -50, -49, -48, -45, -42,
                 -39, -38, -35, -32, -29]),
                '-87,-86,-83,-80,-79,-77--75,-73,-72,-69,-67,-64,'
                '-61,-60,-58,-55,-54,-51--48,-45,-42,-39,-38,-35,'
                '-32,-29')
    
    def test_solution_12(self):
        self.assertEqual(solution(
                [-55, -53, -52, -51, -49, -47, -44, -42, -41, -40, -39, -38,
                 -37, -35, -32, -30, -29, -26]),
                '-55,-53--51,-49,-47,-44,-42--37,-35,-32,-30,-29,-26')
    
    def test_solution_13(self):
        self.assertEqual(
                solution([-76, -73, -71, -70, -67, -66, -64, -62, -61, -60,
                          -59]),
                '-76,-73,-71,-70,-67,-66,-64,-62--59')
    
    def test_solution_14(self):
        self.assertEqual(solution(
                [-63, -60, -58, -55, -52, -49, -47, -46, -45, -42, -39, -38,
                 -35, -34, -31, -28, -26, -24, -22]),
                '-63,-60,-58,-55,-52,-49,-47--45,-42,-39,-38,-35,'
                '-34,-31,-28,-26,-24,-22')
    
    def test_solution_15(self):
        self.assertEqual(solution(
                [-83, -81, -79, -76, -75, -72, -69, -68, -66, -63, -62, -59,
                 -56, -55, -52, -49, -46, -43, -41, -39, -36, -34, -31, -30,
                 -29]),
                '-83,-81,-79,-76,-75,-72,-69,-68,-66,-63,-62,-59,'
                '-56,-55,-52,-49,-46,-43,-41,-39,-36,-34,-31--29')
    
    def test_solution_16(self):
        self.assertEqual(solution(
                [-94, -92, -90, -88, -87, -85, -83, -81, -78, -77, -76, -75,
                 -73, -71, -69, -66, -64, -62, -59, -56, -54]),
                '-94,-92,-90,-88,-87,-85,-83,-81,-78--75,-73,-71,'
                '-69,-66,-64,-62,-59,-56,-54')
    
    def test_solution_17(self):
        self.assertEqual(solution(
                [-98, -96, -93, -92, -91, -88, -85, -83, -81, -79, -77, -74,
                 -73, -72, -71, -69, -68]),
                '-98,-96,-93--91,-88,-85,-83,-81,-79,-77,-74--71,'
                '-69,-68')
    
    def test_solution_18(self):
        self.assertEqual(solution(
                [-60, -57, -55, -53, -50, -49, -48, -45, -42, -40, -38, -36,
                 -34, -33, -32, -30, -28, -25]),
                '-60,-57,-55,-53,-50--48,-45,-42,-40,-38,-36,'
                '-34--32,-30,-28,-25')
    
    def test_solution_19(self):
        self.assertEqual(solution(
                [-78, -75, -73, -72, -70, -68, -65, -64, -63, -62, -59, -56,
                 -54, -53, -51, -48, -45, -43, -40, -39, -38]),
                '-78,-75,-73,-72,-70,-68,-65--62,-59,-56,-54,-53,-51,-48,-45,'
                '-43,-40--38')
    
    def test_solution_20(self):
        self.assertEqual(solution(
                [-99, -97, -95, -92, -89, -88, -85, -82, -81, -80, -79, -77,
                 -76, -74, -73, -71, -70, -68, -65, -62, -60, -59, -58, -57,
                 -56, -53, -52]),
                '-99,-97,-95,-92,-89,-88,-85,-82--79,-77,-76,-74,-73,-71,-70,'
                '-68,-65,-62,-60--56,-53,-52')
    
    def test_solution_21(self):
        self.assertEqual(solution(
                [-92, -90, -89, -87, -85, -82, -79, -78, -77, -74, -71, -69,
                 -66, -64, -63, -60, -59, -57, -56, -53, -50]),
                '-92,-90,-89,-87,-85,-82,-79--77,-74,-71,-69,-66,-64,-63,-60,'
                '-59,-57,-56,-53,-50')
    
    def test_solution_22(self):
        self.assertEqual(solution(
                [-56, -55, -54, -51, -48, -45, -43, -41, -40, -39, -36, -34,
                 -31, -30, -28]),
                '-56--54,-51,-48,-45,-43,-41--39,-36,-34,-31,-30,-28')
    
    def test_solution_23(self):
        self.assertEqual(solution(
                [-72, -71, -68, -65, -63, -62, -61, -58, -55, -54, -51, -49,
                 -47, -45, -44, -41, -39, -36, -34]),
                '-72,-71,-68,-65,-63--61,-58,-55,-54,-51,-49,-47,-45,-44,-41,'
                '-39,-36,-34')
