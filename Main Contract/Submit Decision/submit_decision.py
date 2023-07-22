import hashlib

class SplitOrStealGame:
    # Other methods and class variables here...

    def submit_decision(self, game_id, decision, salt):
        assert game_id in self.games, "Game does not exist."
        game = self.games[game_id]
        player = self.get_sender()  # Replace this with the method to get the player's address (sender).
        assert game[player + "_decision_hash"] is None, "Decision already submitted."

        decision_hash = self.calculate_decision_hash(decision, salt)
        self.decisions[decision_hash] = game_id, player, salt
        game[player + "_decision_hash"] = decision_hash
