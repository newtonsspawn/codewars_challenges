from unittest import TestCase

from dbllinear import dbl_linear


class TestDblLinear(TestCase):
    
    def test_dbl_linear_001(self):
        self.assertEqual(dbl_linear(10), 22)
    
    def test_dbl_linear_002(self):
        self.assertEqual(dbl_linear(20), 57)
    
    def test_dbl_linear_003(self):
        self.assertEqual(dbl_linear(30), 91)
    
    def test_dbl_linear_004(self):
        self.assertEqual(dbl_linear(50), 175)
    
    def test_dbl_linear_005(self):
        self.assertEqual(dbl_linear(100), 447)
    
    def test_dbl_linear_006(self):
        self.assertEqual(dbl_linear(500), 3355)
    
    def test_dbl_linear_007(self):
        self.assertEqual(dbl_linear(1000), 8488)
    
    def test_dbl_linear_008(self):
        self.assertEqual(dbl_linear(2000), 19773)
    
    def test_dbl_linear_009(self):
        self.assertEqual(dbl_linear(6000), 80914)
    
    def test_dbl_linear_010(self):
        self.assertEqual(dbl_linear(60000), 1511311)
    
    def test_dbl_linear_011(self):
        self.assertEqual(dbl_linear(5811), 78703)
    
    def test_dbl_linear_012(self):
        self.assertEqual(dbl_linear(4162), 51760)
    
    def test_dbl_linear_013(self):
        self.assertEqual(dbl_linear(14294), 243139)
    
    def test_dbl_linear_014(self):
        self.assertEqual(dbl_linear(12180), 206110)
    
    def test_dbl_linear_015(self):
        self.assertEqual(dbl_linear(933), 7677)
    
    def test_dbl_linear_016(self):
        self.assertEqual(dbl_linear(1122), 9417)
    
    def test_dbl_linear_017(self):
        self.assertEqual(dbl_linear(6743), 96465)
    
    def test_dbl_linear_018(self):
        self.assertEqual(dbl_linear(5623), 75447)
    
    def test_dbl_linear_019(self):
        self.assertEqual(dbl_linear(612), 4414)
    
    def test_dbl_linear_020(self):
        self.assertEqual(dbl_linear(14044), 237933)
    
    def test_dbl_linear_021(self):
        self.assertEqual(dbl_linear(8838), 136695)
    
    def test_dbl_linear_022(self):
        self.assertEqual(dbl_linear(13446), 226891)
    
    def test_dbl_linear_023(self):
        self.assertEqual(dbl_linear(14332), 243514)
    
    def test_dbl_linear_024(self):
        self.assertEqual(dbl_linear(5279), 71371)
    
    def test_dbl_linear_025(self):
        self.assertEqual(dbl_linear(13009), 221161)
    
    def test_dbl_linear_026(self):
        self.assertEqual(dbl_linear(8868), 137080)
    
    def test_dbl_linear_027(self):
        self.assertEqual(dbl_linear(10496), 164944)
    
    def test_dbl_linear_028(self):
        self.assertEqual(dbl_linear(13766), 234423)
    
    def test_dbl_linear_029(self):
        self.assertEqual(dbl_linear(5930), 79462)
    
    def test_dbl_linear_030(self):
        self.assertEqual(dbl_linear(5685), 76150)
    
    def test_dbl_linear_031(self):
        self.assertEqual(dbl_linear(10692), 167674)
    
    def test_dbl_linear_032(self):
        self.assertEqual(dbl_linear(8965), 140143)
    
    def test_dbl_linear_033(self):
        self.assertEqual(dbl_linear(11526), 188731)
    
    def test_dbl_linear_034(self):
        self.assertEqual(dbl_linear(9377), 147981)
    
    def test_dbl_linear_035(self):
        self.assertEqual(dbl_linear(13660), 230860)
    
    def test_dbl_linear_036(self):
        self.assertEqual(dbl_linear(14255), 242704)
    
    def test_dbl_linear_037(self):
        self.assertEqual(dbl_linear(9560), 149890)
    
    def test_dbl_linear_038(self):
        self.assertEqual(dbl_linear(12725), 216111)
    
    def test_dbl_linear_039(self):
        self.assertEqual(dbl_linear(977), 8325)
    
    def test_dbl_linear_040(self):
        self.assertEqual(dbl_linear(5885), 79221)
    
    def test_dbl_linear_041(self):
        self.assertEqual(dbl_linear(2796), 30463)
    
    def test_dbl_linear_042(self):
        self.assertEqual(dbl_linear(5255), 70759)
    
    def test_dbl_linear_043(self):
        self.assertEqual(dbl_linear(10025), 157845)
    
    def test_dbl_linear_044(self):
        self.assertEqual(dbl_linear(14004), 237573)
    
    def test_dbl_linear_045(self):
        self.assertEqual(dbl_linear(11900), 200127)
    
    def test_dbl_linear_046(self):
        self.assertEqual(dbl_linear(14857), 255406)
    
    def test_dbl_linear_047(self):
        self.assertEqual(dbl_linear(10200), 160555)
    
    def test_dbl_linear_048(self):
        self.assertEqual(dbl_linear(2025), 20127)
    
    def test_dbl_linear_049(self):
        self.assertEqual(dbl_linear(12207), 206338)
    
    def test_dbl_linear_050(self):
        self.assertEqual(dbl_linear(9154), 143335)
    
    def test_dbl_linear_051(self):
        self.assertEqual(dbl_linear(8500), 125559)
    
    def test_dbl_linear_052(self):
        self.assertEqual(dbl_linear(2795), 30415)
    
    def test_dbl_linear_053(self):
        self.assertEqual(dbl_linear(11660), 192903)
    
    def test_dbl_linear_054(self):
        self.assertEqual(dbl_linear(11748), 196857)
    
    def test_dbl_linear_055(self):
        self.assertEqual(dbl_linear(11181), 178174)
    
    def test_dbl_linear_056(self):
        self.assertEqual(dbl_linear(6336), 87487)
    
    def test_dbl_linear_057(self):
        self.assertEqual(dbl_linear(2760), 30135)
    
    def test_dbl_linear_058(self):
        self.assertEqual(dbl_linear(2700), 29223)
    
    def test_dbl_linear_059(self):
        self.assertEqual(dbl_linear(3942), 49339)
    
    def test_dbl_linear_060(self):
        self.assertEqual(dbl_linear(6504), 90589)
    
    def test_dbl_linear_061(self):
        self.assertEqual(dbl_linear(12514), 212089)
    
    def test_dbl_linear_062(self):
        self.assertEqual(dbl_linear(13876), 236347)
    
    def test_dbl_linear_063(self):
        self.assertEqual(dbl_linear(8811), 135871)
    
    def test_dbl_linear_064(self):
        self.assertEqual(dbl_linear(5371), 72259)
    
    def test_dbl_linear_065(self):
        self.assertEqual(dbl_linear(12841), 217486)
    
    def test_dbl_linear_066(self):
        self.assertEqual(dbl_linear(2430), 25983)
    
    def test_dbl_linear_067(self):
        self.assertEqual(dbl_linear(13102), 222591)
    
    def test_dbl_linear_068(self):
        self.assertEqual(dbl_linear(4457), 55567)
    
    def test_dbl_linear_069(self):
        self.assertEqual(dbl_linear(10241), 161149)
    
    def test_dbl_linear_070(self):
        self.assertEqual(dbl_linear(8998), 140799)
    
    def test_dbl_linear_071(self):
        self.assertEqual(dbl_linear(14673), 251128)
    
    def test_dbl_linear_072(self):
        self.assertEqual(dbl_linear(3130), 36127)
    
    def test_dbl_linear_073(self):
        self.assertEqual(dbl_linear(4797), 60466)
    
    def test_dbl_linear_074(self):
        self.assertEqual(dbl_linear(1399), 12717)
    
    def test_dbl_linear_075(self):
        self.assertEqual(dbl_linear(14258), 242733)
    
    def test_dbl_linear_076(self):
        self.assertEqual(dbl_linear(9319), 146671)
    
    def test_dbl_linear_077(self):
        self.assertEqual(dbl_linear(14802), 253935)
    
    def test_dbl_linear_078(self):
        self.assertEqual(dbl_linear(13571), 228447)
    
    def test_dbl_linear_079(self):
        self.assertEqual(dbl_linear(10498), 164971)
    
    def test_dbl_linear_080(self):
        self.assertEqual(dbl_linear(7916), 113980)
    
    def test_dbl_linear_081(self):
        self.assertEqual(dbl_linear(11368), 183739)
    
    def test_dbl_linear_082(self):
        self.assertEqual(dbl_linear(1561), 14587)
    
    def test_dbl_linear_083(self):
        self.assertEqual(dbl_linear(14012), 237664)
    
    def test_dbl_linear_084(self):
        self.assertEqual(dbl_linear(12939), 220510)
    
    def test_dbl_linear_085(self):
        self.assertEqual(dbl_linear(13087), 222393)
    
    def test_dbl_linear_086(self):
        self.assertEqual(dbl_linear(10303), 162043)
    
    def test_dbl_linear_087(self):
        self.assertEqual(dbl_linear(3459), 39718)
    
    def test_dbl_linear_088(self):
        self.assertEqual(dbl_linear(5864), 79087)
    
    def test_dbl_linear_089(self):
        self.assertEqual(dbl_linear(14259), 242734)
    
    def test_dbl_linear_090(self):
        self.assertEqual(dbl_linear(8951), 138189)
    
    def test_dbl_linear_091(self):
        self.assertEqual(dbl_linear(7863), 113511)
    
    def test_dbl_linear_092(self):
        self.assertEqual(dbl_linear(5906), 79318)
    
    def test_dbl_linear_093(self):
        self.assertEqual(dbl_linear(11950), 201199)
    
    def test_dbl_linear_094(self):
        self.assertEqual(dbl_linear(11853), 199281)
    
    def test_dbl_linear_095(self):
        self.assertEqual(dbl_linear(7095), 103095)
    
    def test_dbl_linear_096(self):
        self.assertEqual(dbl_linear(5277), 71359)
    
    def test_dbl_linear_097(self):
        self.assertEqual(dbl_linear(8607), 128923)
    
    def test_dbl_linear_098(self):
        self.assertEqual(dbl_linear(11447), 185169)
    
    def test_dbl_linear_099(self):
        self.assertEqual(dbl_linear(3533), 40879)
    
    def test_dbl_linear_100(self):
        self.assertEqual(dbl_linear(12370), 210639)
    
    def test_dbl_linear_101(self):
        self.assertEqual(dbl_linear(1096), 9265)
    
    def test_dbl_linear_102(self):
        self.assertEqual(dbl_linear(2665), 28255)
    
    def test_dbl_linear_103(self):
        self.assertEqual(dbl_linear(9968), 157485)
    
    def test_dbl_linear_104(self):
        self.assertEqual(dbl_linear(8762), 133771)
    
    def test_dbl_linear_105(self):
        self.assertEqual(dbl_linear(10495), 164943)
    
    def test_dbl_linear_106(self):
        self.assertEqual(dbl_linear(9976), 157522)
    
    def test_dbl_linear_107(self):
        self.assertEqual(dbl_linear(3081), 35704)
    
    def test_dbl_linear_108(self):
        self.assertEqual(dbl_linear(5664), 75933)
    
    def test_dbl_linear_109(self):
        self.assertEqual(dbl_linear(12237), 206751)
    
    def test_dbl_linear_110(self):
        self.assertEqual(dbl_linear(688), 5035)
