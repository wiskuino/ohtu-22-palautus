import unittest
from statistics import Statistics
from player_reader_stub import PlayerReaderStub


class TestStatistics(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.stats = Statistics(PlayerReaderStub)
        self.name = "TommiMakinen"

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_if_player_name_not_in_list(self):
        self.assertEqual(self.stats.search(self.name),None)
