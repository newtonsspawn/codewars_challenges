from unittest import TestCase

from vasya_clerk import tickets


class TestTickets(TestCase):
    def test_tickets_01(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")

    def test_tickets_02(self):
        self.assertEqual(tickets([25, 100]), "NO")