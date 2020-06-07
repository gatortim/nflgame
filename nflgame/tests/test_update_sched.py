import unittest
from nflgame import update_sched


class TestSched(unittest.TestCase):
    def test_url(self):
        test_url = update_sched.schedule_url(2019, "PRE", 1)
        assert "week=1" in test_url
