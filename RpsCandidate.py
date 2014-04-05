ROCK, PAPER, SCISSORS = range(3)

class RpsCandidate:
    """
    Abstract base class for candidates for the
    Pi In The Sky: Rock Paper Scissors Competition
    """

    def __init__(self):
        pass

    def getNextMove(self):
        """
        Get the next move in the game

        Returns:
            the next move (ROCK, PAPER, or SCISSORS)
        """
        pass
        
    def setOpponentsLastMove(self, move):
        """
        Set the opponents last move
        
        Args:
            move: the opponents last move (ROCK, PAPER, or SCISSORS)
        """
        pass

