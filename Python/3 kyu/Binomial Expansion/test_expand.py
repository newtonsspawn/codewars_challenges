from unittest import TestCase

from expand import expand


class TestExpand(TestCase):
    
    def test_expand_001(self):
        self.assertEqual(expand("(x+1)^0"), "1")
    
    def test_expand_002(self):
        self.assertEqual(expand("(x+1)^1"), "x+1")
    
    def test_expand_003(self):
        self.assertEqual(expand("(x+1)^2"), "x^2+2x+1")
    
    def test_expand_004(self):
        self.assertEqual(expand("(x-1)^0"), "1")
    
    def test_expand_005(self):
        self.assertEqual(expand("(x-1)^1"), "x-1")
    
    def test_expand_006(self):
        self.assertEqual(expand("(x-1)^2"), "x^2-2x+1")
    
    def test_expand_007(self):
        self.assertEqual(expand("(5m+3)^4"), "625m^4+1500m^3+1350m^2+540m+81")
    
    def test_expand_008(self):
        self.assertEqual(expand("(2x-3)^3"), "8x^3-36x^2+54x-27")
    
    def test_expand_009(self):
        self.assertEqual(expand("(7x-7)^0"), "1")
    
    def test_expand_010(self):
        self.assertEqual(expand("(-5m+3)^4"), "625m^4-1500m^3+1350m^2-540m+81")
    
    def test_expand_011(self):
        self.assertEqual(expand("(-2k-3)^3"), "-8k^3-36k^2-54k-27")
    
    def test_expand_012(self):
        self.assertEqual(expand("(-7x-7)^0"), "1")
    
    def test_expand_013(self):
        self.assertEqual(expand("(-5i-10)^1"), "-5i-10")
    
    def test_expand_014(self):
        self.assertEqual(expand("(-3a-5)^5"),
                         "-243a^5-2025a^4-6750a^3-11250a^2-9375a-3125")
    
    def test_expand_015(self):
        self.assertEqual(expand("(-4m-17)^3"), "-64m^3-816m^2-3468m-4913")
    
    def test_expand_016(self):
        self.assertEqual(expand("(7n+13)^5"),
                         "16807n^5+156065n^4+579670n^3+1076530n^2+999635n"
                         "+371293")
    
    def test_expand_017(self):
        self.assertEqual(expand("(-3n+2)^5"),
                         "-243n^5+810n^4-1080n^3+720n^2-240n+32")
    
    def test_expand_018(self):
        self.assertEqual(expand("(-k-15)^3"), "-k^3-45k^2-675k-3375")
    
    def test_expand_019(self):
        self.assertEqual(expand("(-6p-1)^0"), "1")
    
    def test_expand_020(self):
        self.assertEqual(expand("(2u-8)^5"),
                         "32u^5-640u^4+5120u^3-20480u^2+40960u-32768")
    
    def test_expand_021(self):
        self.assertEqual(expand("(-2c+13)^0"), "1")
    
    def test_expand_022(self):
        self.assertEqual(expand("(t-18)^4"), "t^4-72t^3+1944t^2-23328t+104976")
    
    def test_expand_023(self):
        self.assertEqual(expand("(-4h-13)^0"), "1")
    
    def test_expand_024(self):
        self.assertEqual(expand("(-w-10)^1"), "-w-10")
    
    def test_expand_025(self):
        self.assertEqual(expand("(-2j-3)^4"), "16j^4+96j^3+216j^2+216j+81")
    
    def test_expand_026(self):
        self.assertEqual(expand("(7b+15)^2"), "49b^2+210b+225")
    
    def test_expand_027(self):
        self.assertEqual(expand("(-7g+2)^0"), "1")
    
    def test_expand_028(self):
        self.assertEqual(expand("(5b-6)^4"),
                         "625b^4-3000b^3+5400b^2-4320b+1296")
    
    def test_expand_029(self):
        self.assertEqual(expand("(-3i-16)^2"), "9i^2+96i+256")
    
    def test_expand_030(self):
        self.assertEqual(expand("(4k-15)^2"), "16k^2-120k+225")
    
    def test_expand_031(self):
        self.assertEqual(expand("(-9v+19)^3"), "-729v^3+4617v^2-9747v+6859")
    
    def test_expand_032(self):
        self.assertEqual(expand("(5s+7)^5"),
                         "3125s^5+21875s^4+61250s^3+85750s^2+60025s+16807")
    
    def test_expand_033(self):
        self.assertEqual(expand("(5c-7)^1"), "5c-7")
    
    def test_expand_034(self):
        self.assertEqual(expand("(8x+8)^3"), "512x^3+1536x^2+1536x+512")
    
    def test_expand_035(self):
        self.assertEqual(expand("(2i-10)^3"), "8i^3-120i^2+600i-1000")
    
    def test_expand_036(self):
        self.assertEqual(expand("(-8t+9)^3"), "-512t^3+1728t^2-1944t+729")
    
    def test_expand_037(self):
        self.assertEqual(expand("(2k+8)^3"), "8k^3+96k^2+384k+512")
    
    def test_expand_038(self):
        self.assertEqual(expand("(6n-16)^1"), "6n-16")
    
    def test_expand_039(self):
        self.assertEqual(expand("(i+20)^0"), "1")
    
    def test_expand_040(self):
        self.assertEqual(expand("(2l-1)^2"), "4l^2-4l+1")
    
    def test_expand_041(self):
        self.assertEqual(expand("(-3z+20)^0"), "1")
    
    def test_expand_042(self):
        self.assertEqual(expand("(-8o+10)^1"), "-8o+10")
    
    def test_expand_043(self):
        self.assertEqual(expand("(-3l+12)^0"), "1")
    
    def test_expand_044(self):
        self.assertEqual(expand("(9q+17)^5"),
                         "59049q^5+557685q^4+2106810q^3+3979530q^2+3758445q"
                         "+1419857")
    
    def test_expand_045(self):
        self.assertEqual(expand("(2p+6)^5"),
                         "32p^5+480p^4+2880p^3+8640p^2+12960p+7776")
    
    def test_expand_046(self):
        self.assertEqual(expand("(-6n-6)^3"), "-216n^3-648n^2-648n-216")
    
    def test_expand_047(self):
        self.assertEqual(expand("(-6j+1)^5"),
                         "-7776j^5+6480j^4-2160j^3+360j^2-30j+1")
    
    def test_expand_048(self):
        self.assertEqual(expand("(-8e-3)^0"), "1")
    
    def test_expand_049(self):
        self.assertEqual(expand("(7h+4)^2"), "49h^2+56h+16")
    
    def test_expand_050(self):
        self.assertEqual(expand("(-9v-15)^2"), "81v^2+270v+225")
    
    def test_expand_051(self):
        self.assertEqual(expand("(3d+20)^3"), "27d^3+540d^2+3600d+8000")
    
    def test_expand_052(self):
        self.assertEqual(expand("(8i+10)^0"), "1")
    
    def test_expand_053(self):
        self.assertEqual(expand("(-10x-5)^1"), "-10x-5")
    
    def test_expand_054(self):
        self.assertEqual(expand("(-2b+9)^4"), "16b^4-288b^3+1944b^2-5832b+6561")
    
    def test_expand_055(self):
        self.assertEqual(expand("(-7n-19)^5"),
                         "-16807n^5-228095n^4-1238230n^3-3360910n^2-4561235n"
                         "-2476099")
    
    def test_expand_056(self):
        self.assertEqual(expand("(6m+16)^5"),
                         "7776m^5+103680m^4+552960m^3+1474560m^2+1966080m"
                         "+1048576")
    
    def test_expand_057(self):
        self.assertEqual(expand("(7p-2)^2"), "49p^2-28p+4")
    
    def test_expand_058(self):
        self.assertEqual(expand("(-3w+11)^2"), "9w^2-66w+121")
    
    def test_expand_059(self):
        self.assertEqual(expand("(-3h+12)^3"), "-27h^3+324h^2-1296h+1728")
    
    def test_expand_060(self):
        self.assertEqual(expand("(-2b-7)^5"),
                         "-32b^5-560b^4-3920b^3-13720b^2-24010b-16807")
    
    def test_expand_061(self):
        self.assertEqual(expand("(-2f+14)^0"), "1")
    
    def test_expand_062(self):
        self.assertEqual(expand("(3g+20)^0"), "1")
    
    def test_expand_063(self):
        self.assertEqual(expand("(-10v+8)^1"), "-10v+8")
    
    def test_expand_064(self):
        self.assertEqual(expand("(-3m-20)^4"),
                         "81m^4+2160m^3+21600m^2+96000m+160000")
    
    def test_expand_065(self):
        self.assertEqual(expand("(2g-19)^1"), "2g-19")
    
    def test_expand_066(self):
        self.assertEqual(expand("(8v+5)^4"),
                         "4096v^4+10240v^3+9600v^2+4000v+625")
    
    def test_expand_067(self):
        self.assertEqual(expand("(-9p+19)^1"), "-9p+19")
    
    def test_expand_068(self):
        self.assertEqual(expand("(v-4)^1"), "v-4")
    
    def test_expand_069(self):
        self.assertEqual(expand("(7t-13)^1"), "7t-13")
    
    def test_expand_070(self):
        self.assertEqual(expand("(7a+10)^2"), "49a^2+140a+100")
    
    def test_expand_071(self):
        self.assertEqual(expand("(7v+19)^1"), "7v+19")
    
    def test_expand_072(self):
        self.assertEqual(expand("(8a-1)^2"), "64a^2-16a+1")
    
    def test_expand_073(self):
        self.assertEqual(expand("(d-11)^0"), "1")
    
    def test_expand_074(self):
        self.assertEqual(expand("(-o+17)^5"),
                         "-o^5+85o^4-2890o^3+49130o^2-417605o+1419857")
    
    def test_expand_075(self):
        self.assertEqual(expand("(-8y-4)^4"),
                         "4096y^4+8192y^3+6144y^2+2048y+256")
    
    def test_expand_076(self):
        self.assertEqual(expand("(4k-6)^0"), "1")
    
    def test_expand_077(self):
        self.assertEqual(expand("(-10x+18)^3"), "-1000x^3+5400x^2-9720x+5832")
    
    def test_expand_078(self):
        self.assertEqual(expand("(-6o+11)^1"), "-6o+11")
    
    def test_expand_079(self):
        self.assertEqual(expand("(9q-20)^2"), "81q^2-360q+400")
    
    def test_expand_080(self):
        self.assertEqual(expand("(2i+2)^0"), "1")
    
    def test_expand_081(self):
        self.assertEqual(expand("(5s+14)^0"), "1")
    
    def test_expand_082(self):
        self.assertEqual(expand("(y-6)^2"), "y^2-12y+36")
    
    def test_expand_083(self):
        self.assertEqual(expand("(6d+6)^4"),
                         "1296d^4+5184d^3+7776d^2+5184d+1296")
    
    def test_expand_084(self):
        self.assertEqual(expand("(-5g+17)^5"),
                         "-3125g^5+53125g^4-361250g^3+1228250g^2-2088025g"
                         "+1419857")
    
    def test_expand_085(self):
        self.assertEqual(expand("(-6y+14)^5"),
                         "-7776y^5+90720y^4-423360y^3+987840y^2-1152480y"
                         "+537824")
    
    def test_expand_086(self):
        self.assertEqual(expand("(-5q-5)^4"),
                         "625q^4+2500q^3+3750q^2+2500q+625")
    
    def test_expand_087(self):
        self.assertEqual(expand("(6c+1)^3"), "216c^3+108c^2+18c+1")
    
    def test_expand_088(self):
        self.assertEqual(expand("(8u-5)^1"), "8u-5")
    
    def test_expand_089(self):
        self.assertEqual(expand("(-7a+1)^4"), "2401a^4-1372a^3+294a^2-28a+1")
    
    def test_expand_090(self):
        self.assertEqual(expand("(4k-2)^2"), "16k^2-16k+4")
    
    def test_expand_091(self):
        self.assertEqual(expand("(2j-10)^1"), "2j-10")
    
    def test_expand_092(self):
        self.assertEqual(expand("(7a+13)^2"), "49a^2+182a+169")
    
    def test_expand_093(self):
        self.assertEqual(expand("(3q+7)^1"), "3q+7")
    
    def test_expand_094(self):
        self.assertEqual(expand("(-8f-10)^0"), "1")
    
    def test_expand_095(self):
        self.assertEqual(expand("(j-15)^0"), "1")
    
    def test_expand_096(self):
        self.assertEqual(expand("(3c-12)^4"),
                         "81c^4-1296c^3+7776c^2-20736c+20736")
    
    def test_expand_097(self):
        self.assertEqual(expand("(2h+1)^5"), "32h^5+80h^4+80h^3+40h^2+10h+1")
    
    def test_expand_098(self):
        self.assertEqual(expand("(5r-16)^1"), "5r-16")
    
    def test_expand_099(self):
        self.assertEqual(expand("(t-11)^0"), "1")
    
    def test_expand_100(self):
        self.assertEqual(expand("(-10b+18)^5"),
                         "-100000b^5+900000b^4-3240000b^3+5832000b^2-5248800b"
                         "+1889568")
    
    def test_expand_101(self):
        self.assertEqual(expand("(9f-5)^5"),
                         "59049f^5-164025f^4+182250f^3-101250f^2+28125f-3125")
    
    def test_expand_102(self):
        self.assertEqual(expand("(2y+8)^0"), "1")
    
    def test_expand_103(self):
        self.assertEqual(expand("(-5c+12)^4"),
                         "625c^4-6000c^3+21600c^2-34560c+20736")
    
    def test_expand_104(self):
        self.assertEqual(expand("(-y+9)^4"), "y^4-36y^3+486y^2-2916y+6561")
    
    def test_expand_105(self):
        self.assertEqual(expand("(i+13)^2"), "i^2+26i+169")
    
    def test_expand_106(self):
        self.assertEqual(expand("(-2g-8)^2"), "4g^2+32g+64")
    
    def test_expand_107(self):
        self.assertEqual(expand("(v+19)^4"), "v^4+76v^3+2166v^2+27436v+130321")
    
    def test_expand_108(self):
        self.assertEqual(expand("(-7z-1)^3"), "-343z^3-147z^2-21z-1")
    
    def test_expand_109(self):
        self.assertEqual(expand("(-6f+20)^0"), "1")
    
    def test_expand_110(self):
        self.assertEqual(expand("(-10t-1)^0"), "1")
    
    def test_expand_111(self):
        self.assertEqual(expand("(-5e-7)^5"),
                         "-3125e^5-21875e^4-61250e^3-85750e^2-60025e-16807")
    
    def test_expand_112(self):
        self.assertEqual(expand("(5d+18)^2"), "25d^2+180d+324")
