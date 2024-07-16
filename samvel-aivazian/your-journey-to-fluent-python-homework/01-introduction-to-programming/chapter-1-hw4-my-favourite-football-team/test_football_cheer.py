# test_football_cheer.py

import unittest

from football_cheer import FootballCheer


class TestFootballCheer(unittest.TestCase):
    def test_cheer(self):
        team_name = "Barcelona"
        cheer = FootballCheer(team_name)
        self.assertEqual(cheer.cheer(), "Barcelona are the champions!")


if __name__ == "__main__":
    unittest.main()
