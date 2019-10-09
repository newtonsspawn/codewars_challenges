from unittest import TestCase

from formatduration import format_duration


class TestFormatDuration(TestCase):
    
    def test_format_duration_01(self):
        self.assertEqual(format_duration(0), "now")
    
    def test_format_duration_02(self):
        self.assertEqual(format_duration(1), "1 second")
        
    def test_format_duration_03(self):
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")

    def test_format_duration_04(self):
        self.assertEqual(format_duration(120), "2 minutes")

    def test_format_duration_05(self):
        self.assertEqual(format_duration(3600), "1 hour")

    def test_format_duration_06(self):
        self.assertEqual(format_duration(3662),
                         "1 hour, 1 minute and 2 seconds")

    def test_format_duration_07(self):
        self.assertEqual(format_duration(15731080), 
                         "182 days, 1 hour, 44 minutes and 40 seconds")
    
    def test_format_duration_08(self):
        self.assertEqual(format_duration(132030240),
                         "4 years, 68 days, 3 hours and 4 minutes")
    
    def test_format_duration_09(self):
        self.assertEqual(format_duration(205851834),
                         "6 years, 192 days, 13 hours, 3 minutes and 54 "
                         "seconds")
    
    def test_format_duration_10(self):
        self.assertEqual(format_duration(253374061),
                         "8 years, 12 days, 13 hours, 41 minutes and 1 second")
    
    def test_format_duration_11(self):
        self.assertEqual(format_duration(242062374),
                         "7 years, 246 days, 15 hours, 32 minutes and 54 "
                         "seconds")
    
    def test_format_duration_12(self):
        self.assertEqual(format_duration(101956166),
                         "3 years, 85 days, 1 hour, 9 minutes and 26 seconds")
    
    def test_format_duration_13(self):
        self.assertEqual(format_duration(33243586),
                         "1 year, 19 days, 18 hours, 19 minutes and 46 "
                         "seconds")
