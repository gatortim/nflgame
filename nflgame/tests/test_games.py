import unittest
import nflgame.game


class TestGames(unittest.TestCase):
    games = nflgame.games(2013, week=1)
    assert len(games) == 16
