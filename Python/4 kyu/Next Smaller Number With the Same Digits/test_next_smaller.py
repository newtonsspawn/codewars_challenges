from unittest import TestCase

from nextsmaller import next_smaller


class TestNextSmaller(TestCase):
    
    def test_next_smaller_01(self):
        self.assertEqual(next_smaller(907), 790)
    
    def test_next_smaller_02(self):
        self.assertEqual(next_smaller(21), 12)
    
    def test_next_smaller_03(self):
        self.assertEqual(next_smaller(531), 513)
    
    def test_next_smaller_04(self):
        self.assertEqual(next_smaller(1027), -1)
    
    def test_next_smaller_05(self):
        self.assertEqual(next_smaller(441), 414)
    
    def test_next_smaller_06(self):
        self.assertEqual(next_smaller(123456798), 123456789)
    
    def test_next_smaller_07(self):
        self.assertEqual(next_smaller(513), 351)
    
    def test_next_smaller_08(self):
        self.assertEqual(next_smaller(351), 315)
    
    def test_next_smaller_09(self):
        self.assertEqual(next_smaller(315), 153)
    
    def test_next_smaller_10(self):
        self.assertEqual(next_smaller(153), 135)
    
    def test_next_smaller_11(self):
        self.assertEqual(next_smaller(135), -1)
    
    def test_next_smaller_12(self):
        self.assertEqual(next_smaller(100), -1)
    
    def test_next_smaller_13(self):
        self.assertEqual(next_smaller(2071), 2017)
    
    def test_next_smaller_14(self):
        self.assertEqual(next_smaller(1207), 1072)
    
    def test_next_smaller_15(self):
        self.assertEqual(next_smaller(414), 144)
    
    def test_next_smaller_16(self):
        self.assertEqual(next_smaller(123456789), -1)
    
    def test_next_smaller_17(self):
        self.assertEqual(next_smaller(29009), 20990)
    
    def test_next_smaller_18(self):
        self.assertEqual(next_smaller(1234567908), 1234567890)
    
    def test_next_smaller_19(self):
        self.assertEqual(next_smaller(9999999999), -1)
    
    def test_next_smaller_20(self):
        self.assertEqual(next_smaller(59884848483559), 59884848459853)
    
    def test_next_smaller_21(self):
        self.assertEqual(next_smaller(1023456789), -1)
    
    def test_next_smaller_22(self):
        self.assertEqual(next_smaller(51226262651257), 51226262627551)
    
    def test_next_smaller_23(self):
        self.assertEqual(next_smaller(202233445566), -1)
    
    def test_next_smaller_24(self):
        self.assertEqual(next_smaller(506789), -1)
    
    def test_next_smaller_25(self):
        self.assertEqual(next_smaller(26877994102587), 26877994102578)
    
    def test_next_smaller_26(self):
        self.assertEqual(next_smaller(767552255677), 767527765552)
    
    def test_next_smaller_27(self):
        self.assertEqual(next_smaller(84089730347889), 84089709887433)
    
    def test_next_smaller_28(self):
        self.assertEqual(next_smaller(19759037663779930133356677779999),
                         19759037663779919999777766533330)
    
    def test_next_smaller_29(self):
        self.assertEqual(next_smaller(9013996401346999), 9013996399964410)
    
    def test_next_smaller_30(self):
        self.assertEqual(next_smaller(4289322), 4289232)
    
    def test_next_smaller_31(self):
        self.assertEqual(next_smaller(2091669108283500112235668899),
                         2091669108283399886655221100)
    
    def test_next_smaller_32(self):
        self.assertEqual(next_smaller(96262669), 96229666)
    
    def test_next_smaller_33(self):
        self.assertEqual(next_smaller(6446), 4664)
    
    def test_next_smaller_34(self):
        self.assertEqual(next_smaller(253701903001233579), 253701902975333100)
    
    def test_next_smaller_35(self):
        self.assertEqual(next_smaller(11383017276870990), 11383017276870909)
    
    def test_next_smaller_36(self):
        self.assertEqual(next_smaller(8415712667508876801124556667778888),
                         8415712667508876788888776665542110)
    
    def test_next_smaller_37(self):
        self.assertEqual(next_smaller(1919), 1199)
    
    def test_next_smaller_38(self):
        self.assertEqual(next_smaller(329239), 323992)
    
    def test_next_smaller_39(self):
        self.assertEqual(next_smaller(1382216060102935400011122233456689),
                         1382216060102935398665443222111000)
    
    def test_next_smaller_40(self):
        self.assertEqual(next_smaller(210055144909534496), 210055144909534469)
    
    def test_next_smaller_41(self):
        self.assertEqual(next_smaller(34292242223449), 34292239444222)
    
    def test_next_smaller_42(self):
        self.assertEqual(next_smaller(284010256001224568), 284010255866422100)
    
    def test_next_smaller_43(self):
        self.assertEqual(next_smaller(281549383339413112333334458899),
                         281549383339412998854433333311)
    
    def test_next_smaller_44(self):
        self.assertEqual(next_smaller(103400846869000134466889),
                         103400846868998664431000)
    
    def test_next_smaller_45(self):
        self.assertEqual(next_smaller(85638798548640416), 85638798548640164)
    
    def test_next_smaller_46(self):
        self.assertEqual(next_smaller(2428871073701223477788),
                         2428871073488777732210)
    
    def test_next_smaller_47(self):
        self.assertEqual(next_smaller(1818864032401123446888),
                         1818864032388864442110)
    
    def test_next_smaller_48(self):
        self.assertEqual(next_smaller(5069529808100125568899),
                         5069529808099886552110)
    
    def test_next_smaller_49(self):
        self.assertEqual(next_smaller(4646), 4466)
    
    def test_next_smaller_50(self):
        self.assertEqual(next_smaller(72), 27)
    
    def test_next_smaller_51(self):
        self.assertEqual(next_smaller(20240968870349775360002233445667778899),
                         20240968870349775359988777666443322000)
    
    def test_next_smaller_52(self):
        self.assertEqual(next_smaller(8203066800236688), 8203066688863200)
    
    def test_next_smaller_53(self):
        self.assertEqual(next_smaller(34278524224029050880002222234445578889),
                         34278524224029050879888855444322222000)
    
    def test_next_smaller_54(self):
        self.assertEqual(next_smaller(23900239), 23399200)
    
    def test_next_smaller_55(self):
        self.assertEqual(next_smaller(98297233818), 98297233188)
    
    def test_next_smaller_56(self):
        self.assertEqual(next_smaller(19281289), 19229881)
    
    def test_next_smaller_57(self):
        self.assertEqual(next_smaller(338058071173257152001112233355577788),
                         338058071173257151887775553332221100)
    
    def test_next_smaller_58(self):
        self.assertEqual(next_smaller(9016302091900011236999),
                         9016302091699993211000)
    
    def test_next_smaller_59(self):
        self.assertEqual(next_smaller(292377763317492992122223334677779999),
                         292377763317492991999977776433322222)
    
    def test_next_smaller_60(self):
        self.assertEqual(next_smaller(65252), 65225)
    
    def test_next_smaller_61(self):
        self.assertEqual(next_smaller(274201406001224467), 274201404766422100)
    
    def test_next_smaller_62(self):
        self.assertEqual(next_smaller(9901158401145899), 9901158199854410)
    
    def test_next_smaller_63(self):
        self.assertEqual(next_smaller(11533056473164010011113334455667),
                         11533056473164007665544333111110)
    
    def test_next_smaller_64(self):
        self.assertEqual(next_smaller(3414902401234449), 3414902394444210)
    
    def test_next_smaller_65(self):
        self.assertEqual(next_smaller(152858162453353632), 152858162453353623)
    
    def test_next_smaller_66(self):
        self.assertEqual(next_smaller(3687656767223566667778),
                         3687656766877776665322)
    
    def test_next_smaller_67(self):
        self.assertEqual(next_smaller(178080001788), 178078881000)
    
    def test_next_smaller_68(self):
        self.assertEqual(next_smaller(3505565303355556), 3505565065555333)
    
    def test_next_smaller_69(self):
        self.assertEqual(next_smaller(7337), 3773)
    
    def test_next_smaller_70(self):
        self.assertEqual(next_smaller(3930792496933724), 3930792496933472)
    
    def test_next_smaller_71(self):
        self.assertEqual(next_smaller(263949208022346899), 263949206998843220)
    
    def test_next_smaller_72(self):
        self.assertEqual(next_smaller(2002), -1)
    
    def test_next_smaller_73(self):
        self.assertEqual(next_smaller(4980313701334789), 4980313498773310)
    
    def test_next_smaller_74(self):
        self.assertEqual(next_smaller(91608510115689), 91608509865111)
