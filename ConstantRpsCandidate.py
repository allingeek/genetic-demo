from RpsCandidate import *

class ConstantRpsCandidate(RpsCandidate):
    """
    This is an instance of RpsCandidate that always returns ROCK
    """
    def __init__(self):
        RpsCandidate.__init__(self)

    def getNextMove(self):
        """
        Get the next move in the game

        Returns:
            the next move (ROCK, PAPER, or SCISSORS)
        """
        return ROCK
        
    def setOpponentsLastMove(self, move):
        """
        Set the opponents last move
        
        Args:
            move: the opponents last move (ROCK, PAPER, or SCISSORS)
        """
        pass

