import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from gamification import Gamification


def test_update_leaderboard_returns_correct_list():
    gamification = Gamification()
    result = gamification.update_leaderboard('user1', 100)
    assert result == [('user1', 100)]


if __name__ == '__main__':
    raise SystemExit(pytest.main([__file__]))
