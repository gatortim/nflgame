import pytest
import unittest
from nflgame import constants


class TestGame(unittest.TestCase):
    def test_teams(self):
        fp = constants.teams
        assert ["DEN", "Denver", "Broncos", "Denver Broncos"] in fp

    def test_season(self):
        s = constants.SeasonTypes
        assert s.pre.value == "PRE"
