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
        self.yksi_top = 1
        self.joukkue = "EDM" 

    def test_rally_driver_can_not_found_on_the_list(self):
        self.assertEqual(self.stats.search(self.name_rallikuski),None)

    def test_player_name_if_on_the_list_returned_right(self):
        self.assertEqual(self.stats.search(self.name_hockey),"Kurri")
    
    def test_top_by_points_returns_right_number_of_players(self):
        self.assertEqual(len(self.stats.top(self.maara)), 3)

    def test_givev_team_player_count_right(self):
        self.assertEqual(len(self.stats.team(self.joukkue)),3)

    def test_top_by_assists_returns_right_name_of_top_assists_getter(self):
        self.assertEqual(str(self.stats.top(self.yksi_top,3)[0].name), "Gretzky")

    def test_top_by_goals_returns_right_goal_number_of_top_goal_getter(self):
        self.assertEqual((self.stats.top(self.yksi_top,2)[0].goals), 45)

    def test_top_by_assists_returns_right_assists_number_of_top_assists_getter(self):
        self.assertEqual((self.stats.top(self.yksi_top,3)[0].assists), 89)  

    def test_top_by_points_returns_right_point_number_of_the_top_points_getter_with_sort_key(self):
        self.assertEqual((self.stats.top(self.yksi_top,1)[0].points), 124)    

    def test_top_by_points_return_right_point_number_of_the_top_points_getter_without_sortkey(self):
        self.assertEqual((self.stats.top(self.yksi_top)[0].points), 124)               

    
