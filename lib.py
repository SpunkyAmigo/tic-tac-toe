#
# This library will provide functions for the gameplay of Tic Tac Toe
#
#

from abc import ABC, abstractmethod
from copy import deepcopy
import numpy as np
import os


# Helper function 
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class TTTGame:
    def __init__(self, mapping={0: '-', 1: 'X', 2: 'O'}):
        # Player 1's turn by default
        self.player_turn = 1

        # The board will be represented as a 3x3 numpy array
        # 0 - Represents an empty cell
        # 1 - Represents player 1's mark
        # 2 - Represents player 2's mark
        self.board = np.zeros((3, 3), dtype=np.int8)
        self.vectorized_mapping = np.vectorize(mapping.get)
    
    # Places a mark on the board
    # Returns True or False based on whether the move was successful
    def move(self, move: tuple):
        # Check if the move is valid
        if move is None:
            return False

        i, j = move

        # Check if the move is valid
        # i and j should be between 0 and 2
        # The cell should be empty
        if not (0 <= i <= 2 and 0 <= j <= 2) or not self.board[i, j] == 0:
            return False

        # Place the mark on the board
        self.board[i, j] = self.player_turn
        
        # Switch the player's turn
        self.player_turn = 3 - self.player_turn

        return True
    
    # Get position of all empty cells as tuples [(i, j)]
    def get_all_moves(self):
        indices = np.where(self.board == 0)
        moves = list(zip(indices[0], indices[1]))
        return moves
    
    # Get the current state of the game
    # 0 - Game is still in progress
    # 1 - Player 1 wins
    # 2 - Player 2 wins
    # 3 - Draw
    def is_over(self):
        # Check win status for both players
        for player in [1, 2]:
            status = self.board == player
            column_status = np.any(np.all(status, axis=0))
            row_status = np.any(np.all(status, axis=1))
            diagonal_status = np.all(np.diag(status))
            anti_diagonal_status = np.all(np.diag(np.rot90(status)))

            # Player has won
            if column_status or row_status or diagonal_status or anti_diagonal_status:
                return player
            
        # Draw
        # No empty cells left
        if not np.any(self.board == 0):
            return 3
        
        # Game is still in progress
        return 0

    # Display current status of game
    # player's turn and board
    def display(self):
        symbol = self.vectorized_mapping(self.player_turn)
        print(f"Player {self.player_turn}'s turn ({symbol})")
        board = self._get_readable_board()
        for row in board:
            print(*row)

    # Get the board from numerical values to mapping set by user
    def _get_readable_board(self):
        converted_array = self.vectorized_mapping(self.board)
        board = list(converted_array)
        return board


# Abstract class for Player
class TTTPlayer(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_move(self, game: TTTGame):
        pass


# Human Player with ability to give input
class TTTHuman(TTTPlayer):
    def get_move(self, game: TTTGame):
        board = game._get_readable_board()

        # Transform into a user friendly board with numbers as options
        moves = []
        counter = 1
        for i in range(3):
            for j in range(3):
                moves.append((i, j))
                if board[i][j] == '-':
                    board[i][j] = counter
                counter += 1

        # Display the transformed board        
        for row in board:
            print(*row)
        
        # Input from options
        n = int(input('Select number: '))
        move = moves[n - 1]
        
        return move


class TTTHopelessAI(TTTPlayer):
    def __init__(self, player, depth=9):
        self.player = player
        self.depth = depth

    # Min max algorithm with alpha beta pruning    
    def minmax(self, game, depth, alpha, beta, max_player):
        winner = game.is_over()
        if depth == 0 or winner:
            return self.evaluate(game, winner)
        
        if max_player:
            max_eval = float('-inf')
            for move in game.get_all_moves():
                new_game = deepcopy(game)
                new_game.move(move)
                _eval = self.minmax(new_game, depth - 1, alpha, beta, False)
                max_eval = max(_eval, max_eval)
                alpha = max(alpha, _eval)
                if beta <= alpha:
                    break
            return alpha
        else:
            min_eval = float('inf')
            for move in game.get_all_moves():
                new_game = deepcopy(game)
                new_game.move(move)
                _eval = self.minmax(new_game, depth - 1, alpha, beta, True)
                min_eval = min(_eval, min_eval)
                beta = min(beta, _eval)
                if alpha >= beta:
                    break
            return beta
    
    def evaluate(self, game: TTTGame, winner):
        if winner == self.player:
            return np.inf

        return 0

    # Get the best possible move
    def get_move(self, game):
        best_move = None
        best_val = -np.inf
        for move in game.get_all_moves():
            new_game = deepcopy(game)
            new_game.move(move)
            _eval = self.minmax(new_game, self.depth - 1, -np.inf, np.inf, False)
            if _eval > best_val:
                best_move = move
                best_val = _eval
        return best_move


class TTTConfidentAI(TTTPlayer):
    def __init__(self, player, depth=9):
        self.player = player
        self.depth = depth

    # Min max algorithm with alpha beta pruning    
    def minmax(self, game, depth, alpha, beta, max_player):
        winner = game.is_over()
        if depth == 0 or winner:
            return self.evaluate(game, winner)
        
        if max_player:
            max_eval = float('-inf')
            for move in game.get_all_moves():
                new_game = deepcopy(game)
                new_game.move(move)
                _eval = self.minmax(new_game, depth - 1, alpha, beta, False)
                max_eval = max(_eval, max_eval)
                alpha = max(alpha, _eval)
                if beta <= alpha:
                    break
            return alpha
        else:
            min_eval = float('inf')
            for move in game.get_all_moves():
                new_game = deepcopy(game)
                new_game.move(move)
                _eval = self.minmax(new_game, depth - 1, alpha, beta, True)
                min_eval = min(_eval, min_eval)
                beta = min(beta, _eval)
                if alpha >= beta:
                    break
            return beta
    
    def evaluate(self, game: TTTGame, winner):
        if winner == self.player:
            return np.inf
        if winner == 3:
            return np.inf
        
        return np.sum(game.board == 3 - self.player)

    # Count in how many positions is the opponent winning
    def _count_opponent_winnings(self, game: TTTGame):
        count = 0
        for move in game.get_all_moves():
            new_game = deepcopy(game)
            new_game.move(move)
            count += (3 - self.player) == new_game.is_over()
        return count
    
    # Get the best possible move
    # and dont loose hope when there is no way to win
    def get_move(self, game):
        best_move = None
        best_val = -np.inf
        for move in game.get_all_moves():
            new_game = deepcopy(game)
            new_game.move(move)
            """
            The AI knows when it is dead lost against a top notch player. So it tends to make random moves.
            To encourage the AI to fight longer than it can, reduce the amount of winning position the opponent can have.
            Also encourage to make more moves (prolong the game).
            """
            _eval = self.minmax(new_game, self.depth - 1, -np.inf, np.inf, False) - self._count_opponent_winnings(new_game)
            if _eval > best_val:
                best_move = move
                best_val = _eval
        return best_move
    

# This player will play the game randomly
class TTTRandom(TTTPlayer):
    def get_move(self, game: TTTGame):
        # Select random moves
        moves = game.get_all_moves()
        n = len(moves)
        random = np.random.randint(n)
        move = moves[random]
        return move
