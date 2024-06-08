from lib import TTTConfidentAI
from game import TicTacToe

loop = TicTacToe(
    TTTConfidentAI(1),
    TTTConfidentAI(2),
    random_iterations=3
)

loop.play()