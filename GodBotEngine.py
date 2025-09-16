"""
-This Class is responsible for handling the main chess engine logic.
-It is also responsible for storing the information related to the current state of the game.
-It is also be responsible for determining the valid moves at the current state.
-It is also responsible for keeping a move log.
"""

import numpy as np

class GameState():
    def __int__(self):
        self.board = np.array([])