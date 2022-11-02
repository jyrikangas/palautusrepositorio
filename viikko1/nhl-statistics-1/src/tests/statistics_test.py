import unittest
from statistics import Statistics
from player import Player

from enum import Enum

from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3


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
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual(str(self.statistics.search("Semenko")), "Semenko EDM 4 + 12 = 16")
        
    def test_search_nonexistant(self):
        self.assertIsNone(self.statistics.search("asfasf"))
        
    def test_team_returns_correct_list(self):
        list = self.statistics.team("EDM")
        self.assertEqual(len(list), 3)
        self.assertEqual(list[0].team, "EDM")
        
    def test_top_returns_correct_list(self):
        list = self.statistics.top(3, SortBy.POINTS)
        self.assertEqual(len(list), 4)
        self.assertEqual(list[0].name, "Gretzky")
    def test_top_returns_correct_list_by_assists(self):
        list = self.statistics.top(3, SortBy.ASSISTS)
        self.assertEqual(len(list), 4)
        self.assertEqual(list[1].name, "Yzerman")
    def test_top_returns_correct_list_by_goals(self):
        list = self.statistics.top(3, SortBy.GOALS)
        self.assertEqual(len(list), 4)
        self.assertEqual(list[1].name, "Yzerman")