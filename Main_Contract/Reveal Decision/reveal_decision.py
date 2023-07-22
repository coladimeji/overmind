class SplitOrStealGame:
    # Other methods and class variables here...

    def reveal_decision(self, decision, salt):
        decision_hash = self.calculate_decision_hash(decision, salt)
        assert decision_hash in self.decisions, "Invalid decision hash."
        game_id, player, _ = self.decisions[decision_hash]
        game = self.games[game_id]
        assert game[player + "_decision_hash"] == decision_hash, "Decisions do not match."
        self.decisions.pop(decision_hash)
        game["reveal_count"] += 1
        if game["reveal_count"] == 2:
            self.compute_results(game_id)
