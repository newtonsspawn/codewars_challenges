from unittest import TestCase

from calc import calc


class TestCalc(TestCase):
    
    def test_calc_001(self):
        self.assertEqual(calc('2 + 3 * 4 / 3 - 6 / 3 * 3 + 8'), 8)
    
    def test_calc_002(self):
        self.assertEqual(calc('1 + 2 * 3 * 3 - 8'), 11)
    
    def test_calc_003(self):
        self.assertEqual(calc('1 + 2 * 3 * (5 - 2) - 8'), 11)
    
    def test_calc_004(self):
        self.assertEqual(calc('1 + 2 * 3 * (5 - (3 - 1)) - 8'), 11)
    
    def test_calc_005(self):
        self.assertEqual(calc('4 + -(1)'), 3)
    
    def test_calc_006(self):
        self.assertEqual(calc('4 - -(1)'), 5)
    
    def test_calc_007(self):
        self.assertEqual(calc('4 * -(1)'), -4)
    
    def test_calc_008(self):
        self.assertEqual(calc('4 / -(1)'), -4)
    
    def test_calc_009(self):
        self.assertEqual(calc('-1'), -1)
    
    def test_calc_010(self):
        self.assertEqual(calc('-(-1)'), 1)
    
    def test_calc_011(self):
        self.assertEqual(calc('-(-(-1))'), -1)
    
    def test_calc_012(self):
        self.assertEqual(calc('-(-(-(-1)))'), 1)
    
    def test_calc_013(self):
        self.assertEqual(calc('(((((-1)))))'), -1)
    
    def test_calc_014(self):
        self.assertEqual(calc('5 - 1'), 4)
    
    def test_calc_015(self):
        self.assertEqual(calc('5- 1'), 4)
    
    def test_calc_016(self):
        self.assertEqual(calc('5 -1'), 4)
    
    def test_calc_017(self):
        self.assertEqual(calc('28 + 86 - -4 / 57 - -93 + -48 * -40 / -29'),
                         140.86327888687237)
    
    def test_calc_018(self):
        self.assertEqual(calc('-18 - 96 * 48 + 23 - 2 - 88 / -71 * -33'),
                         -4645.901408450704)
    
    def test_calc_019(self):
        self.assertEqual(calc('49 - -94 / -36 * 94 * 43 * -11 - -26 + 2'),
                         116172.22222222222)
    
    def test_calc_020(self):
        self.assertEqual(calc('-41 - 15 * -56 - 52 - -25 - -8 - -47 + -6'), 821)
    
    def test_calc_021(self):
        self.assertEqual(calc('-66 - 85 - 87 + 15 * -8 + -13 - 37 + -6'), -414)
    
    def test_calc_022(self):
        self.assertEqual(calc('31 + -43 * 38 * -40 / -82 + -62 + -87 / -41'),
                         -825.9512195121952)
    
    def test_calc_023(self):
        self.assertEqual(calc('-74 - 61 / 36 - 18 - 4 - -63 * 16 * -23'),
                         -23281.694444444445)
    
    def test_calc_024(self):
        self.assertEqual(calc('-6 * -10 + -14 - -97 / 33 / -21 / 41 * -15'),
                         46.05120895364798)
    
    def test_calc_025(self):
        self.assertEqual(calc('-84 / -7 * -3 + -31 / 7 * 52 / 27 - -40'),
                         -4.529100529100532)
    
    def test_calc_026(self):
        self.assertEqual(calc('46 + 92 + -34 + 35 / -72 + -2 * 41 + 26'),
                         47.513888888888886)
    
    def test_calc_027(self):
        self.assertEqual(calc('-4 + 89 - -84 + 75 + 50 + -11 - 64 + 22'), 241)
    
    def test_calc_028(self):
        self.assertEqual(calc('-69 * 42 * -25 - -71 + -43 + -73 * 48 - 74'),
                         68900)
    
    def test_calc_029(self):
        self.assertEqual(calc('-70 * -44 * -75 + -38 / 22 * -84 / 2 * -54'),
                         -234917.45454545456)
    
    def test_calc_030(self):
        self.assertEqual(calc('4 - -24 * 79 * -1 * -14 + 62 + 62 - -44'), 26716)
    
    def test_calc_031(self):
        self.assertEqual(calc('31 * 57 * 46 * 90 + -63 - 6 - -54 + -45'),
                         7315320)
    
    def test_calc_032(self):
        self.assertEqual(calc('-69 / 72 + 66 * -9 + -76 - -57 / -98 / -14'),
                         -670.916788143829)
    
    def test_calc_033(self):
        self.assertEqual(calc('-91 - 22 - -53 * 19 + -19 - -16 + 30 - 5'), 916)
    
    def test_calc_034(self):
        self.assertEqual(calc('-40 - -47 * 3 / -2 * -85 - -11 + 76 + -44'),
                         5995.5)
    
    def test_calc_035(self):
        self.assertEqual(calc('82 + -81 * -62 - 41 * -77 - 12 * -23 + -97'),
                         8440)
    
    def test_calc_036(self):
        self.assertEqual(calc('-92 - 38 - 42 + -70 - -95 - 69 - -60 + 76'), -80)
    
    def test_calc_037(self):
        self.assertEqual(calc('72 * -48 * 98 - 65 + -40 / 85 - 58 + 59'),
                         -338752.4705882353)
    
    def test_calc_038(self):
        self.assertEqual(calc('-74 * 45 / 25 - -1 - -66 - -47 * -44 - -37'),
                         -2097.2)
    
    def test_calc_039(self):
        self.assertEqual(calc('-69 / -33 + -58 + 46 + 94 - -51 + 81 + 8'),
                         224.0909090909091)
    
    def test_calc_040(self):
        self.assertEqual(calc('-25 / -5 / -27 + -57 / 8 * 69 * 80 + -64'),
                         -39394.18518518518)
    
    def test_calc_041(self):
        self.assertEqual(calc('8 * -47 + 77 + -98 / -87 / -47 - -91 - 4'),
                         -212.0239667400342)
    
    def test_calc_042(self):
        self.assertEqual(calc('-21 / 31 * -73 / 73 / -93 - 69 * -54 + -97'),
                         3628.9927159209155)
    
    def test_calc_043(self):
        self.assertEqual(calc('41 / -89 / 29 * -55 * 67 / -100 * -41 * -2'),
                         -48.00065865943432)
    
    def test_calc_044(self):
        self.assertEqual(calc('3 + 71 * -31 - 31 + -44 - 94 - 79 - -59'), -2387)
    
    def test_calc_045(self):
        self.assertEqual(calc('-9 - -96 * 80 / 56 + 89 / -43 + -25 + -91'),
                         10.073089700996675)
    
    def test_calc_046(self):
        self.assertEqual(calc('18 + -75 * 79 - 93 * -88 * 48 * 92 - -91'),
                         36134728)
    
    def test_calc_047(self):
        self.assertEqual(calc('-91 - 83 - 42 - -76 + -38 - 15 + 9 + 91'), -93)
    
    def test_calc_048(self):
        self.assertEqual(calc('-52 + -47 * 50 / 84 / -21 / -41 - -51 / -97'),
                         -52.55826586774178)
    
    def test_calc_049(self):
        self.assertEqual(calc('70 + 35 + 7 - -20 / 68 * 82 * 71 - 48'),
                         1776.3529411764705)
    
    def test_calc_050(self):
        self.assertEqual(calc('1 / 81 + 20 * -64 / -2 - -7 / -53 + 18'),
                         657.8802702073142)
    
    def test_calc_051(self):
        self.assertEqual(calc('-63 * 27 / 62 / 81 + -45 - -87 - 83 + -74'),
                         -115.33870967741936)
    
    def test_calc_052(self):
        self.assertEqual(calc('-49 + -75 / 90 - 89 * 40 / 62 / 12 * -50'),
                         189.41397849462365)
    
    def test_calc_053(self):
        self.assertEqual(calc('79 + -28 - -15 + -100 / 56 + 10 - 93 / 97'),
                         73.25552282768777)
    
    def test_calc_054(self):
        self.assertEqual(calc('40 * -29 + 27 * -71 / 11 - -73 + -3 * 65'),
                         -1456.2727272727273)
    
    def test_calc_055(self):
        self.assertEqual(calc('-28 - -33 / 13 * 27 + 30 / 34 + -61 * -73'),
                         4494.420814479638)
    
    def test_calc_056(self):
        self.assertEqual(calc('-49 - 54 / -41 - -64 / 37 - 54 * 69 / -92'),
                         -5.453197099538556)
    
    def test_calc_057(self):
        self.assertEqual(calc('-7 - -7 * -24 * 47 * -76 * 96 * -100 * -55'),
                         316850687993)
    
    def test_calc_058(self):
        self.assertEqual(calc('10 / -55 + -73 / 46 - 30 + 40 - -82 / -19'),
                         3.915435822758477)
    
    def test_calc_059(self):
        self.assertEqual(calc('19 - -93 - 11 + 45 / -17 + -51 / 23 * -22'),
                         147.13554987212277)
    
    def test_calc_060(self):
        self.assertEqual(calc('10 / 11 - -13 / 93 / -4 * -63 / -29 * 12'),
                         -0.001921326726665895)
    
    def test_calc_061(self):
        self.assertEqual(calc('57 * -41 - -65 - -49 - 75 - -37 / 82 - 76'),
                         -2373.548780487805)
    
    def test_calc_062(self):
        self.assertEqual(calc('-50 - -61 + 76 / 44 / 71 * 8 - -82 * -6'),
                         -480.8053777208707)
    
    def test_calc_063(self):
        self.assertEqual(calc('-43 / 98 / 2 * 53 + 4 / 100 - -48 + 53'),
                         89.41244897959183)
    
    def test_calc_064(self):
        self.assertEqual(calc('-46 * -95 - -30 + 66 / 29 * 71 - 78 * 46'),
                         973.5862068965516)
    
    def test_calc_065(self):
        self.assertEqual(calc('-34 + 35 / -35 + -32 / -16 + -26 * 96 * -6'),
                         14943.0)
    
    def test_calc_066(self):
        self.assertEqual(calc('81 + -14 + 42 + -41 + -100 * -89 + -78 * -22'),
                         10684)
    
    def test_calc_067(self):
        self.assertEqual(calc('-29 + -56 - -53 + -46 - 76 / 24 * 22 * -6'),
                         339.99999999999994)
    
    def test_calc_068(self):
        self.assertEqual(calc('-94 + -28 + 35 + 67 + 31 - 21 - 94 - -31'), -73)
    
    def test_calc_069(self):
        self.assertEqual(calc('-96 * -56 / -24 - -42 - 81 + 37 + -9 * 42'),
                         -604.0)
    
    def test_calc_070(self):
        self.assertEqual(calc('17 * 7 * 39 - -35 + 70 * 28 / -83 / -65'),
                         4676.363299351251)
    
    def test_calc_071(self):
        self.assertEqual(calc('-26 * 88 / 91 / 58 + -5 / -45 + -59 / 52'),
                         -1.4570018104500861)
    
    def test_calc_072(self):
        self.assertEqual(calc('-66 * 28 * 32 - -20 - 50 / -52 - 88 + 39'),
                         -59164.03846153846)
    
    def test_calc_073(self):
        self.assertEqual(calc('76 / 32 - 46 * 39 - 35 * 72 / 40 * -54'),
                         1610.375)
    
    def test_calc_074(self):
        self.assertEqual(calc('61 + 81 / 57 * 29 + -52 / 42 * -78 / 46'),
                         104.30990519777706)
    
    def test_calc_075(self):
        self.assertEqual(calc('-32 - 64 - -14 - 44 + 78 * 47 + -81 / -64'),
                         3541.265625)
    
    def test_calc_076(self):
        self.assertEqual(calc('-59 / -54 * 21 + 73 * 52 * 96 - 86 / 77'),
                         364437.82756132755)
    
    def test_calc_077(self):
        self.assertEqual(calc('-93 / -98 + -36 + 20 * 5 - 61 / -51 * 16'),
                         84.08623449379752)
    
    def test_calc_078(self):
        self.assertEqual(calc('12 * 51 + 33 - -7 - -60 * -54 / -88 / 7'),
                         657.2597402597403)
    
    def test_calc_079(self):
        self.assertEqual(calc('1 + -77 - 8 + 73 / -9 - 66 * -37 * 98'),
                         239223.88888888888)
    
    def test_calc_080(self):
        self.assertEqual(calc('15 + 34 - -54 / -7 / -14 - -62 * -64 - 25'),
                         -3943.4489795918366)
    
    def test_calc_081(self):
        self.assertEqual(calc('-9 - 78 * -2 + 93 - -48 * 57 / 87 + 93'),
                         364.44827586206895)
    
    def test_calc_082(self):
        self.assertEqual(calc('16 + -24 - -75 / -7 + 22 * 42 / 37 * -33'),
                         -842.8223938223938)
    
    def test_calc_083(self):
        self.assertEqual(calc('-60 - 68 * 17 - -77 * 31 + 83 / -35 / 18'),
                         1170.868253968254)
    
    def test_calc_084(self):
        self.assertEqual(calc('-36 - -78 * 45 * -69 * 11 - 13 + 88 + -98'),
                         -2664149)
    
    def test_calc_085(self):
        self.assertEqual(calc('71 - -48 / -38 - -97 * 55 - -91 / -22 * -47'),
                         5599.145933014354)
    
    def test_calc_086(self):
        self.assertEqual(calc('-70 + -58 / 20 / -72 + -97 / 42 + -98 * -49'),
                         4729.730753968254)
    
    def test_calc_087(self):
        self.assertEqual(calc('-100 + 93 / 19 - -35 + -57 + -89 + -88 + -82'),
                         -376.10526315789474)
    
    def test_calc_088(self):
        self.assertEqual(calc('52 * -84 + 94 - -64 * -26 / -66 * 3 - -16'),
                         -4182.363636363636)
    
    def test_calc_089(self):
        self.assertEqual(calc('94 + -7 - 70 / 55 - -53 * 87 + 81 + -23'),
                         4754.727272727273)
    
    def test_calc_090(self):
        self.assertEqual(calc('68 * -51 / -40 / -8 * -6 - -89 + 61 * 85'),
                         5339.025)
    
    def test_calc_091(self):
        self.assertEqual(calc('75 + -95 + 85 / 3 * -39 * -88 + -49 - -63'),
                         97234.0)
    
    def test_calc_092(self):
        self.assertEqual(calc('76 / -8 - 48 + -77 / 26 * 93 + -63 / -27'),
                         -330.58974358974365)
    
    def test_calc_093(self):
        self.assertEqual(calc('-24 - -19 + 15 + -61 * 59 * -56 + -28 * 99'),
                         198782)
    
    def test_calc_094(self):
        self.assertEqual(calc('-22 / 50 / 78 + -51 + -8 * 39 / 76 - -64'),
                         8.889095816464234)
    
    def test_calc_095(self):
        self.assertEqual(calc('-41 / -39 - 48 - -98 / 31 - 67 + -48 * 43'),
                         -2174.7874276261373)
    
    def test_calc_096(self):
        self.assertEqual(calc('-13 * -27 - -46 * -99 - -25 - 53 - -41 + 88'),
                         -4102)
    
    def test_calc_097(self):
        self.assertEqual(calc('92 - 81 - 89 + 63 * 51 / -2 + 73 * -66'),
                         -6502.5)
    
    def test_calc_098(self):
        self.assertEqual(calc('-35 / -62 * -43 - 46 + -88 / 38 / -97 + -36'),
                         -106.2503194301017)
    
    def test_calc_099(self):
        self.assertEqual(calc('53 + -84 * -58 / -39 - 82 + -18 * 4 + -95'),
                         -320.9230769230769)
    
    def test_calc_100(self):
        self.assertEqual(calc('-71 - 24 * -19 - 34 + 65 - 89 - -52 - 41'), 338)
    
    def test_calc_101(self):
        self.assertEqual(calc('-62 - -38 - 14 * 54 + -92 * 4 - 70 - 66'), -1284)
    
    def test_calc_102(self):
        self.assertEqual(calc('60 * 82 / 72 + 81 - 65 * 40 * -91 - 7'),
                         236742.33333333334)
    
    def test_calc_103(self):
        self.assertEqual(calc('-91 + 55 - -26 + -48 / -17 - -25 + 28 * -25'),
                         -682.1764705882352)
    
    def test_calc_104(self):
        self.assertEqual(calc('-10 * 15 * -25 * -7 * 99 / 55 * -3 / -1'),
                         -141750.0)
    
    def test_calc_105(self):
        self.assertEqual(calc('-37 - -43 / 21 * -42 / 3 / -47 - -52 / -73'),
                         -37.102399689109106)
    
    def test_calc_106(self):
        self.assertEqual(calc('73 + 38 + 64 * 44 - 6 + 38 * 81 * -25'), -74029)
    
    def test_calc_107(self):
        self.assertEqual(calc('-67 * -42 / -2 + -4 / -49 + 80 - 10 / -82'),
                         -1326.7964161274267)
    
    def test_calc_108(self):
        self.assertEqual(calc('-28 * 23 * 61 / -2 / -90 + 42 / 27 + 11'),
                         -205.6888888888889)
    
    def test_calc_109(self):
        self.assertEqual(calc('-63 / 4 - -72 / -98 * 1 - -17 / 2 + 76'),
                         68.01530612244898)
    
    def test_calc_110(self):
        self.assertEqual(calc('90 + 78 - -5 - -61 * 31 - -9 * 20 + 16'), 2260)
    
    def test_calc_111(self):
        self.assertEqual(calc('-92 + -10 / 71 / 95 - -7 - 4 * -77 * 69'),
                         21166.99851742031)
    
    def test_calc_112(self):
        self.assertEqual(calc('-43 / -93 * 51 - 57 / -53 * -6 * -50 * 27'),
                         8734.90139987827)
    
    def test_calc_113(self):
        self.assertEqual(calc('-41 / 90 - -41 - -76 / -32 / 8 - 4 * 82'),
                         -287.7524305555556)
    
    def test_calc_114(self):
        self.assertEqual(calc('67 * 19 / 40 - -37 / -76 / -66 + -43 + -68'),
                         -79.16762360446572)
    
    def test_calc_115(self):
        self.assertEqual(calc('-80 + 2 * -44 + 49 + -16 / -56 / -78 / 14'),
                         -119.00026164311879)
    
    def test_calc_116(self):
        self.assertEqual(calc('-33 + 72 * 64 / 20 - 96 + -80 / 82 / -16'),
                         101.4609756097561)
    
    def test_calc_117(self):
        self.assertEqual(
            calc('(15) + (-29 - 71 / (27)) - (47 * ((((-81 / 52)))) * 16)'),
            1154.754985754986)
    
    def test_calc_118(self):
        self.assertEqual(
            calc('-(-9) * (81 / 78 * -(98)) + (-23 + -(((-(-20 - 30)))) / 40)'),
            -940.1730769230769)
    
    def test_calc_119(self):
        self.assertEqual(
            calc('-(81) / (56 * -66 / -(19)) - (-9 - -((((-8 + -19)))) + -63)'),
            98.5836038961039)
    
    def test_calc_120(self):
        self.assertEqual(
            calc('(-77) + (80 + 83 / (12)) + (34 * (((-(77 - -57)))) * 87)'),
            -396362.0833333333)
    
    def test_calc_121(self):
        self.assertEqual(
            calc('(-12) - (-2 / -36 + (2)) / (86 * ((((-86 * -9)))) + -36)'),
            -12.000030897600341)
    
    def test_calc_122(self):
        self.assertEqual(
            calc('(51) / (-24 + -54 * -(31)) + (-40 + (((-(9 - 44)))) - -80)'),
            75.03090909090909)
    
    def test_calc_123(self):
        self.assertEqual(
            calc('(33) / (-82 / 92 - (55)) / (-38 - -(((-(-49 + 56)))) * 46)'),
            0.001640088162841955)
    
    def test_calc_124(self):
        self.assertEqual(
            calc('(-72) - (-37 + -75 + (62)) + (-95 * ((((63 + 79)))) - -93)'),
            -13419)
    
    def test_calc_125(self):
        self.assertEqual(
            calc('-(66) + (70 - -90 - (7)) / (-96 - -((((-88 + 99)))) * 29)'),
            -65.31390134529148)
    
    def test_calc_126(self):
        self.assertEqual(
            calc('(100) / (60 + 6 * (100)) - (-24 / -((((34 - -74)))) / -44)'),
            0.15656565656565657)
    
    def test_calc_127(self):
        self.assertEqual(
            calc('-(51) * (77 - -76 / -(46)) - (97 * (((-(-78 * 90)))) + -46)'),
            -684736.7391304348)
    
    def test_calc_128(self):
        self.assertEqual(
            calc('-(100) * (79 / 9 + (33)) / (77 / (((-(32 + -35)))) / 40)'),
            -6510.8225108225115)
    
    def test_calc_129(self):
        self.assertEqual(calc(
            '(-10) / (59 / -41 * -(91)) * (28 * -((((-80 / -16)))) + -42)'),
                         13.898305084745763)
    
    def test_calc_130(self):
        self.assertEqual(calc(
            '-(-73) + (-19 * 91 + (59)) - (31 - -(((-(-15 * 48)))) / -61)'),
                         -1616.1967213114754)
    
    def test_calc_131(self):
        self.assertEqual(
            calc('(10) - (-40 * -18 / (98)) - (81 * (((-(-58 - -25)))) - 99)'),
            -2571.3469387755104)
    
    def test_calc_132(self):
        self.assertEqual(
            calc('-(-5) - (84 + -21 + (11)) * (-77 + -((((-6 * 53)))) / 58)'),
            5297.275862068966)
    
    def test_calc_133(self):
        self.assertEqual(
            calc('(-52) - (-8 / -80 / (57)) / (-96 / (((-(62 - -84)))) * 58)'),
            -52.00004600221819)
    
    def test_calc_134(self):
        self.assertEqual(
            calc('-(-85) / (66 * 15 * -(14)) + (-73 * (((-(71 / 63)))) * -10)'),
            -822.7045454545454)
    
    def test_calc_135(self):
        self.assertEqual(calc(
            '-(-59) + (-11 / -79 - -(72)) - (-23 * (((-(77 + 56)))) - -63)'),
                         -2990.8607594936707)
    
    def test_calc_136(self):
        self.assertEqual(
            calc('(-39) + (28 * -92 * -(22)) + (-3 / -((((78 * 5)))) * -97)'),
            56632.25384615385)
    
    def test_calc_137(self):
        self.assertEqual(
            calc('(56) / (96 / -77 - (45)) * (71 - ((((-71 * 27)))) / 85)'),
            -113.28286502469565)
    
    def test_calc_138(self):
        self.assertEqual(calc(
            '(-31) + (-33 + -58 - (97)) + (-20 - -(((-(63 / 47)))) + -82)'),
                         -322.3404255319149)
    
    def test_calc_139(self):
        self.assertEqual(
            calc('-(-62) * (54 - 51 / -(78)) * (85 * (((-(-24 + -36)))) - 3)'),
            17271380.538461536)
    
    def test_calc_140(self):
        self.assertEqual(
            calc('-(12) / (81 + -27 / -(85)) + (58 / -((((-40 / 55)))) / 21)'),
            3.650049603174603)
    
    def test_calc_141(self):
        self.assertEqual(
            calc('-(-32) * (-63 + -76 - (44)) - (-17 / ((((54 / 63)))) + 64)'),
            -5900.166666666667)
    
    def test_calc_142(self):
        self.assertEqual(
            calc('-(-46) / (55 * 66 * (68)) + (-8 - ((((-41 - 57)))) / 85)'),
            -6.846872467995463)
    
    def test_calc_143(self):
        self.assertEqual(
            calc('-(71) + (48 - 66 + -(50)) / (82 + ((((-60 + 66)))) * -100)'),
            -70.86872586872587)
    
    def test_calc_144(self):
        self.assertEqual(calc(
            '-(-84) * (22 * 66 + -(46)) + (-94 * -(((-(-43 + 10)))) * -3)'),
                         108798)
    
    def test_calc_145(self):
        self.assertEqual(
            calc('-(83) * (-73 + -87 + (18)) / (-11 * ((((13 * 42)))) / 30)'),
            -58.871128871128874)
    
    def test_calc_146(self):
        self.assertEqual(
            calc('(-46) / (-82 / 70 * (48)) + (59 + (((-(-11 + -68)))) - 38)'),
            100.8180894308943)
    
    def test_calc_147(self):
        self.assertEqual(calc(
            '(-51) + (-42 + 92 - -(18)) / (-53 * -(((-(-16 / 45)))) + -46)'),
                         -53.50409165302782)
    
    def test_calc_148(self):
        self.assertEqual(
            calc('-(-77) / (82 + 14 * (86)) * (-41 / ((((47 + 28)))) - 96)'),
            -5.780787973043028)
    
    def test_calc_149(self):
        self.assertEqual(
            calc('-(-99) / (97 + -71 - -(91)) - (-42 / ((((57 - -69)))) + 32)'),
            -30.82051282051282)
    
    def test_calc_150(self):
        self.assertEqual(
            calc('-(-48) - (87 * 14 / -(23)) + (-83 - (((-(72 * 19)))) / 37)'),
            54.92949471210341)
    
    def test_calc_151(self):
        self.assertEqual(
            calc('(87) - (-92 * 59 + (80)) - (59 + (((-(-20 - -89)))) * 45)'),
            8481)
    
    def test_calc_152(self):
        self.assertEqual(
            calc('(84) - (60 - 36 / -(88)) + (-48 - -((((-50 + -12)))) + 5)'),
            -81.4090909090909)
    
    def test_calc_153(self):
        self.assertEqual(
            calc('(-45) / (1 / 3 / -(54)) + (18 / ((((-100 - 35)))) * 99)'),
            7276.8)
    
    def test_calc_154(self):
        self.assertEqual(calc(
            '(-62) / (-16 * -18 * -(99)) * (-80 * -((((-89 - 75)))) * -30)'),
                         855.8922558922559)
    
    def test_calc_155(self):
        self.assertEqual(
            calc('-(-9) + (8 / -64 * -(27)) + (70 + ((((-78 - -41)))) + 74)'),
            119.375)
    
    def test_calc_156(self):
        self.assertEqual(
            calc('-(75) / (74 - -73 * -(76)) - (31 + (((-(-82 * 70)))) - 87)'),
            -5683.986298867373)
    
    def test_calc_157(self):
        self.assertEqual(
            calc('(-49) * (-91 + -2 * (80)) + (-52 - ((((-47 + 99)))) * 26)'),
            10895)
    
    def test_calc_158(self):
        self.assertEqual(
            calc('-(-39) - (-48 / 33 / (49)) + (75 / (((-(65 + 74)))) * -40)'),
            60.612418414062816)
    
    def test_calc_159(self):
        self.assertEqual(
            calc('-(-18) / (-97 / 46 * (64)) * (-51 + -(((-(-20 * 8)))) + 92)'),
            15.871778350515463)
    
    def test_calc_160(self):
        self.assertEqual(
            calc('-(-19) - (37 - -15 - -(17)) - (91 - (((-(31 / 49)))) + -92)'),
            -49.63265306122449)
    
    def test_calc_161(self):
        self.assertEqual(
            calc('(13) / (34 / -62 * (22)) * (-30 - ((((-75 / 13)))) + -58)'),
            88.60695187165776)
    
    def test_calc_162(self):
        self.assertEqual(
            calc('(-86) - (-16 + -74 / -(50)) / (88 + ((((22 * 80)))) * -3)'),
            -86.0027966101695)
    
    def test_calc_163(self):
        self.assertEqual(
            calc('(-13) * (55 / -63 - (50)) / (37 - (((-(2 * -17)))) * 36)'),
            -0.5571602412377475)
    
    def test_calc_164(self):
        self.assertEqual(
            calc('(-37) + (39 / -12 * -(13)) - (72 - ((((28 / -49)))) - -87)'),
            -154.32142857142856)
    
    def test_calc_165(self):
        self.assertEqual(
            calc('-(1) / (87 / -17 * -(76)) / (-57 - ((((-42 + 69)))) / -33)'),
            4.576361112579463e-05)
    
    def test_calc_166(self):
        self.assertEqual(calc(
            '-(-71) * (38 * -88 / (100)) - (-26 + -(((-(88 / 11)))) - -83)'),
                         -2439.24)
    
    def test_calc_167(self):
        self.assertEqual(calc(
            '-(-30) * (-45 + -19 * (89)) - (-81 * (((-(-89 - -13)))) / 81)'),
                         -52004.0)
    
    def test_calc_168(self):
        self.assertEqual(
            calc('-(86) - (92 + -11 * -(69)) * (82 / -(((-(68 - 62)))) / 24)'),
            -570.5972222222222)
    
    def test_calc_169(self):
        self.assertEqual(calc(
            '(87) + (-23 / 25 + -(43)) / (-84 / -(((-(-91 / -94)))) + -29)'),
                         87.3793754152824)
    
    def test_calc_170(self):
        self.assertEqual(
            calc('-(26) + (-27 + 23 * (85)) + (70 - -((((47 * -29)))) * -39)'),
            55129)
    
    def test_calc_171(self):
        self.assertEqual(
            calc('-(25) * (-66 * 33 - (5)) / (88 + (((-(-44 - 23)))) / 94)'),
            615.1876723827797)
    
    def test_calc_172(self):
        self.assertEqual(
            calc('(-25) * (-75 + 44 * -(50)) * (-7 - -((((-94 * -67)))) / 31)'),
            11156673.387096774)
    
    def test_calc_173(self):
        self.assertEqual(
            calc('-(55) - (-74 - -74 * (49)) + (37 - ((((-77 / -89)))) * 72)'),
            -3632.2921348314608)
    
    def test_calc_174(self):
        self.assertEqual(
            calc('(82) - (25 * 36 + (61)) * (65 - -((((4 + 58)))) - 56)'),
            -68149)
    
    def test_calc_175(self):
        self.assertEqual(
            calc('-(22) + (-11 * 20 / (28)) + (33 * ((((71 / 82)))) * -34)'),
            -1001.3449477351917)
    
    def test_calc_176(self):
        self.assertEqual(
            calc('(57) - (-69 / -68 + (80)) * (-8 * -((((-25 * 74)))) + -24)'),
            1201019.0)
    
    def test_calc_177(self):
        self.assertEqual(
            calc('(43) + (-2 / 18 / (70)) - (93 / (((-(-85 * 95)))) - 23)'),
            65.98689567054892)
    
    def test_calc_178(self):
        self.assertEqual(
            calc('-(5) / (61 * -61 * (54)) - (35 / (((-(-50 - -15)))) + 78)'),
            -78.99997511620731)
    
    def test_calc_179(self):
        self.assertEqual(
            calc('-(32) - (4 + 60 - -(84)) / (-16 * ((((79 - -92)))) - -21)'),
            -31.94548802946593)
    
    def test_calc_180(self):
        self.assertEqual(
            calc('-(64) / (-58 + -63 / -(2)) + (96 + -(((-(58 - 2)))) - -40)'),
            194.41509433962264)
    
    def test_calc_181(self):
        self.assertEqual(calc(
            '-(-62) / (-57 + -63 * (2)) / (-82 + -(((-(64 - 83)))) * -73)'),
                         -0.0002596151833008814)
    
    def test_calc_182(self):
        self.assertEqual(calc(
            '-(6) * (-69 + -32 * -(13)) * (68 + -(((-(-40 + -55)))) + 35)'),
                         -16656)
    
    def test_calc_183(self):
        self.assertEqual(
            calc('(83) + (-96 * -20 / -(48)) / (-73 - -((((21 / 1)))) + 83)'),
            81.70967741935483)
    
    def test_calc_184(self):
        self.assertEqual(
            calc('-(-21) / (65 + -60 - -(51)) / (96 - ((((-12 - 68)))) - -50)'),
            0.00165929203539823)
    
    def test_calc_185(self):
        self.assertEqual(
            calc('-(2) * (69 * 15 + -(6)) - (66 / -(((-(67 * 4)))) * -90)'),
            -2035.8358208955224)
    
    def test_calc_186(self):
        self.assertEqual(
            calc('(-15) * (-58 * 29 + -(64)) - (-66 / ((((-74 / 83)))) - -95)'),
            26020.972972972973)
    
    def test_calc_187(self):
        self.assertEqual(calc(
            '-(17) * (-74 - -83 + -(20)) + (-88 / -((((-34 - 99)))) / -19)'),
                         187.0348239018599)
    
    def test_calc_188(self):
        self.assertEqual(
            calc('-(28) / (-22 / 95 - -(53)) - (69 - -((((46 / -10)))) * 94)'),
            362.8693796130062)
    
    def test_calc_189(self):
        self.assertEqual(
            calc('(60) + (37 + 78 / -(25)) / (-54 + -(((-(-56 - -81)))) * 25)'),
            60.05933450087566)
    
    def test_calc_190(self):
        self.assertEqual(calc(
            '-(25) / (-86 - -72 - (55)) / (-48 + -(((-(24 - 66)))) + -21)'),
                         -0.0032641336989163074)
    
    def test_calc_191(self):
        self.assertEqual(
            calc('-(45) * (-95 + -46 * -(78)) * (-39 / (((-(35 / 15)))) * 82)'),
            -215433269.99999997)
    
    def test_calc_192(self):
        self.assertEqual(
            calc('(-53) * (14 - 18 - -(70)) * (61 + ((((19 / -13)))) * -5)'),
            -238940.3076923077)
    
    def test_calc_193(self):
        self.assertEqual(calc(
            '(-74) + (-13 / -100 / (30)) - (-74 + ((((-16 - -32)))) - 28)'),
                         12.004333333333335)
    
    def test_calc_194(self):
        self.assertEqual(
            calc('-(76) * (66 - 76 + (23)) * (70 * (((-(-15 + -48)))) / 6)'),
            -726180.0)
    
    def test_calc_195(self):
        self.assertEqual(
            calc('(91) + (19 * 75 * (65)) + (-43 + -(((-(-54 + 10)))) / -39)'),
            92674.1282051282)
    
    def test_calc_196(self):
        self.assertEqual(calc(
            '-(-21) + (28 / -32 - (54)) / (26 * -(((-(-17 * -54)))) / 28)'),
                         20.93562510474275)
    
    def test_calc_197(self):
        self.assertEqual(
            calc('(-47) / (-97 * -59 * (90)) + (90 + (((-(56 * 76)))) * 9)'),
            -38214.000091249734)
    
    def test_calc_198(self):
        self.assertEqual(
            calc('(-44) - (-16 + -94 / (29)) * (24 * -(((-(-9 / 79)))) / -1)'),
            8.609340899170661)
    
    def test_calc_199(self):
        self.assertEqual(
            calc('-(85) * (-41 / -26 - -(42)) + (50 / -((((65 / 23)))) / 100)'),
            -3704.215384615385)
    
    def test_calc_200(self):
        self.assertEqual(calc(
            '-(40) * (13 * 93 + -(78)) * (-38 * -(((-(-34 * 79)))) - -12)'),
                         -4618099200)
    
    def test_calc_201(self):
        self.assertEqual(
            calc('(7) - (73 + 25 * (7)) / (20 + ((((-40 + 97)))) + 29)'),
            4.660377358490566)
    
    def test_calc_202(self):
        self.assertEqual(
            calc('(54) + (13 / -50 * (29)) - (-64 - -(((-(-34 * 52)))) / -50)'),
            145.82)
    
    def test_calc_203(self):
        self.assertEqual(
            calc('(-53) + (100 * -46 - -(28)) * (91 * (((-(-17 - 47)))) / 96)'),
            -277421.0)
    
    def test_calc_204(self):
        self.assertEqual(
            calc('(30) - (67 * 13 * -(97)) + (-24 - ((((-88 / 99)))) * -31)'),
            84465.44444444444)
    
    def test_calc_205(self):
        self.assertEqual(
            calc('-(95) - (-40 + -44 * (77)) / (32 - -((((77 - 82)))) * -8)'),
            -47.388888888888886)
    
    def test_calc_206(self):
        self.assertEqual(calc(
            '-(-97) * (-97 - -86 * -(23)) * (-46 + ((((-69 - 44)))) / -37)'),
                         8643945.27027027)
    
    def test_calc_207(self):
        self.assertEqual(
            calc('(-13) + (9 / 14 / (54)) - (-29 - -((((-48 / 38)))) + 10)'),
            7.275062656641605)
    
    def test_calc_208(self):
        self.assertEqual(
            calc('(-40) - (-85 * 22 - (78)) - (2 - (((-(-19 * 62)))) + 60)'),
            3024)
    
    def test_calc_209(self):
        self.assertEqual(
            calc('-(-38) * (8 - 21 * (98)) + (75 - -(((-(-25 + -38)))) * -97)'),
            -83936)
    
    def test_calc_210(self):
        self.assertEqual(calc(
            '(-3) * (-58 * 17 / (40)) * (-84 / -(((-(-42 + -70)))) * -69)'),
                         -3826.9124999999995)
    
    def test_calc_211(self):
        self.assertEqual(
            calc('-(1) / (-20 / -53 * -(49)) + (-79 + ((((-57 - 9)))) - -5)'),
            -139.94591836734693)
    
    def test_calc_212(self):
        self.assertEqual(
            calc('-(20) * (-38 - -76 + (96)) + (-18 + (((-(69 + -73)))) / 60)'),
            -2697.9333333333334)
    
    def test_calc_213(self):
        self.assertEqual(
            calc('-(69) * (28 + -76 * (56)) + (90 + -(((-(100 - 2)))) / 61)'),
            291823.60655737703)
    
    def test_calc_214(self):
        self.assertEqual(calc(
            '-(-86) - (64 + 14 / (22)) + (-73 * -(((-(-44 / -80)))) * -20)'),
                         824.3636363636365)
    
    def test_calc_215(self):
        self.assertEqual(calc(
            '(-82) / (-3 / 40 * (95)) / (-53 - -(((-(-29 * -20)))) * -12)'),
                         0.001666247564763944)
    
    def test_calc_216(self):
        self.assertEqual(
            calc('-(-85) * (31 - -16 * (69)) * (75 * -((((36 - -33)))) / -32)'),
            15601816.40625)
    
    def test_calc_217(self):
        self.assertEqual(calc('40- 10- 8- -72'), 94)
    
    def test_calc_218(self):
        self.assertEqual(calc('-33- 31- 18- 54'), -136)
    
    def test_calc_219(self):
        self.assertEqual(calc('-75- -37- 62- 50'), -150)
    
    def test_calc_220(self):
        self.assertEqual(calc('-59- -28- 6- 8'), -45)
    
    def test_calc_221(self):
        self.assertEqual(calc('62- -57- -78- -95'), 292)
    
    def test_calc_222(self):
        self.assertEqual(calc('-15- 94- 60- 4'), -173)
    
    def test_calc_223(self):
        self.assertEqual(calc('92- -19- 22- 36'), 53)
    
    def test_calc_224(self):
        self.assertEqual(calc('4- 8- 53- -36'), -21)
    
    def test_calc_225(self):
        self.assertEqual(calc('21- -71- 51- 80'), -39)
    
    def test_calc_226(self):
        self.assertEqual(calc('-12- -11- 66- -70'), 3)
    
    def test_calc_227(self):
        self.assertEqual(calc('50- 80- 27- -11'), -46)
    
    def test_calc_228(self):
        self.assertEqual(calc('26- 49- -72- 70'), -21)
    
    def test_calc_229(self):
        self.assertEqual(calc('40- 36- -48- 100'), -48)
    
    def test_calc_230(self):
        self.assertEqual(calc('-79- -58- -35- 67'), -53)
    
    def test_calc_231(self):
        self.assertEqual(calc('-2- -74- 6- 89'), -23)
    
    def test_calc_232(self):
        self.assertEqual(calc('-31- -85- 36- -51'), 69)
    
    def test_calc_233(self):
        self.assertEqual(calc('74- -32- 24- -1'), 83)
    
    def test_calc_234(self):
        self.assertEqual(calc('34- -99- 49- -9'), 93)
    
    def test_calc_235(self):
        self.assertEqual(calc('41- 51- -19- -10'), 19)
    
    def test_calc_236(self):
        self.assertEqual(calc('-76- -26- 19- 77'), -146)
    
    def test_calc_237(self):
        self.assertEqual(calc('48- -51- 22- -16'), 93)
    
    def test_calc_238(self):
        self.assertEqual(calc('-13- 96- -90- -63'), 44)
    
    def test_calc_239(self):
        self.assertEqual(calc('32- -24- -62- 80'), 38)
    
    def test_calc_240(self):
        self.assertEqual(calc('49- 63- 5- -48'), 29)
    
    def test_calc_241(self):
        self.assertEqual(calc('23- -22- 88- -25'), -18)
    
    def test_calc_242(self):
        self.assertEqual(calc('59- -85- 7- 41'), 96)
    
    def test_calc_243(self):
        self.assertEqual(calc('-93- 57- -31- -92'), -27)
    
    def test_calc_244(self):
        self.assertEqual(calc('-73- -5- 21- 79'), -168)
    
    def test_calc_245(self):
        self.assertEqual(calc('-78- -48- 53- 94'), -177)
    
    def test_calc_246(self):
        self.assertEqual(calc('-51- -20- 72- 41'), -144)
    
    def test_calc_247(self):
        self.assertEqual(calc('-47- -61- 20- 32'), -38)
    
    def test_calc_248(self):
        self.assertEqual(calc('-75- -69- -32- -40'), 66)
    
    def test_calc_249(self):
        self.assertEqual(calc('-11- -11- 5- 15'), -20)
    
    def test_calc_250(self):
        self.assertEqual(calc('-3- -64- -27- -13'), 101)
    
    def test_calc_251(self):
        self.assertEqual(calc('21- -52- 7- -38'), 104)
    
    def test_calc_252(self):
        self.assertEqual(calc('-11- 78- 31- -81'), -39)
    
    def test_calc_253(self):
        self.assertEqual(calc('-4- 75- -23- -54'), -2)
    
    def test_calc_254(self):
        self.assertEqual(calc('-84- 50- -60- 34'), -108)
    
    def test_calc_255(self):
        self.assertEqual(calc('94- -10- -41- 87'), 58)
    
    def test_calc_256(self):
        self.assertEqual(calc('-23- -8- 34- -100'), 51)
    
    def test_calc_257(self):
        self.assertEqual(calc('63- -70- 23- 14'), 96)
    
    def test_calc_258(self):
        self.assertEqual(calc('67- -75- -38- 23'), 157)
    
    def test_calc_259(self):
        self.assertEqual(calc('52- 6- 58- 24'), -36)
    
    def test_calc_260(self):
        self.assertEqual(calc('-95- 40- 94- -72'), -157)
    
    def test_calc_261(self):
        self.assertEqual(calc('-55- 17- 36- 60'), -168)
    
    def test_calc_262(self):
        self.assertEqual(calc('-100- 27- 7- 19'), -153)
    
    def test_calc_263(self):
        self.assertEqual(calc('-78- -14- -49- 74'), -89)
    
    def test_calc_264(self):
        self.assertEqual(calc('-52- 76- 43- 48'), -219)
    
    def test_calc_265(self):
        self.assertEqual(calc('-27- 45- 28- -67'), -33)
    
    def test_calc_266(self):
        self.assertEqual(calc('-64- 18- 38- 97'), -217)
    
    def test_calc_267(self):
        self.assertEqual(calc('48- 34- -55- -64'), 133)
    
    def test_calc_268(self):
        self.assertEqual(calc('-35- 80- -94- 33'), -54)
    
    def test_calc_269(self):
        self.assertEqual(calc('-37- 38- 74- -6'), -143)
    
    def test_calc_270(self):
        self.assertEqual(calc('53- -17- -55- -26'), 151)
    
    def test_calc_271(self):
        self.assertEqual(calc('-29- 23- 57- -80'), -29)
    
    def test_calc_272(self):
        self.assertEqual(calc('-31- -61- 25- -6'), 11)
    
    def test_calc_273(self):
        self.assertEqual(calc('-28- -57- 69- -76'), 36)
    
    def test_calc_274(self):
        self.assertEqual(calc('32- -84- -32- -20'), 168)
    
    def test_calc_275(self):
        self.assertEqual(calc('-86- -24- -97- -32'), 67)
    
    def test_calc_276(self):
        self.assertEqual(calc('69- 54- -83- -41'), 139)
    
    def test_calc_277(self):
        self.assertEqual(calc('-99- -98- -56- -10'), 65)
    
    def test_calc_278(self):
        self.assertEqual(calc('-14- 22- -82- -32'), 78)
    
    def test_calc_279(self):
        self.assertEqual(calc('-83- 5- -49- 38'), -77)
    
    def test_calc_280(self):
        self.assertEqual(calc('49- 33- -25- 93'), -52)
    
    def test_calc_281(self):
        self.assertEqual(calc('5- -99- -94- -7'), 205)
    
    def test_calc_282(self):
        self.assertEqual(calc('-9- -41- -9- -99'), 140)
    
    def test_calc_283(self):
        self.assertEqual(calc('5- 40- 46- 35'), -116)
    
    def test_calc_284(self):
        self.assertEqual(calc('-96- 45- -12- -45'), -84)
    
    def test_calc_285(self):
        self.assertEqual(calc('-92- -54- -25- 87'), -100)
    
    def test_calc_286(self):
        self.assertEqual(calc('-25- 40- 47- -48'), -64)
    
    def test_calc_287(self):
        self.assertEqual(calc('27- -75- -67- -57'), 226)
    
    def test_calc_288(self):
        self.assertEqual(calc('24- 46- -94- 82'), -10)
    
    def test_calc_289(self):
        self.assertEqual(calc('77- -6- 62- 95'), -74)
    
    def test_calc_290(self):
        self.assertEqual(calc('27- 95- 96- -84'), -80)
    
    def test_calc_291(self):
        self.assertEqual(calc('23- -9- -48- -2'), 82)
    
    def test_calc_292(self):
        self.assertEqual(calc('84- 73- 26- 93'), -108)
    
    def test_calc_293(self):
        self.assertEqual(calc('30- 67- 88- -59'), -66)
    
    def test_calc_294(self):
        self.assertEqual(calc('17- 48- 23- 70'), -124)
    
    def test_calc_295(self):
        self.assertEqual(calc('-70- 37- -67- 76'), -116)
    
    def test_calc_296(self):
        self.assertEqual(calc('-64- -49- -41- 94'), -68)
    
    def test_calc_297(self):
        self.assertEqual(calc('4- 54- -86- -33'), 69)
    
    def test_calc_298(self):
        self.assertEqual(calc('-42- 61- 72- 39'), -214)
    
    def test_calc_299(self):
        self.assertEqual(calc('13- -52- -69- 96'), 38)
    
    def test_calc_300(self):
        self.assertEqual(calc('81- 15- -5- -13'), 84)
    
    def test_calc_301(self):
        self.assertEqual(calc('88- -66- 53- 10'), 91)
    
    def test_calc_302(self):
        self.assertEqual(calc('-60- -96- 52- 55'), -71)
    
    def test_calc_303(self):
        self.assertEqual(calc('-7- -18- -54- -19'), 84)
    
    def test_calc_304(self):
        self.assertEqual(calc('73- -47- -59- 60'), 119)
    
    def test_calc_305(self):
        self.assertEqual(calc('-43- 7- -64- 17'), -3)
    
    def test_calc_306(self):
        self.assertEqual(calc('5- 41- -44- -2'), 10)
    
    def test_calc_307(self):
        self.assertEqual(calc('31- -83- 69- 81'), -36)
    
    def test_calc_308(self):
        self.assertEqual(calc('37- -73- 49- -53'), 114)
    
    def test_calc_309(self):
        self.assertEqual(calc('33- 8- -47- -60'), 132)
    
    def test_calc_310(self):
        self.assertEqual(calc('14- 93- 82- -4'), -157)
    
    def test_calc_311(self):
        self.assertEqual(calc('-9- -32- -26- 21'), 28)
    
    def test_calc_312(self):
        self.assertEqual(calc('-32- 33- 10- -26'), -49)
    
    def test_calc_313(self):
        self.assertEqual(calc('89- -81- 5- 1'), 164)
    
    def test_calc_314(self):
        self.assertEqual(calc('25- 59- 22- 94'), -150)
    
    def test_calc_315(self):
        self.assertEqual(calc('24- -86- -61- -28'), 199)
    
    def test_calc_316(self):
        self.assertEqual(calc('-1- -44- 45- 62'), -64)
