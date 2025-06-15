class Gamification:
    def update_leaderboard(self, user_id, user_points):
        """Return leaderboard list with a single tuple of user_id and user_points."""
        leaderboard = []
        leaderboard.append((user_id, user_points))
        return leaderboard
