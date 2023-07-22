import unittest
from main_contract import SplitOrStealGame

class TestSplitOrStealGame(unittest.TestCase):
    def setUp(self):
        self.contract_deployer = "0x123abc"  # Replace with an actual Ethereum address
        self.game = SplitOrStealGame(self.contract_deployer)

    def test_create_game(self):
        player1 = "0x456def"  # Replace with an actual Ethereum address
        player2 = "0x789ghi"  # Replace with an actual Ethereum address
        prize_pool = 1000  # Replace with the desired prize pool value
        game_id = self.game.create_game(player1, player2, prize_pool)

        self.assertEqual(self.game.games[game_id]["player1"], player1)
        self.assertEqual(self.game.games[game_id]["player2"], player2)
        self.assertEqual(self.game.games[game_id]["prize_pool"], prize_pool)
        self.assertIsNotNone(self.game.games[game_id]["expiration_time"])
        self.assertIsNone(self.game.games[game_id]["player1_decision_hash"])
        self.assertIsNone(self.game.games[game_id]["player2_decision_hash"])
        self.assertEqual(self.game.prize_pool, prize_pool)

    def test_submit_decision(self):
        player1 = "0x456def"  # Replace with an actual Ethereum address
        player2 = "0x789ghi"  # Replace with an actual Ethereum address
        prize_pool = 1000  # Replace with the desired prize pool value
        game_id = self.game.create_game(player1, player2, prize_pool)

        decision_hash1 = "hash_of_decision1"  # Replace with an actual decision hash
        salt1 = "salt_for_decision1"  # Replace with an actual salt
        self.game.submit_decision(game_id, decision_hash1, salt1)

        self.assertEqual(self.game.games[game_id]["player1_decision_hash"], decision_hash1)
        self.assertIn(decision_hash1, self.game.decisions)

    # Add more test cases for other contract functions...

if __name__ == "__main__":
    unittest.main()
