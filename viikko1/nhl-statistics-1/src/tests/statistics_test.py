import unittest
from statistics import Statistics
from player_reader_stub import PlayerReaderStub


class TestStatistics(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.stats = Statistics(PlayerReaderStub)
        self.name_rallikuski = "TommiMakinen"
        self.name_hockey = "Kurri"
        self.maara = 3
        self.joukkue = "EDM" 

    def test_listalta_puuttuva_pelaaja_ei_löydy(self):
        self.assertEqual(self.stats.search(self.name_rallikuski),None)

    def test_listalle_oleva_pelaaja_löytyy(self):
        self.assertEqual(self.stats.search(self.name_hockey),"Kurri")
    
    def test_top_by_points_returns_right_number_of_players(self):
        self.assertEqual(len(self.stats.top(self.maara)), 3)

    def test_annetun_joukkueen_pelaajien_maara_palautetaan_oikein(self):
        self.assertEqual(len(self.stats.team(self.joukkue)),3)

    
