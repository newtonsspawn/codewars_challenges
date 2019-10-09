from unittest import TestCase

from humanreadabletime import make_readable


class TestMakeReadable(TestCase):
    def test_make_readable_01(self):
        self.assertEqual(make_readable(0), "00:00:00")

    def test_make_readable_02(self):
        self.assertEqual(make_readable(5), "00:00:05")

    def test_make_readable_03(self):
        self.assertEqual(make_readable(60), "00:01:00")

    def test_make_readable_04(self):
        self.assertEqual(make_readable(86399), "23:59:59")

    def test_make_readable_05(self):
        self.assertEqual(make_readable(359999), "99:59:59")