import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_returns_player(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")
        
    def test_player_not_found(self):
        player = self.statistics.search("Selanne")
        self.assertEqual(player, None)

    def test_players_of_team(self):
        team = self.statistics.team("EDM")
        self.assertEqual(len(team), 3)
        self.assertEqual(team[0].name, "Semenko")

    def test_top_scorers(self):
        players = self.statistics.top_scorers(3)
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Gretzky")

        


