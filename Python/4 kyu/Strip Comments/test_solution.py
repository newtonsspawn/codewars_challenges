from unittest import TestCase

from solution import solution


class TestSolution(TestCase):
    
    def test_solution_01(self):
        self.assertEqual(
                solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                         ['#', '!']), "apples, pears\ngrapes\nbananas")
    
    def test_solution_02(self):
        self.assertEqual(solution("a #b\nc\nd $e f g", ['#', '$']), "a\nc\nd")
    
    def test_solution_03(self):
        self.assertEqual(
                solution(
                    "apples, pears # and bananas\ngrapes\nbananas !#apples",
                    ['#', '!']), "apples, pears\ngrapes\nbananas")
    
    def test_solution_04(self):
        self.assertEqual(
                solution(
                    "apples, pears # and bananas\ngrapes\nbananas #!apples",
                    ['#', '!']), "apples, pears\ngrapes\nbananas")
    
    def test_solution_05(self):
        self.assertEqual(
                solution("apples, pears # and bananas\ngrapes\navocado @apples",
                         ['@', '!']),
                "apples, pears # and bananas\ngrapes\navocado")
    
    def test_solution_06(self):
        self.assertEqual(
                solution("apples, pears § and bananas\ngrapes\navocado *apples",
                         ['*', '§']), "apples, pears\ngrapes\navocado")
    
    def test_solution_07(self):
        self.assertEqual(solution("", ['#', '!']), "")
    
    def test_solution_08(self):
        self.assertEqual(solution("#", ['#', '!']), "")
    
    def test_solution_09(self):
        self.assertEqual(solution("\n§", ['#', '§']), "\n")
    
    def test_solution_10(self):
        self.assertEqual(
                solution("apples, pears # and bananas\ngrapes\nbananas !apples",
                         []),
                "apples, pears # and bananas\ngrapes\nbananas !apples")
    
    def test_solution_11(self):
        self.assertEqual(solution(
                "cherries lemons cherries\nlemons strawberries\navocados pears "
                "apples",
                ['=', "'", '!', '@']),
                "cherries lemons cherries\nlemons "
                "strawberries\navocados pears apples")
    
    def test_solution_12(self):
        self.assertEqual(solution(
                ". strawberries apples watermelons\noranges\nstrawberries "
                "bananas\n= lemons ' bananas\ncherries strawberries bananas",
                ['^', '=', '#']),
                ". strawberries apples "
                "watermelons\noranges\nstrawberries "
                "bananas\n\ncherries strawberries bananas")
    
    def test_solution_13(self):
        self.assertEqual(solution(
                "watermelons watermelons apples\n# apples\noranges\nlemons "
                "bananas strawberries oranges =\n! bananas cherries bananas",
                ['?']),
                "watermelons watermelons apples\n# "
                "apples\noranges\nlemons bananas strawberries "
                "oranges =\n! bananas cherries bananas")
    
    def test_solution_14(self):
        self.assertEqual(solution(
                "lemons lemons oranges\nstrawberries avocados\ncherries @ "
                "pears\nstrawberries pears avocados pears cherries\napples "
                "watermelons pears bananas",
                ['#']),
                "lemons lemons oranges\nstrawberries "
                "avocados\ncherries @ pears\nstrawberries pears "
                "avocados pears cherries\napples watermelons pears "
                "bananas")
    
    def test_solution_15(self):
        self.assertEqual(solution(
                "oranges bananas oranges\navocados ?\nstrawberries\nbananas "
                "watermelons\npears oranges oranges pears",
                ['.', "'", '#', '?']),
                "oranges bananas "
                "oranges\navocados\nstrawberries\nbananas "
                "watermelons\npears oranges oranges pears")
    
    def test_solution_16(self):
        self.assertEqual(solution(
                "apples strawberries , avocados\n?\nwatermelons apples "
                "=\navocados # apples strawberries ' ",
                ['!', '=', ',', '.', '?']),
                "apples strawberries\n\nwatermelons apples\navocados "
                "# apples strawberries '")
    
    def test_solution_17(self):
        self.assertEqual(solution(
                "strawberries apples apples watermelons\ncherries pears "
                "pears\n^",
                ['.', "'", '@']),
                "strawberries apples apples watermelons\ncherries "
                "pears pears\n^")
    
    def test_solution_18(self):
        self.assertEqual(solution(
                "cherries apples apples\ncherries oranges watermelons\nbananas "
                "bananas\nbananas pears oranges\nstrawberries ' bananas",
                ['?', '-', "'", '.', ',', '!']),
                "cherries apples apples\ncherries oranges "
                "watermelons\nbananas bananas\nbananas pears "
                "oranges\nstrawberries")
    
    def test_solution_19(self):
        self.assertEqual(solution(
                "bananas bananas apples lemons @ watermelons\nlemons "
                "strawberries "
                "apples watermelons\navocados lemons ' oranges\noranges apples "
                "bananas\nbananas ' cherries -",
                ['=', '#', "'", '?', '-', ',', '^', '.']),
                "bananas bananas apples lemons @ watermelons\nlemons "
                "strawberries apples watermelons\navocados "
                "lemons\noranges apples bananas\nbananas")
    
    def test_solution_20(self):
        self.assertEqual(solution(
                "bananas bananas lemons\n. apples apples lemons apples\n= "
                "strawberries - pears\napples cherries bananas\nwatermelons "
                "lemons lemons strawberries pears",
                ['.', '^', "'", '?']),
                "bananas bananas lemons\n\n= strawberries - "
                "pears\napples cherries bananas\nwatermelons lemons "
                "lemons strawberries pears")
    
    def test_solution_21(self):
        self.assertEqual(solution(
                "watermelons @\nlemons . bananas bananas lemons cherries\n# "
                "cherries pears\ncherries ^ oranges avocados\navocados",
                ['-', '?', ',', '.', '^']),
                "watermelons @\nlemons\n# cherries "
                "pears\ncherries\navocados")
    
    def test_solution_22(self):
        self.assertEqual(solution(
                "- ?\npears oranges ! @ avocados\n= oranges = apples\napples "
                "avocados strawberries",
                ['-', '^', '?']),
                "\npears oranges ! @ avocados\n= oranges = "
                "apples\napples avocados strawberries")
    
    def test_solution_23(self):
        self.assertEqual(solution(
                "pears bananas watermelons pears cherries\napples avocados ^ "
                "cherries\noranges oranges",
                ['=', "'", ',', '.', '!', '@']),
                "pears bananas watermelons pears cherries\napples "
                "avocados ^ cherries\noranges oranges")
    
    def test_solution_24(self):
        self.assertEqual(solution(
                "^ oranges\nbananas @ pears avocados apples "
                "watermelons\ncherries "
                "bananas",
                ['-', '!', ',', '^', '?', '=']),
                "\nbananas @ pears avocados apples "
                "watermelons\ncherries bananas")
    
    def test_solution_25(self):
        self.assertEqual(solution(
                "lemons pears cherries\nlemons ! watermelons !\nstrawberries ! "
                "oranges watermelons\n^ pears bananas bananas bananas\npears "
                "bananas apples ?",
                ['.', '^', '-', '=', ',', '?', "'"]),
                "lemons pears cherries\nlemons ! watermelons "
                "!\nstrawberries ! oranges watermelons\n\npears "
                "bananas apples")
    
    def test_solution_26(self):
        self.assertEqual(solution(
                "bananas oranges avocados watermelons strawberries\n, "
                "oranges\npears\npears",
                ["'", '?', ',', '.']),
                "bananas oranges avocados watermelons "
                "strawberries\n\npears\npears")
    
    def test_solution_27(self):
        self.assertEqual(solution(
                "pears avocados cherries .\nlemons , avocados\nwatermelons "
                "avocados strawberries",
                []),
                "pears avocados cherries .\nlemons , "
                "avocados\nwatermelons avocados strawberries")
    
    def test_solution_28(self):
        self.assertEqual(solution(
                "apples pears pears oranges watermelons\napples\napples "
                "oranges\npears avocados oranges\nwatermelons - ! avocados "
                "watermelons avocados",
                ['?', '#', '.', '=', '-', '!', "'"]),
                "apples pears pears oranges "
                "watermelons\napples\napples oranges\npears avocados "
                "oranges\nwatermelons")
    
    def test_solution_29(self):
        self.assertEqual(solution(
                "cherries pears lemons - pears strawberries\noranges cherries "
                "lemons pears\nstrawberries avocados bananas = ^ watermelons",
                ['!', '#', '@', '-', '^', '?', '=', "'"]),
                "cherries pears lemons\noranges cherries lemons "
                "pears\nstrawberries avocados bananas")
    
    def test_solution_30(self):
        self.assertEqual(solution(
                "oranges pears lemons @ watermelons\n. oranges strawberries "
                "strawberries apples apples\napples pears",
                ['?', '.', '=', '@', ',', "'", '^', '#', '-']),
                "oranges pears lemons\n\napples pears")
    
    def test_solution_31(self):
        self.assertEqual(solution(
                "bananas lemons # bananas\npears watermelons avocados = "
                "cherries\noranges pears bananas apples avocados ?\npears =",
                ['?', '#', ',', '^', '@', "'", '-', '.', '=']),
                "bananas lemons\npears watermelons avocados\noranges "
                "pears bananas apples avocados\npears")
    
    def test_solution_32(self):
        self.assertEqual(solution(
                "#\nlemons strawberries strawberries lemons\nstrawberries "
                "lemons "
                ", !\navocados avocados",
                ['#', '!', '^', '-', '=', '@', '?', ',']),
                "\nlemons strawberries strawberries "
                "lemons\nstrawberries lemons\navocados avocados")
    
    def test_solution_33(self):
        self.assertEqual(solution(
                "# !\n- watermelons watermelons .\noranges\n? cherries "
                "cherries",
                ['.', '^', '#', "'", ',', '@', '?']),
                "\n- watermelons watermelons\noranges\n")
    
    def test_solution_34(self):
        self.assertEqual(solution(
                "= avocados\navocados lemons bananas bananas ,\nwatermelons "
                "strawberries # bananas bananas apples\nwatermelons pears "
                "strawberries strawberries pears watermelons\npears avocados "
                "apples pears",
                ['@', '-', '#', '!', '^', '?', ',', "'"]),
                "= avocados\navocados lemons bananas "
                "bananas\nwatermelons strawberries\nwatermelons "
                "pears strawberries strawberries pears "
                "watermelons\npears avocados apples pears")
    
    def test_solution_35(self):
        self.assertEqual(solution(
                "oranges . watermelons lemons\npears\noranges lemons bananas -",
                ['-', ',', '@', '=', '.']),
                "oranges\npears\noranges lemons bananas")
    
    def test_solution_36(self):
        self.assertEqual(solution(
                "apples cherries strawberries\n? watermelons ^ strawberries "
                "strawberries\noranges watermelons bananas - lemons",
                ['^', '=', '-', '.']),
                "apples cherries strawberries\n? "
                "watermelons\noranges watermelons bananas")
    
    def test_solution_37(self):
        self.assertEqual(solution(
                "watermelons\n# = apples ,\n^ lemons apples\nlemons pears "
                "lemons "
                "cherries\noranges apples",
                ['#', '?', '!']),
                "watermelons\n\n^ lemons apples\nlemons pears lemons "
                "cherries\noranges apples")
    
    def test_solution_38(self):
        self.assertEqual(solution(
                "cherries oranges\npears cherries "
                "apples\nstrawberries\nstrawberries apples = - bananas bananas",
                []),
                "cherries oranges\npears cherries "
                "apples\nstrawberries\nstrawberries apples = - "
                "bananas bananas")
    
    def test_solution_39(self):
        self.assertEqual(solution(
                "apples\n. apples lemons oranges bananas bananas\n? "
                "?\nstrawberries apples strawberries",
                ['-', '?', '@', '=']),
                "apples\n. apples lemons oranges bananas "
                "bananas\n\nstrawberries apples strawberries")
    
    def test_solution_40(self):
        self.assertEqual(solution(
                "bananas\ncherries\napples oranges cherries\nstrawberries "
                "lemons "
                "apples ^ # lemons\nbananas pears strawberries pears "
                "watermelons "
                "pears",
                [',', '^', '?', '@']),
                "bananas\ncherries\napples oranges "
                "cherries\nstrawberries lemons apples\nbananas pears "
                "strawberries pears watermelons pears")
    
    def test_solution_41(self):
        self.assertEqual(solution(
                "apples bananas\nbananas watermelons watermelons cherries "
                "oranges\navocados watermelons avocados bananas "
                "apples\ncherries "
                "strawberries pears lemons",
                []),
                "apples bananas\nbananas watermelons watermelons "
                "cherries oranges\navocados watermelons avocados "
                "bananas apples\ncherries strawberries pears lemons")
    
    def test_solution_42(self):
        self.assertEqual(solution(
                "strawberries cherries strawberries\nwatermelons\navocados "
                "avocados pears\n!\nstrawberries # . watermelons",
                ['#', "'", '!', '^', '-', ',']),
                "strawberries cherries "
                "strawberries\nwatermelons\navocados avocados "
                "pears\n\nstrawberries")
    
    def test_solution_43(self):
        self.assertEqual(solution(
                "watermelons\nbananas lemons ? = @\n? watermelons strawberries "
                "lemons",
                ['!', "'", '-', '#', '?', ',']),
                "watermelons\nbananas lemons\n")
    
    def test_solution_44(self):
        self.assertEqual(solution(
                "strawberries cherries cherries\nlemons oranges avocados "
                "pears = "
                "avocados\npears oranges\npears lemons lemons lemons "
                "watermelons\n,",
                [',', "'", '=', '#', '.', '-', '?', '@']),
                "strawberries cherries cherries\nlemons oranges avocados "
                "pears\npears oranges\npears lemons lemons lemons "
                "watermelons\n")
    
    def test_solution_45(self):
        self.assertEqual(
                solution("lemons apples -\n' @\nlemons oranges avocados",
                         ['@', '^', '#', '-', '!']),
                "lemons apples\n'\nlemons oranges avocados")
    
    def test_solution_46(self):
        self.assertEqual(solution(
                "lemons ? oranges avocados apples ^\n! strawberries pears "
                "strawberries @ lemons\napples = avocados",
                [',', '?', '!', '=']), "lemons\n\napples")
    
    def test_solution_47(self):
        self.assertEqual(solution("bananas ,\npears\nwatermelons\n' ^ # ?",
                                  ['#', '@', '^', '=', '!']),
                         "bananas ,\npears\nwatermelons\n'")
    
    def test_solution_48(self):
        self.assertEqual(solution(
                "apples = ^\n- = !\nwatermelons watermelons lemons . "
                "lemons\napples bananas avocados lemons avocados",
                ['#', '=', '@', '!']),
                "apples\n-\nwatermelons watermelons lemons . lemons\napples "
                "bananas avocados lemons avocados")
    
    def test_solution_49(self):
        self.assertEqual(solution(
                "- ! strawberries watermelons pears strawberries\napples "
                "avocados ^ oranges\napples watermelons apples ! bananas "
                "lemons\noranges bananas",
                ['?', '-', '#', '=', '.', '^', "'", ',', '!']),
                "\napples avocados\napples watermelons apples\noranges bananas")
    
    def test_solution_50(self):
        self.assertEqual(solution(
                "cherries cherries apples cherries bananas\navocados ? "
                "bananas pears lemons !\nwatermelons\n. apples lemons oranges "
                "watermelons watermelons",
                ['#']),
                "cherries cherries apples cherries bananas\navocados ? "
                "bananas pears lemons !\nwatermelons\n. apples lemons oranges "
                "watermelons watermelons")
