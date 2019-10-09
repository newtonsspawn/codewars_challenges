from unittest import TestCase
from diff import diff


class TestDiffs(TestCase):

    def test_diff_01(self):
        self.assertIn(diff("(tan x)"),
                      [
                              '(+ 1 (^ (tan x) 2))',
                              '(^ (cos x) -2)',
                              '(/ 1 (^ (cos x) 2))'
                      ])
    
    def test_diff_02(self):
        self.assertEqual(diff("5"), '0')
    
    def test_diff_03(self):
        self.assertEqual(diff("x"), '1')
    
    def test_diff_04(self):
        self.assertEqual(diff("(+ x x)"), '2')
    
    def test_diff_05(self):
        self.assertEqual(diff("(- x x)"), '0')
    
    def test_diff_06(self):
        self.assertEqual(diff("(* x 2)"), '2')
    
    def test_diff_07(self):
        self.assertEqual(diff("(/ x 2)"), '0.5')
    
    def test_diff_08(self):
        self.assertEqual(diff("(^ x 2)"), '(* 2 x)')
    
    def test_diff_09(self):
        self.assertEqual(diff("(cos x)"), '(* -1 (sin x))')
    
    def test_diff_10(self):
        self.assertEqual(diff("(sin x)"), '(cos x)')
    
    def test_diff_11(self):
        self.assertEqual(diff("(exp x)"), '(exp x)')
    
    def test_diff_12(self):
        self.assertEqual(diff("(ln x)"), '(/ 1 x)')
    
    def test_diff_13(self):
        self.assertEqual(diff("(+ x (+ x x))"), '3')
    
    def test_diff_14(self):
        self.assertEqual(diff("(- (+ x x) x)"), '1')
    
    def test_diff_15(self):
        self.assertEqual(diff("(* 2 (+ x 2))"), '2')
    
    def test_diff_16(self):
        self.assertEqual(diff("(/ 2 (+ 1 x))"), '(/ -2 (^ (+ 1 x) 2))')
    
    def test_diff_17(self):
        self.assertEqual(diff("(cos (+ x 1))"), '(* -1 (sin (+ x 1)))')
    
    def test_diff_18(self):
        self.assertEqual(diff("(sin (+ x 1))"), '(cos (+ x 1))')
    
    def test_diff_19(self):
        self.assertEqual(diff("(sin (* 2 x))"), '(* 2 (cos (* 2 x)))')
    
    def test_diff_20(self):
        self.assertEqual(diff("(exp (* 2 x))"), '(* 2 (exp (* 2 x)))')
    
    def test_diff_21(self):
        self.assertIn(diff("(tan (* 2 x))"),
                      [
                              '(* 2 (+ 1 (^ (tan (* 2 x)) 2)))',
                              '(* 2 (^ (cos (* 2 x)) -2))',
                              '(/ 2 (^ (cos (* 2 x)) 2))'
                      ])
    
    def test_diff_22(self):
        self.assertIn(diff("(cos (* 2 x))"),
                      [
                              '* 2 (* -1 (sin (* 2 x))))',
                              '(* -2 (sin (* 2 x)))'
                      ])
    
    # second derivative
    def test_diff_23(self):
        self.assertEqual(diff(diff("(sin x)")), '(* -1 (sin x))')

    # second derivative
    def test_diff_24(self):
        self.assertEqual(diff(diff("(exp x)")), '(exp x)')

    # second derivative
    def test_diff_25(self):
        self.assertIn(diff(diff("(^ x 3)")),
                      [
                              '(* 3 (* 2 x))',
                              '(* 6 x)'
                      ])
    
    def test_diff_26(self):
        self.assertEqual(diff("41"), '0')
    
    def test_diff_27(self):
        self.assertEqual(diff("(* x 41)"), '41')
    
    def test_diff_28(self):
        self.assertEqual(diff("(cos (+ x 41))"), '(* -1 (sin (+ x 41)))')
    
    def test_diff_29(self):
        self.assertEqual(diff("(sin (* 41 x))"), '(* 41 (cos (* 41 x)))')
    
    def test_diff_30(self):
        self.assertEqual(diff("(exp (* 41 x))"), '(* 41 (exp (* 41 x)))')
    
    def test_diff_31(self):
        self.assertIn(diff("(cos (* 41 x))"),
                      [
                              '* 41 (* -1 (sin (* 41 x))))',
                              '(* -41 (sin (* 41 x)))'
                      ])
    
    def test_diff_32(self):
        self.assertIn(diff("(tan (* 41 x))"),
                      [
                              '(* 41 (+ 1 (^ (tan (* 41 x)) 2)))',
                              '(* 41 (^ (cos (* 41 x)) -2))',
                              '(/ 41 (^ (cos (* 41 x)) 2))'
                      ])
    
    def test_diff_33(self):
        self.assertEqual(diff("88"), '0')
    
    def test_diff_34(self):
        self.assertEqual(diff("(* x 88)"), '88')
    
    def test_diff_35(self):
        self.assertEqual(diff("(cos (+ x 88))"), '(* -1 (sin (+ x 88)))')
    
    def test_diff_36(self):
        self.assertEqual(diff("(sin (* 88 x))"), '(* 88 (cos (* 88 x)))')
    
    def test_diff_37(self):
        self.assertEqual(diff("(exp (* 88 x))"), '(* 88 (exp (* 88 x)))')
    
    def test_diff_38(self):
        self.assertIn(diff("(cos (* 88 x))"),
                      [
                              '* 88 (* -1 (sin (* 88 x))))',
                              '(* -88 (sin (* 88 x)))'
                      ])
    
    def test_diff_39(self):
        self.assertIn(diff("(tan (* 88 x))"),
                      [
                              '(* 88 (+ 1 (^ (tan (* 88 x)) 2)))',
                              '(* 88 (^ (cos (* 88 x)) -2))',
                              '(/ 88 (^ (cos (* 88 x)) 2))'
                      ])
    
    def test_diff_40(self):
        self.assertEqual(diff("11"), '0')
    
    def test_diff_41(self):
        self.assertEqual(diff("(* x 11)"), '11')
    
    def test_diff_42(self):
        self.assertEqual(diff("(cos (+ x 11))"), '(* -1 (sin (+ x 11)))')
    
    def test_diff_43(self):
        self.assertEqual(diff("(sin (* 11 x))"), '(* 11 (cos (* 11 x)))')
    
    def test_diff_44(self):
        self.assertEqual(diff("(exp (* 11 x))"), '(* 11 (exp (* 11 x)))')
    
    def test_diff_45(self):
        self.assertIn(diff("(cos (* 11 x))"),
                      [
                              '* 11 (* -1 (sin (* 11 x))))',
                              '(* -11 (sin (* 11 x)))'
                      ])
    
    def test_diff_46(self):
        self.assertIn(diff("(tan (* 11 x))"),
                      [
                              '(* 11 (+ 1 (^ (tan (* 11 x)) 2)))',
                              '(* 11 (^ (cos (* 11 x)) -2))',
                              '(/ 11 (^ (cos (* 11 x)) 2))'
                      ])
    
    def test_diff_47(self):
        self.assertEqual(diff("27"), '0')
    
    def test_diff_48(self):
        self.assertEqual(diff("(* x 27)"), '27')
    
    def test_diff_49(self):
        self.assertEqual(diff("(cos (+ x 27))"), '(* -1 (sin (+ x 27)))')
    
    def test_diff_50(self):
        self.assertEqual(diff("(sin (* 27 x))"), '(* 27 (cos (* 27 x)))')
    
    def test_diff_51(self):
        self.assertEqual(diff("(exp (* 27 x))"), '(* 27 (exp (* 27 x)))')
    
    def test_diff_52(self):
        self.assertIn(diff("(cos (* 27 x))"),
                      [
                              '* 27 (* -1 (sin (* 27 x))))',
                              '(* -27 (sin (* 27 x)))'
                      ])
    
    def test_diff_53(self):
        self.assertIn(diff("(tan (* 27 x))"),
                      [
                              '(* 27 (+ 1 (^ (tan (* 27 x)) 2)))',
                              '(* 27 (^ (cos (* 27 x)) -2))',
                              '(/ 27 (^ (cos (* 27 x)) 2))'
                      ])
    
    def test_diff_54(self):
        self.assertEqual(diff("65"), '0')
    
    def test_diff_55(self):
        self.assertEqual(diff("(* x 65)"), '65')
    
    def test_diff_56(self):
        self.assertEqual(diff("(cos (+ x 65))"), '(* -1 (sin (+ x 65)))')
    
    def test_diff_57(self):
        self.assertEqual(diff("(sin (* 65 x))"), '(* 65 (cos (* 65 x)))')
    
    def test_diff_58(self):
        self.assertEqual(diff("(exp (* 65 x))"), '(* 65 (exp (* 65 x)))')
    
    def test_diff_59(self):
        self.assertIn(diff("(cos (* 65 x))"),
                      [
                              '* 65 (* -1 (sin (* 65 x))))',
                              '(* -65 (sin (* 65 x)))'
                      ])
    
    def test_diff_60(self):
        self.assertIn(diff("(tan (* 65 x))"),
                      [
                              '(* 65 (+ 1 (^ (tan (* 65 x)) 2)))',
                              '(* 65 (^ (cos (* 65 x)) -2))',
                              '(/ 65 (^ (cos (* 65 x)) 2))'
                      ])
    
    def test_diff_61(self):
        self.assertEqual(diff("42"), '0')
    
    def test_diff_62(self):
        self.assertEqual(diff("(* x 42)"), '42')
    
    def test_diff_63(self):
        self.assertEqual(diff("(cos (+ x 42))"), '(* -1 (sin (+ x 42)))')
    
    def test_diff_64(self):
        self.assertEqual(diff("(sin (* 42 x))"), '(* 42 (cos (* 42 x)))')
    
    def test_diff_65(self):
        self.assertEqual(diff("(exp (* 42 x))"), '(* 42 (exp (* 42 x)))')
    
    def test_diff_66(self):
        self.assertIn(diff("(cos (* 42 x))"),
                      [
                              '* 42 (* -1 (sin (* 42 x))))',
                              '(* -42 (sin (* 42 x)))'
                      ])
    
    def test_diff_67(self):
        self.assertIn(diff("(tan (* 42 x))"),
                      [
                              '(* 42 (+ 1 (^ (tan (* 42 x)) 2)))',
                              '(* 42 (^ (cos (* 42 x)) -2))',
                              '(/ 42 (^ (cos (* 42 x)) 2))'
                      ])
    
    def test_diff_68(self):
        self.assertEqual(diff("78"), '0')
    
    def test_diff_69(self):
        self.assertEqual(diff("(* x 78)"), '78')
    
    def test_diff_70(self):
        self.assertEqual(diff("(cos (+ x 78))"), '(* -1 (sin (+ x 78)))')
    
    def test_diff_71(self):
        self.assertEqual(diff("(sin (* 78 x))"), '(* 78 (cos (* 78 x)))')
    
    def test_diff_72(self):
        self.assertEqual(diff("(exp (* 78 x))"), '(* 78 (exp (* 78 x)))')
    
    def test_diff_73(self):
        self.assertIn(diff("(cos (* 78 x))"),
                      [
                              '* 78 (* -1 (sin (* 78 x))))',
                              '(* -78 (sin (* 78 x)))'
                      ])
    
    def test_diff_74(self):
        self.assertIn(diff("(tan (* 78 x))"),
                      [
                              '(* 78 (+ 1 (^ (tan (* 78 x)) 2)))',
                              '(* 78 (^ (cos (* 78 x)) -2))',
                              '(/ 78 (^ (cos (* 78 x)) 2))'
                      ])
    
    def test_diff_75(self):
        self.assertEqual(diff("15"), '0')
    
    def test_diff_76(self):
        self.assertEqual(diff("(* x 15)"), '15')
    
    def test_diff_77(self):
        self.assertEqual(diff("(cos (+ x 15))"), '(* -1 (sin (+ x 15)))')
    
    def test_diff_78(self):
        self.assertEqual(diff("(sin (* 15 x))"), '(* 15 (cos (* 15 x)))')
    
    def test_diff_79(self):
        self.assertEqual(diff("(exp (* 15 x))"), '(* 15 (exp (* 15 x)))')
    
    def test_diff_80(self):
        self.assertIn(diff("(cos (* 15 x))"),
                      [
                              '(* 15 (* -1 (sin (* 15 x))))',
                              '(* -15 (sin (* 15 x)))'
                      ])
    
    def test_diff_81(self):
        self.assertIn(diff("(tan (* 15 x))"),
                      [
                              '(* 15 (+ 1 (^ (tan (* 15 x)) 2)))',
                              '(* 15 (^ (cos (* 15 x)) -2))',
                              '(/ 15 (^ (cos (* 15 x)) 2))'
                      ])
    
    def test_diff_82(self):
        self.assertEqual(diff("64"), '0')
    
    def test_diff_83(self):
        self.assertEqual(diff("(* x 64)"), '64')
    
    def test_diff_84(self):
        self.assertEqual(diff("(cos (+ x 64))"), '(* -1 (sin (+ x 64)))')
    
    def test_diff_85(self):
        self.assertEqual(diff("(sin (* 64 x))"), '(* 64 (cos (* 64 x)))')
    
    def test_diff_86(self):
        self.assertEqual(diff("(exp (* 64 x))"), '(* 64 (exp (* 64 x)))')
    
    def test_diff_87(self):
        self.assertIn(diff("(cos (* 64 x))"),
                      [
                              '* 64 (* -1 (sin (* 64 x))))',
                              '(* -64 (sin (* 64 x)))'
                      ])
    
    def test_diff_88(self):
        self.assertIn(diff("(tan (* 64 x))"),
                      [
                              '(* 64 (+ 1 (^ (tan (* 64 x)) 2)))',
                              '(* 64 (^ (cos (* 64 x)) -2))',
                              '(/ 64 (^ (cos (* 64 x)) 2))'
                      ])
    
    def test_diff_89(self):
        self.assertEqual(diff("40"), '0')
    
    def test_diff_90(self):
        self.assertEqual(diff("(* x 40)"), '40')
    
    def test_diff_91(self):
        self.assertEqual(diff("(cos (+ x 40))"), '(* -1 (sin (+ x 40)))')
    
    def test_diff_92(self):
        self.assertEqual(diff("(sin (* 40 x))"), '(* 40 (cos (* 40 x)))')
    
    def test_diff_93(self):
        self.assertEqual(diff("(exp (* 40 x))"), '(* 40 (exp (* 40 x)))')
    
    def test_diff_94(self):
        self.assertIn(diff("(cos (* 40 x))"),
                      [
                              '* 40 (* -1 (sin (* 40 x))))',
                              '(* -40 (sin (* 40 x)))'
                      ])
    
    def test_diff_95(self):
        self.assertIn(diff("(tan (* 40 x))"),
                      [
                              '(* 40 (+ 1 (^ (tan (* 40 x)) 2)))',
                              '(* 40 (^ (cos (* 40 x)) -2))',
                              '(/ 40 (^ (cos (* 40 x)) 2))'
                      ])
