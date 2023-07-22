from datetime import datetime
from ftplib import MSG_OOB;



def create_game(self, player1, player2, prize_pool):
        assert MSG_OOB.sender == self.contract_deployer, "Only the contract deployer can create games."
        game_id = self.get_game_id(player1, player2)
        self.games[game_id] = {
            "player1": player1,
            "player2": player2,
            "prize_pool": prize_pool,
            "expiration_time": datetime.now() + self.expiration_time,
            "player1_decision_hash": None,
            "player2_decision_hash": None,
            "reveal_count": 0
        }
        self.prize_pool += prize_pool
