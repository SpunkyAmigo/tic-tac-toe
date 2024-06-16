from lib import TTTConfidentAI, TTTHuman
from game import TicTacToe

loop = TicTacToe(
    TTTConfidentAI(1),
    TTTHuman(),
    random_iterations=2
)

loop.play()